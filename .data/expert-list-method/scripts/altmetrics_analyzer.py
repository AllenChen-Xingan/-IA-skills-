#!/usr/bin/env python3
"""
Altmetrics Analyzer
===================

Fetch and analyze Altmetric Attention Scores for research papers.

Features:
- Fetch Altmetric data by DOI, PMID, or arXiv ID
- Calculate aggregate scores for multiple papers
- Generate reports with visualizations
- Export data to CSV/JSON

Usage:
    python altmetrics_analyzer.py --doi 10.1038/nature12373
    python altmetrics_analyzer.py --pmid 12345678
    python altmetrics_analyzer.py --file dois.txt --output report.json

Requirements:
    pip install requests pandas tabulate

Author: Claude Code (IA Skills)
Version: 1.0.0
Created: 2026-01-11
"""

import argparse
import json
import sys
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Install with: pip install requests")
    sys.exit(1)

try:
    import pandas as pd
except ImportError:
    pd = None
    print("Warning: 'pandas' not found. CSV export disabled. Install with: pip install pandas")

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None
    print("Warning: 'tabulate' not found. Table display disabled. Install with: pip install tabulate")


# Altmetric API Configuration
ALTMETRIC_API_BASE = "https://api.altmetric.com/v1"


@dataclass
class AltmetricData:
    """Data class for Altmetric information."""
    identifier: str
    identifier_type: str
    altmetric_id: Optional[int] = None
    score: Optional[float] = None
    title: Optional[str] = None
    journal: Optional[str] = None
    published_on: Optional[str] = None

    # Mention counts
    twitter: int = 0
    news: int = 0
    blogs: int = 0
    facebook: int = 0
    reddit: int = 0
    wikipedia: int = 0
    policy: int = 0
    patents: int = 0
    peer_review: int = 0

    # Additional metrics
    mendeley_readers: int = 0
    cited_by_posts_count: int = 0

    # Context
    percentile: Optional[float] = None
    context_all: Optional[str] = None

    # Status
    error: Optional[str] = None


class AltmetricAnalyzer:
    """Analyzer for Altmetric data."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize analyzer.

        Args:
            api_key: Optional Altmetric API key for unlimited access
        """
        self.api_key = api_key
        self.session = requests.Session()

    def fetch_by_doi(self, doi: str) -> AltmetricData:
        """
        Fetch Altmetric data by DOI.

        Args:
            doi: Digital Object Identifier

        Returns:
            AltmetricData object
        """
        url = f"{ALTMETRIC_API_BASE}/fetch?doi={doi}"
        if self.api_key:
            url += f"&key={self.api_key}"

        return self._fetch_data(url, doi, "DOI")

    def fetch_by_pmid(self, pmid: str) -> AltmetricData:
        """
        Fetch Altmetric data by PubMed ID.

        Args:
            pmid: PubMed ID

        Returns:
            AltmetricData object
        """
        url = f"{ALTMETRIC_API_BASE}/fetch?pmid={pmid}"
        if self.api_key:
            url += f"&key={self.api_key}"

        return self._fetch_data(url, pmid, "PMID")

    def fetch_by_arxiv(self, arxiv_id: str) -> AltmetricData:
        """
        Fetch Altmetric data by arXiv ID.

        Args:
            arxiv_id: arXiv identifier

        Returns:
            AltmetricData object
        """
        url = f"{ALTMETRIC_API_BASE}/fetch?arxiv={arxiv_id}"
        if self.api_key:
            url += f"&key={self.api_key}"

        return self._fetch_data(url, arxiv_id, "arXiv")

    def _fetch_data(self, url: str, identifier: str, id_type: str) -> AltmetricData:
        """
        Fetch data from Altmetric API.

        Args:
            url: API endpoint URL
            identifier: Article identifier
            id_type: Type of identifier (DOI, PMID, arXiv)

        Returns:
            AltmetricData object
        """
        try:
            response = self.session.get(url, timeout=10)

            if response.status_code == 404:
                return AltmetricData(
                    identifier=identifier,
                    identifier_type=id_type,
                    error="Not found in Altmetric database"
                )

            response.raise_for_status()
            data = response.json()

            # Extract counts safely
            counts = data.get('counts', {})

            return AltmetricData(
                identifier=identifier,
                identifier_type=id_type,
                altmetric_id=data.get('altmetric_id'),
                score=data.get('score'),
                title=data.get('title'),
                journal=data.get('journal'),
                published_on=str(data.get('published_on', '')),
                twitter=counts.get('twitter', 0),
                news=counts.get('news', 0),
                blogs=counts.get('blogs', 0),
                facebook=counts.get('facebook', 0),
                reddit=counts.get('reddit', 0),
                wikipedia=data.get('cited_by_wikipedia_count', 0),
                policy=counts.get('policy', 0),
                patents=counts.get('patents', 0),
                peer_review=counts.get('peer_review', 0),
                mendeley_readers=data.get('readers', {}).get('mendeley', 0),
                cited_by_posts_count=data.get('cited_by_posts_count', 0),
                percentile=data.get('context', {}).get('all', {}).get('pct', None),
                context_all=data.get('context', {}).get('all', {}).get('rank', None)
            )

        except requests.exceptions.RequestException as e:
            return AltmetricData(
                identifier=identifier,
                identifier_type=id_type,
                error=f"Request error: {str(e)}"
            )
        except Exception as e:
            return AltmetricData(
                identifier=identifier,
                identifier_type=id_type,
                error=f"Unexpected error: {str(e)}"
            )

    def fetch_batch(self, identifiers: List[tuple]) -> List[AltmetricData]:
        """
        Fetch Altmetric data for multiple articles.

        Args:
            identifiers: List of (identifier, type) tuples
                        type can be 'doi', 'pmid', or 'arxiv'

        Returns:
            List of AltmetricData objects
        """
        results = []

        for identifier, id_type in identifiers:
            if id_type.lower() == 'doi':
                result = self.fetch_by_doi(identifier)
            elif id_type.lower() == 'pmid':
                result = self.fetch_by_pmid(identifier)
            elif id_type.lower() == 'arxiv':
                result = self.fetch_by_arxiv(identifier)
            else:
                result = AltmetricData(
                    identifier=identifier,
                    identifier_type=id_type,
                    error=f"Unknown identifier type: {id_type}"
                )

            results.append(result)

        return results

    @staticmethod
    def calculate_aggregate_stats(data_list: List[AltmetricData]) -> Dict:
        """
        Calculate aggregate statistics for multiple articles.

        Args:
            data_list: List of AltmetricData objects

        Returns:
            Dictionary with aggregate statistics
        """
        valid_data = [d for d in data_list if d.score is not None]

        if not valid_data:
            return {
                'total_articles': len(data_list),
                'valid_articles': 0,
                'error': 'No valid data found'
            }

        scores = [d.score for d in valid_data]

        return {
            'total_articles': len(data_list),
            'valid_articles': len(valid_data),
            'total_score': sum(scores),
            'average_score': sum(scores) / len(scores),
            'max_score': max(scores),
            'min_score': min(scores),
            'total_twitter': sum(d.twitter for d in valid_data),
            'total_news': sum(d.news for d in valid_data),
            'total_blogs': sum(d.blogs for d in valid_data),
            'total_wikipedia': sum(d.wikipedia for d in valid_data),
            'total_policy': sum(d.policy for d in valid_data),
            'total_mendeley': sum(d.mendeley_readers for d in valid_data),
            'avg_twitter': sum(d.twitter for d in valid_data) / len(valid_data),
            'avg_news': sum(d.news for d in valid_data) / len(valid_data),
            'avg_mendeley': sum(d.mendeley_readers for d in valid_data) / len(valid_data)
        }

    @staticmethod
    def print_report(data: Union[AltmetricData, List[AltmetricData]]):
        """
        Print formatted report.

        Args:
            data: Single AltmetricData or list of AltmetricData objects
        """
        if isinstance(data, AltmetricData):
            AltmetricAnalyzer._print_single_report(data)
        else:
            AltmetricAnalyzer._print_batch_report(data)

    @staticmethod
    def _print_single_report(data: AltmetricData):
        """Print report for single article."""
        print("\n" + "="*70)
        print("ALTMETRIC REPORT")
        print("="*70)

        if data.error:
            print(f"\n❌ Error: {data.error}")
            print(f"Identifier: {data.identifier} ({data.identifier_type})")
            return

        print(f"\n📄 Article Information:")
        print(f"   Identifier: {data.identifier} ({data.identifier_type})")
        if data.title:
            print(f"   Title: {data.title[:80]}...")
        if data.journal:
            print(f"   Journal: {data.journal}")
        if data.published_on:
            print(f"   Published: {data.published_on}")

        print(f"\n⭐ Altmetric Attention Score: {data.score}")

        if data.percentile:
            print(f"   Percentile: Top {100 - data.percentile:.1f}% of all articles")

        print(f"\n📊 Attention Breakdown:")
        print(f"   Twitter mentions: {data.twitter}")
        print(f"   News mentions: {data.news}")
        print(f"   Blog mentions: {data.blogs}")
        print(f"   Facebook mentions: {data.facebook}")
        print(f"   Reddit mentions: {data.reddit}")
        print(f"   Wikipedia citations: {data.wikipedia}")
        print(f"   Policy citations: {data.policy}")
        print(f"   Patent citations: {data.patents}")
        print(f"   Peer reviews: {data.peer_review}")

        print(f"\n📚 Readership:")
        print(f"   Mendeley readers: {data.mendeley_readers}")
        print(f"   Total posts: {data.cited_by_posts_count}")

        print("\n" + "="*70 + "\n")

    @staticmethod
    def _print_batch_report(data_list: List[AltmetricData]):
        """Print report for multiple articles."""
        print("\n" + "="*70)
        print("ALTMETRIC BATCH REPORT")
        print("="*70)

        # Individual articles
        if tabulate:
            table_data = []
            for d in data_list:
                if d.error:
                    table_data.append([
                        d.identifier[:30],
                        d.identifier_type,
                        "ERROR",
                        "-",
                        "-",
                        "-",
                        d.error[:30]
                    ])
                else:
                    table_data.append([
                        d.identifier[:30],
                        d.identifier_type,
                        f"{d.score:.1f}" if d.score else "-",
                        d.twitter,
                        d.news,
                        d.mendeley_readers,
                        "✓"
                    ])

            print("\n📄 Individual Articles:")
            print(tabulate(
                table_data,
                headers=["Identifier", "Type", "Score", "Twitter", "News", "Mendeley", "Status"],
                tablefmt="grid"
            ))
        else:
            print("\n📄 Individual Articles:")
            for i, d in enumerate(data_list, 1):
                status = "✓" if not d.error else f"❌ {d.error}"
                score = f"{d.score:.1f}" if d.score else "-"
                print(f"   {i}. {d.identifier} ({d.identifier_type}): Score={score} {status}")

        # Aggregate statistics
        stats = AltmetricAnalyzer.calculate_aggregate_stats(data_list)

        print(f"\n📊 Aggregate Statistics:")
        print(f"   Total articles: {stats['total_articles']}")
        print(f"   Valid articles: {stats['valid_articles']}")

        if stats['valid_articles'] > 0:
            print(f"   Total Altmetric score: {stats['total_score']:.1f}")
            print(f"   Average score: {stats['average_score']:.1f}")
            print(f"   Max score: {stats['max_score']:.1f}")
            print(f"   Min score: {stats['min_score']:.1f}")
            print(f"\n   Total Twitter mentions: {stats['total_twitter']}")
            print(f"   Total news mentions: {stats['total_news']}")
            print(f"   Total blog mentions: {stats['total_blogs']}")
            print(f"   Total Wikipedia citations: {stats['total_wikipedia']}")
            print(f"   Total policy citations: {stats['total_policy']}")
            print(f"   Total Mendeley readers: {stats['total_mendeley']}")

        print("\n" + "="*70 + "\n")

    @staticmethod
    def export_to_json(data: Union[AltmetricData, List[AltmetricData]],
                      output_file: str):
        """
        Export data to JSON file.

        Args:
            data: Single AltmetricData or list of AltmetricData objects
            output_file: Output file path
        """
        if isinstance(data, AltmetricData):
            data_dict = asdict(data)
        else:
            data_dict = {
                'articles': [asdict(d) for d in data],
                'aggregate_stats': AltmetricAnalyzer.calculate_aggregate_stats(data)
            }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data_dict, f, indent=2, ensure_ascii=False)

        print(f"✓ Data exported to {output_file}")

    @staticmethod
    def export_to_csv(data_list: List[AltmetricData], output_file: str):
        """
        Export data to CSV file.

        Args:
            data_list: List of AltmetricData objects
            output_file: Output file path
        """
        if pd is None:
            print("Error: pandas not installed. Cannot export to CSV.")
            return

        df = pd.DataFrame([asdict(d) for d in data_list])
        df.to_csv(output_file, index=False)

        print(f"✓ Data exported to {output_file}")


def read_identifiers_from_file(file_path: str) -> List[tuple]:
    """
    Read identifiers from file.

    File format (one per line):
        DOI: 10.1038/nature12373
        PMID: 12345678
        arXiv: 1234.5678

    Or simple format (assumes DOI):
        10.1038/nature12373
        10.1126/science.1234567

    Args:
        file_path: Path to input file

    Returns:
        List of (identifier, type) tuples
    """
    identifiers = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if ':' in line:
                id_type, identifier = line.split(':', 1)
                identifiers.append((identifier.strip(), id_type.strip()))
            else:
                # Assume DOI
                identifiers.append((line, 'DOI'))

    return identifiers


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch and analyze Altmetric Attention Scores",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single article by DOI
  python altmetrics_analyzer.py --doi 10.1038/nature12373

  # Single article by PMID
  python altmetrics_analyzer.py --pmid 12345678

  # Batch processing from file
  python altmetrics_analyzer.py --file dois.txt --output report.json

  # With API key for unlimited access
  python altmetrics_analyzer.py --doi 10.1038/nature12373 --api-key YOUR_KEY
        """
    )

    parser.add_argument('--doi', help='DOI of the article')
    parser.add_argument('--pmid', help='PubMed ID of the article')
    parser.add_argument('--arxiv', help='arXiv ID of the article')
    parser.add_argument('--file', help='File with list of identifiers')
    parser.add_argument('--api-key', help='Altmetric API key (optional)')
    parser.add_argument('--output', help='Output file (JSON or CSV)')
    parser.add_argument('--format', choices=['json', 'csv'], default='json',
                       help='Output format (default: json)')

    args = parser.parse_args()

    # Validate arguments
    if not any([args.doi, args.pmid, args.arxiv, args.file]):
        parser.error("Must specify --doi, --pmid, --arxiv, or --file")

    # Initialize analyzer
    analyzer = AltmetricAnalyzer(api_key=args.api_key)

    # Fetch data
    if args.file:
        # Batch processing
        identifiers = read_identifiers_from_file(args.file)
        print(f"Processing {len(identifiers)} identifiers...")
        results = analyzer.fetch_batch(identifiers)
        analyzer.print_report(results)

        if args.output:
            if args.format == 'csv':
                analyzer.export_to_csv(results, args.output)
            else:
                analyzer.export_to_json(results, args.output)

    else:
        # Single article
        if args.doi:
            result = analyzer.fetch_by_doi(args.doi)
        elif args.pmid:
            result = analyzer.fetch_by_pmid(args.pmid)
        else:  # args.arxiv
            result = analyzer.fetch_by_arxiv(args.arxiv)

        analyzer.print_report(result)

        if args.output:
            analyzer.export_to_json(result, args.output)


if __name__ == '__main__':
    main()
