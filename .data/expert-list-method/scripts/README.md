# Altmetrics Analyzer Scripts

Python tools for fetching and analyzing Altmetric Attention Scores.

## Installation

```bash
pip install requests pandas tabulate
```

## Quick Start

### Single Article Analysis

```bash
# By DOI
python altmetrics_analyzer.py --doi 10.1038/nature12373

# By PubMed ID
python altmetrics_analyzer.py --pmid 12345678

# By arXiv ID
python altmetrics_analyzer.py --arxiv 1234.5678
```

### Batch Analysis

Create a file `dois.txt`:
```
DOI: 10.1038/nature12373
DOI: 10.1126/science.1234567
PMID: 12345678
arXiv: 1234.5678
```

Run batch analysis:
```bash
python altmetrics_analyzer.py --file dois.txt --output report.json
```

### Export Options

```bash
# Export to JSON
python altmetrics_analyzer.py --file dois.txt --output report.json --format json

# Export to CSV
python altmetrics_analyzer.py --file dois.txt --output report.csv --format csv
```

### With API Key

For unlimited access (no rate limits):
```bash
python altmetrics_analyzer.py --doi 10.1038/nature12373 --api-key YOUR_API_KEY
```

## Output Format

### Console Output

```
======================================================================
ALTMETRIC REPORT
======================================================================

📄 Article Information:
   Identifier: 10.1038/nature12373 (DOI)
   Title: The human microbiome project...
   Journal: Nature
   Published: 2013-08-29

⭐ Altmetric Attention Score: 456.5
   Percentile: Top 5.0% of all articles

📊 Attention Breakdown:
   Twitter mentions: 234
   News mentions: 45
   Blog mentions: 12
   Wikipedia citations: 3
   Policy citations: 2
   Mendeley readers: 1234

======================================================================
```

### JSON Output

```json
{
  "identifier": "10.1038/nature12373",
  "identifier_type": "DOI",
  "score": 456.5,
  "twitter": 234,
  "news": 45,
  "blogs": 12,
  "wikipedia": 3,
  "policy": 2,
  "mendeley_readers": 1234,
  "percentile": 95.0
}
```

### CSV Output

| identifier | identifier_type | score | twitter | news | blogs | wikipedia | policy | mendeley_readers |
|------------|----------------|-------|---------|------|-------|-----------|--------|------------------|
| 10.1038/... | DOI | 456.5 | 234 | 45 | 12 | 3 | 2 | 1234 |

## Use Cases

### 1. Evaluate Expert's Public Impact

```bash
# Create file with expert's paper DOIs
cat > expert_papers.txt <<EOF
DOI: 10.1038/nature12373
DOI: 10.1126/science.1234567
DOI: 10.1016/j.cell.2020.01.001
EOF

# Analyze
python altmetrics_analyzer.py --file expert_papers.txt --output expert_impact.json

# View aggregate statistics
cat expert_impact.json | jq '.aggregate_stats'
```

### 2. Compare Multiple Experts

```bash
# Analyze each expert
python altmetrics_analyzer.py --file expert1_papers.txt --output expert1.csv --format csv
python altmetrics_analyzer.py --file expert2_papers.txt --output expert2.csv --format csv

# Compare in spreadsheet or pandas
```

### 3. Track Research Dissemination

```bash
# Fetch data at different time points
python altmetrics_analyzer.py --doi 10.1038/nature12373 --output week1.json
# Wait 1 week
python altmetrics_analyzer.py --doi 10.1038/nature12373 --output week2.json
# Compare scores
```

## API Reference

### AltmetricAnalyzer Class

```python
from altmetrics_analyzer import AltmetricAnalyzer

# Initialize
analyzer = AltmetricAnalyzer(api_key="YOUR_KEY")  # api_key optional

# Fetch single article
data = analyzer.fetch_by_doi("10.1038/nature12373")
print(f"Score: {data.score}")
print(f"Twitter: {data.twitter}")

# Fetch batch
identifiers = [
    ("10.1038/nature12373", "doi"),
    ("12345678", "pmid")
]
results = analyzer.fetch_batch(identifiers)

# Calculate aggregate stats
stats = analyzer.calculate_aggregate_stats(results)
print(f"Average score: {stats['average_score']}")

# Print report
analyzer.print_report(results)

# Export
analyzer.export_to_json(results, "output.json")
analyzer.export_to_csv(results, "output.csv")
```

## Troubleshooting

### Rate Limiting

**Problem**: "429 Too Many Requests"

**Solution**:
- Wait a few minutes between requests
- Get free API key from Altmetric
- Use `--api-key` parameter

### Article Not Found

**Problem**: "Not found in Altmetric database"

**Solution**:
- Verify DOI/PMID is correct
- Article may not have any altmetric attention yet
- Try alternative identifier (DOI vs PMID)

### Import Errors

**Problem**: "ModuleNotFoundError: No module named 'requests'"

**Solution**:
```bash
pip install requests pandas tabulate
```

## Advanced Usage

### Python Integration

```python
from altmetrics_analyzer import AltmetricAnalyzer, AltmetricData

# Custom analysis
analyzer = AltmetricAnalyzer()
data = analyzer.fetch_by_doi("10.1038/nature12373")

if data.score and data.score > 100:
    print("High impact article!")

if data.news > 10:
    print("Significant news coverage")

if data.policy > 0:
    print("Cited in policy documents")
```

### Batch Processing with Progress

```python
from altmetrics_analyzer import AltmetricAnalyzer
from tqdm import tqdm  # pip install tqdm

analyzer = AltmetricAnalyzer()
dois = ["10.1038/nature12373", "10.1126/science.1234567"]

results = []
for doi in tqdm(dois, desc="Fetching"):
    result = analyzer.fetch_by_doi(doi)
    results.append(result)

analyzer.print_report(results)
```

## Resources

- Altmetric API Docs: https://api.altmetric.com/
- Altmetric Help: https://help.altmetric.com/
- Get API Key: https://www.altmetric.com/products/free-tools/

---

*Version: 1.0.0*
*Created: 2026-01-11*
