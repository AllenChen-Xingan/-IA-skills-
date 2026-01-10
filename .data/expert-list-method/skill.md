---
name: expert-list-method
description: Identifies domain experts through citation analysis and cross-validation. Use when exploring new fields, building literature reviews, finding research directions, or mentions "大牛清单", "expert list", "domain experts", "top scholars".
---

# Expert List Method (大牛清单法)

Rapidly master any academic discipline by identifying and studying 40-200 core experts instead of reading textbooks.

## Quick Start

| Step | Action | Time |
|------|--------|------|
| 1 | Search Google Scholar for domain keywords | 2 min |
| 2 | Identify top 42 scholars by H-index | 5 min |
| 3 | Cross-verify with Exa and other sources | 3 min |
| 4 | Analyze expert profiles and papers | 20 min |

**Total**: ~30 minutes to build expert list for any domain

## When to Use

- Quickly understand new academic fields
- Find research directions and inflection points
- Construct comprehensive literature reviews
- Identify emerging trends and key players
- Transition from textbooks to cutting-edge research
- Build domain intuition and judgment

**Not for**:
- Reading individual papers in depth
- Writing detailed literature reviews
- Learning basic concepts (use textbooks first)

## Core Methodology

### Step 1: Initial Search (Google Scholar)

**Action**: Search domain keywords in Google Scholar
- Example: "cognitive science", "machine learning", "quantum computing"
- Click on researcher profiles (underlined names)
- Access scholar rankings sorted by citation count

**Output**: List of 20-50 potential experts

### Step 2: Rank by Metrics

**Key Metrics**:
- **H-index**: Scholar has ≥H papers cited ≥H times
  - Example: H-index of 50 = 50 papers with 50+ citations each
  - Better reflects researcher level than impact factor alone
- **Citation count**: Total citations across all papers
- **Recent activity**: Papers published in last 2-3 years

**Selection Criteria**:
- Top 42 scholars based on domain size
- Larger domains (50,000+ books) → 100-200 experts
- Smaller domains (5,000 books) → 40-60 experts

### Step 3: Cross-Verification with Exa

**IMPORTANT**: Use Exa to find professional rankings and authoritative sources

**Exa Search Queries**:
```
"most influential [domain] researchers 2025"
"top [domain] scholars by citation"
"best [domain] scientists ranking"
"[domain] award winners"
"[domain] society presidents"
```

**Implementation**:
```markdown
When cross-verifying experts, use mcp__exa__web_search_exa with:
- query: "(best or top or brilliant or influential or most cited) [domain] researchers"
- numResults: 10-15
- type: "deep" for comprehensive search
```

**Verification Sources**:
- Authority institution rankings
- Academic society leadership (presidents, lifetime achievement)
- Award winners (Nobel, Turing, Fields Medal, etc.)
- University department faculty pages
- Conference keynote speakers

**For Chinese Scholars**:
- CNKI Scholar Database (中国知网-学者库): H-index + G-index rankings
- Baidu Scholar (百度学术): Citation count sorting
- Use Exa to find Chinese academic rankings: "中国 [领域] 学者排名"

### Step 4: Analyze Each Expert

**Information to Gather**:
1. **Academic Papers**: Understand expertise areas and credibility
2. **Knowledge Graph**: Identify collaborators and predict research directions
3. **Social Citations**: Understand different perspectives (Altmetric)
4. **Reference Materials**: Trace intellectual influences
5. **Writing Principles**: Extract core methodologies

**Paper Selection Strategy** (12 papers per expert):
- 3 highest-cited papers
- 3 most recent papers
- 3 most original papers
- 3 papers of personal interest

## Theoretical Foundation

**Lotka's Law (洛特卡定律)**:
- Author productivity follows 1/N² distribution
- Small number of authors produce large volume of papers
- Principle: Focus on high-productivity researchers for maximum efficiency

**20/80 Rule**:
- 20% of experts constitute 80% of discipline development
- 40-200 core experts = entire development history of a field
- More efficient than reading hundreds of textbooks

## Output Format

```markdown
# [Domain] Expert List

## Top 42 Experts (by H-index)

| Rank | Name | H-index | Citations | Institution | Key Research |
|------|------|---------|-----------|-------------|--------------|
| 1 | [Name] | [H] | [Count] | [Univ] | [Topics] |
| 2 | ... | ... | ... | ... | ... |

## Cross-Verification Results

### Google Scholar Top 10
- [Name 1] (H-index: X)
- [Name 2] (H-index: Y)

### Exa Search Results
- [Ranking source 1]: [Names]
- [Ranking source 2]: [Names]

### Award Winners
- [Award name]: [Winners]

## Consensus Experts (appear in 3+ sources)
1. [Name] - [Why important]
2. [Name] - [Why important]

## Next Steps
- [ ] Download top 12 papers from each expert
- [ ] Analyze collaboration networks
- [ ] Track latest publications via RSS
```

## Real-World Examples

### Example 1: Cognitive Science

**Input**: "I need to understand cognitive science quickly"

**Process**:
1. Google Scholar search: "cognitive science"
2. Top scholars: Steven Pinker (H: 172), Daniel Kahneman (H: 158), etc.
3. Exa verification: "most influential cognitive scientists 2025"
4. Cross-check: Nobel Prize winners, APS Fellows, university rankings

**Output**: 42 core experts with H-index 50+, covering:
- Language and cognition (Pinker, Chomsky)
- Decision-making (Kahneman, Tversky)
- Memory (Tulving, Schacter)
- Perception (Marr, Treisman)

**Time**: 30 minutes to build comprehensive expert list

### Example 2: Machine Learning (with Exa)

**Input**: "Find top machine learning researchers for 2025"

**Exa Query**:
```
mcp__exa__web_search_exa(
  query: "top machine learning researchers 2025 ranking",
  numResults: 15,
  type: "deep"
)
```

**Exa Results**:
- CSRankings.org: Yoshua Bengio, Geoffrey Hinton, Yann LeCun
- Google Scholar: Andrew Ng, Ian Goodfellow, Demis Hassabis
- Turing Award winners: Hinton, Bengio, LeCun (2018)

**Cross-Verification**:
- All three sources agree on "deep learning pioneers"
- H-index range: 150-200+
- Recent papers: Transformers, LLMs, multimodal learning

**Output**: 42 experts covering deep learning, reinforcement learning, NLP, computer vision

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Single source bias | Only using Google Scholar | Cross-verify with Exa + awards + institutions |
| Ignoring recent papers | Missing emerging trends | Check last 2-3 years of publications |
| Over-focusing on H-index | Missing young rising stars | Balance H-index with recent impact |
| No Chinese sources | Missing Chinese scholars | Use CNKI + Baidu Scholar + Exa Chinese search |
| Too many experts | List of 200+ scholars | Focus on top 42, expand only if needed |
| Skipping verification | Inaccurate or biased list | Always cross-check 3+ sources |

## Integration with Other Methods

**Before Expert List**:
- Use **minimal-global-cognition** to understand domain structure
- Use **time-space-variable-method** to identify information distribution

**After Expert List**:
- Use **batch-paper-acquisition** to download papers (#12)
- Use **batch-paper-reading** to analyze 100 papers (#18)
- Use **citation-analysis** for network mapping (#35)

**Complementary Tools**:
- Zotero: Organize papers with 4×5 principle
- Acemap: Visualize knowledge graphs
- CiteSpace: Citation network analysis
- RSS: Track latest publications

## Resources

### Reference Materials

**[Quality Sources Guide](references/quality-sources.md)**:
- Scholar ranking systems (Clarivate, ScholarGPS, CSRankings)
- Award winners (Nobel, Turing, Fields Medal)
- Academic societies (NAS, ACM Fellows, IEEE Fellows)
- Top journals by discipline (Nature, Science, NEJM, etc.)
- Academic databases (Web of Science, Scopus, CNKI)
- Preprint servers (arXiv, bioRxiv, medRxiv)
- University rankings (QS, THE, US News)

**[Altmetrics Evaluation Guide](references/altmetrics-guide.md)**:
- What is Altmetrics and how it differs from citations
- Major platforms (Altmetric.com, PlumX, ImpactStory)
- Altmetric Attention Score calculation
- Interpretation guidelines and best practices
- API access and tools
- Evaluation workflow for experts

### Tools & Scripts

**[Altmetrics Analyzer](scripts/altmetrics_analyzer.py)**:
- Python script for fetching Altmetric Attention Scores
- Supports DOI, PMID, arXiv ID
- Batch processing capabilities
- Export to JSON/CSV
- Aggregate statistics calculation

**Usage**:
```bash
# Single article
python scripts/altmetrics_analyzer.py --doi 10.1038/nature12373

# Batch analysis
python scripts/altmetrics_analyzer.py --file dois.txt --output report.json

# With API key
python scripts/altmetrics_analyzer.py --doi 10.1038/nature12373 --api-key YOUR_KEY
```

See [scripts/README.md](scripts/README.md) for detailed documentation.

## Advanced Tips

**Knowledge Management (4×5 Principle)**:
- Initial stage: Store all papers in single folder (< 30 papers)
- Growth stage: Create subcategories when > 30 papers (1.5× of 20)
- Naming: Use Wikipedia naming standards
- Search depth: Maximum 3 levels

**Learning Progress**:
- Initial phase: Monthly scanning
- Intermediate: Quarterly reviews
- Advanced: Semi-annual or annual
- Real-time: RSS subscriptions for breakthroughs

**Exa Best Practices**:
- Use `type: "deep"` for comprehensive expert discovery
- Search multiple query variations: "top", "best", "influential", "most cited"
- Include year in query: "2025" for latest rankings
- Search both English and Chinese: "中国 [领域] 专家"
- Set `numResults: 10-15` for cross-verification

## Quality Checklist

- [ ] Top 42 experts identified with H-index
- [ ] Cross-verified with 3+ sources (Google Scholar + Exa + awards)
- [ ] Recent papers checked (last 2-3 years)
- [ ] Chinese scholars included (if applicable)
- [ ] Collaboration networks mapped
- [ ] Papers organized in Zotero
- [ ] RSS feeds set up for tracking

---

*Version: v1.1.0*
*Created: 2026-01-11*
*Updated: 2026-01-11*
*Based on: Information Analysis Course + Lotka's Law + Exa Integration + Altmetrics*

**Changelog**:
- v1.1.0 (2026-01-11): Added comprehensive reference materials, Altmetrics guide, and Python analyzer script
- v1.0.0 (2026-01-11): Initial release with core methodology and Exa integration
