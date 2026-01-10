# Altmetrics Evaluation Guide

Comprehensive guide to evaluating research impact using alternative metrics (altmetrics) beyond traditional citations.

## What is Altmetrics?

**Altmetrics** (alternative metrics) measure the online attention and engagement that research receives across:
- Social media (Twitter, Facebook, Reddit)
- News coverage (mainstream media, blogs)
- Policy documents (government citations)
- Wikipedia citations
- Mendeley readers
- Online reference managers

**Key Difference from Citations**:
- **Citations**: Academic impact (slow, selective, months/years)
- **Altmetrics**: Public attention (fast, inclusive, days/weeks)

---

## 1. Major Altmetrics Platforms

### Altmetric.com (Altmetric Attention Score)

**Overview**:
- Created: 2011
- Owner: Digital Science
- Coverage: ~50.6% of Web of Science records
- Strengths: Best for news, blogs, tweets

**Key Features**:
- Altmetric Attention Score (AAS): Weighted score of online attention
- Altmetric Donut: Visual representation of attention sources
- Details Page: Full breakdown of mentions
- Explorer: Institutional tracking tool

**Access**:
- Free: Altmetric Bookmarklet (browser extension)
- Paid: Altmetric Explorer (institutional subscription)
- API: Details Page API (free tier + paid tier)

### PlumX Metrics

**Overview**:
- Created: 2012
- Owner: Elsevier (acquired 2017)
- Coverage: ~93% of Web of Science records (highest)
- Strengths: Best Mendeley reader coverage

**Five Metric Categories**:
1. **Citations**: Scopus, CrossRef, clinical/policy citations
2. **Usage**: Downloads, views, plays
3. **Captures**: Saves, bookmarks, favorites
4. **Mentions**: News, blogs, comments, reviews
5. **Social Media**: Tweets, shares, likes

**Access**: Subscription (institutional or individual)

### ImpactStory

**Overview**:
- Type: Free, open-source, nonprofit
- Access: Free with ORCID or Twitter account
- Coverage: DOI-based research outputs

**Features**:
- Tracks: Buzz, Engagement, Openness, Fun
- Percentile rankings for context
- ORCID integration for auto-import
- Depsy tool for research software impact

**Access**: Completely free

### Dimensions

**Overview**:
- Type: Discovery and analytics platform
- Integration: Collaborates with Altmetric
- Coverage: 90+ million publications

**Metrics**:
- Publication citations
- Field Citation Ratio (FCR)
- Relative Citation Ratio (RCR)
- Altmetric Attention Score

**Access**: Limited free access + subscription

---

## 2. Altmetric Attention Score (AAS) Calculation

### Three Main Factors

#### 1. Volume
- Count of mentions (one per person per source)
- More mentions = higher score
- Deduplication: Only first mention per person per source

#### 2. Source Quality/Profile
Different sources have different base weights:

| Source Type | Weight |
|-------------|--------|
| News (mainstream media) | 8 |
| Blog | 5 |
| Policy document (per source) | 3 |
| Clinical Guidelines (per source) | 3 |
| Patent | 3 |
| Wikipedia | 3 |
| Peer review (Publons, PubPeer) | 1 |
| Social media (Twitter, Facebook, Reddit) | Variable |

#### 3. Author Credibility
- Who authored the mention matters
- Influential authors/sources weighted higher
- Potential bias and audience considered
- Journal publisher mentions ≠ individual tweets

### Calculation Formula

```
Altmetric Attention Score = Σ(Volume × Source Weight × Author Credibility)
```

**Important Notes**:
- Weighted approximation, not raw total
- Proprietary algorithm (some opacity)
- Score modifiers may apply
- Time decay factors considered
- Field normalization available

---

## 3. Metrics Categories & Data Sources

### Social Media Mentions

**Twitter**:
- Weighted heavily in Altmetric
- Tracks tweets mentioning DOI or article URL
- Author credibility affects weight
- Most common altmetric source

**Facebook**:
- Public posts and shares
- Tracked by Altmetric and PlumX
- Lower weight than news

**Reddit**:
- Tracked by Altmetric
- Academic subreddits weighted higher
- Growing importance

**ResearchGate**:
- Professional network mentions
- Tracked by PlumX

### News Coverage

**Mainstream Media**:
- Weight: 8 (highest in Altmetric)
- Includes: NYT, BBC, CNN, etc.
- Indicates broad public interest

**Blogs**:
- Weight: 5
- Includes: Academic blogs, science blogs
- More specialized audience

### Policy Documents

**Weight**: 3 per source

**Tracked by**: Altmetric, PlumX

**Includes**:
- Government policy documents
- Think tank reports
- Policy briefs
- White papers

**Significance**: Research influencing policy

### Wikipedia Citations

**Weight**: 3 per source

**Coverage**: 31 language versions tracked by Altmetric

**Requirements**:
- Must be in "References" section
- Proper citation tag required
- Detection via Wikipedia Events API

**Significance**: Encyclopedic importance

### Mendeley Readers

**Definition**: Count of users who saved article to library

**Tracked by**: Altmetric, PlumX

**Important**: Does NOT contribute to Altmetric Attention Score (tracked separately)

**Access**: Via Mendeley API using DOI

**Significance**: Academic interest indicator

### Citation Counts

**Scopus**: Integrated by Altmetric and Dimensions

**Web of Science**: Traditional citation index

**CrossRef**: Open citation data

**OpenCitations**: Open access citation data

**Note**: Traditional citations tracked separately from altmetrics

---

## 4. How to Evaluate Research Using Altmetrics

### Step 1: Gather Altmetric Data

**Using Altmetric Bookmarklet** (Free):
1. Install browser extension
2. Navigate to article page
3. Click bookmarklet to see Altmetric donut
4. View breakdown of mentions

**Using Altmetric API** (Programmatic):
```python
import requests

DOI = "10.1038/nature12373"
API_KEY = "your_api_key"  # Optional for basic access

url = f"https://api.altmetric.com/v1/fetch?doi={DOI}"
response = requests.get(url)
data = response.json()

print(f"Altmetric Score: {data['score']}")
print(f"Twitter mentions: {data['counts']['twitter']}")
print(f"News mentions: {data['counts']['news']}")
print(f"Wikipedia citations: {data['cited_by_wikipedia_count']}")
```

### Step 2: Interpret the Score

**Score Ranges** (approximate):
- **0-10**: Low attention
- **10-50**: Moderate attention
- **50-100**: High attention
- **100-500**: Very high attention
- **500+**: Exceptional attention

**Context Matters**:
- Compare to similar articles in same field
- Use percentile rankings (e.g., "Top 5% of all articles")
- Consider article age (older articles have more time to accumulate attention)

### Step 3: Analyze Attention Sources

**Check the Breakdown**:
- **High news coverage**: Broad public interest
- **High Twitter**: Academic/professional discussion
- **Policy citations**: Real-world impact
- **Wikipedia citations**: Encyclopedic importance
- **High Mendeley readers**: Academic interest

**Red Flags**:
- Attention from single source only
- Negative attention (controversial findings)
- Sudden spike then silence (flash in the pan)

### Step 4: Read the Mentions

**Don't just look at the score**:
- Read actual tweets, news articles, blog posts
- Understand context (positive vs. negative)
- Check for misinterpretation or controversy
- Verify quality of sources

### Step 5: Compare with Traditional Metrics

**Combine with**:
- Citation count (Scopus, Web of Science)
- H-index (author level)
- Journal impact factor
- Field-normalized metrics

**Balanced Approach**:
- Altmetrics: Immediate/public impact
- Citations: Academic impact
- Together: Complete picture

---

## 5. Interpretation Guidelines

### What Altmetric Scores Mean

✅ **Altmetrics Indicate**:
- Online attention and engagement
- Public interest in research
- Potential for broader impact
- Speed of dissemination

❌ **Altmetrics Do NOT Indicate**:
- Research quality or validity
- Academic importance (use citations)
- Long-term impact (too early)
- Peer approval (not peer review)

### Comparison Across Disciplines

**NOT directly comparable** across fields:
- Popular topics (COVID, climate) naturally score higher
- STEM fields receive more social media attention
- Humanities/social sciences have lower baseline scores

**Use Percentile Rankings**:
- "Top 5% of all articles"
- "Top 10% in this journal"
- "Top 25% in this field"

### Limitations & Biases

**Major Limitations**:
1. **Quality Indicator**: Does NOT indicate research quality
2. **Gaming Risk**: Can be manipulated via social media
3. **Topic Bias**: Sensational topics receive more attention
4. **Incomplete Coverage**: Not all research captured
5. **Data Quality**: Errors may be undetectable
6. **Lack of Normalization**: Few sources normalize data
7. **Transparency**: Proprietary algorithm not fully transparent

**Disciplinary Biases**:
- Stronger in sciences and medicine
- Weaker in humanities and social sciences
- Interdisciplinary comparison not recommended

**Source Biases**:
- News coverage concentrated in certain topics
- Twitter activity skewed toward certain demographics
- Policy citations limited to certain countries
- Wikipedia coverage varies by language

---

## 6. Best Practices

### Do's ✅

1. **Use in Context**:
   - Compare to similar articles in same field
   - Use percentile rankings
   - Read underlying posts

2. **Combine Metrics**:
   - Use alongside traditional citations
   - Consider multiple altmetric sources
   - Don't rely on single metric

3. **Provide Context**:
   - Clearly state what metric measures
   - Acknowledge limitations
   - Use percentile rankings when available

4. **Track Over Time**:
   - Monitor attention patterns
   - Identify inflection points
   - Understand dissemination speed

### Don'ts ❌

1. **Avoid Misuse**:
   - Don't use as sole evaluation criterion
   - Don't compare across disciplines without normalization
   - Don't assume attention = quality
   - Don't use for hiring/promotion decisions alone

2. **Don't Ignore Context**:
   - Don't just look at the score
   - Don't ignore negative attention
   - Don't forget article age

3. **Don't Over-Interpret**:
   - Don't equate attention with impact
   - Don't assume causation
   - Don't ignore traditional metrics

---

## 7. Platform Comparison

| Feature | Altmetric | PlumX | ImpactStory | Dimensions |
|---------|-----------|-------|-------------|------------|
| **Coverage** | 50.6% | 93% | DOI-based | 90M+ |
| **Cost** | Subscription | Subscription | Free | Subscription |
| **Best For** | News/blogs/tweets | Mendeley readers | Individual researchers | Comprehensive |
| **Blogs** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **News** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **Twitter** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **Mendeley** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **Wikipedia** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **Policy** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **API** | Yes | Yes | Limited | Yes |
| **Free Tier** | Limited | No | Yes | No |

---

## 8. API Access & Tools

### Altmetric Details Page API

**Endpoints**:
```
GET https://api.altmetric.com/v1/fetch?doi={DOI}
GET https://api.altmetric.com/v1/fetch?pmid={PMID}
GET https://api.altmetric.com/v1/fetch?arxiv={ARXIV_ID}
```

**Supported Identifiers**:
- DOI (Digital Object Identifier)
- PMID (PubMed ID)
- arXiv ID
- ADS bibcode
- Journal ISSN

**Response Fields**:
- `altmetric_id`: Unique identifier
- `score`: Altmetric Attention Score
- `counts`: Mention counts by source
- `citation`: Citation data
- `demographics`: Reader demographics
- `posts`: Detailed mention information
- `readers`: Mendeley reader count
- `cited_by_wikipedia_count`: Wikipedia citations

**Rate Limits**:
- Free tier: Rate-limited
- Paid tier: Unlimited with API key

### Python Libraries

**PyAltmetric**:
```bash
pip install pyaltmetric
```

**Altmetric Explorer API Client**:
```bash
pip install altmetric-explorer-api-client
```

See `scripts/altmetrics_analyzer.py` for complete implementation.

---

## 9. Evaluation Workflow

### For Individual Articles

1. **Gather Data**:
   - Use Altmetric Bookmarklet or API
   - Collect Altmetric Attention Score
   - Get breakdown by source

2. **Analyze Context**:
   - Check percentile ranking
   - Compare to similar articles
   - Read actual mentions

3. **Combine Metrics**:
   - Check citation count (Scopus/WoS)
   - Check Mendeley readers
   - Check journal impact factor

4. **Interpret**:
   - What type of attention? (positive/negative)
   - Who is paying attention? (academics/public/policy)
   - Why? (novelty/controversy/practical application)

### For Expert Evaluation

1. **Aggregate Scores**:
   - Sum Altmetric scores across all papers
   - Calculate average score per paper
   - Identify highest-scoring papers

2. **Analyze Patterns**:
   - Which papers get most attention?
   - What types of attention? (news/social/policy)
   - Trends over time?

3. **Cross-Verify**:
   - Compare with citation metrics
   - Check H-index
   - Verify with traditional metrics

4. **Contextualize**:
   - Field-specific baselines
   - Career stage considerations
   - Publication venue effects

---

## 10. Common Use Cases

### Use Case 1: Evaluating Research Impact

**Scenario**: Assess broader impact of research beyond academia

**Steps**:
1. Gather Altmetric scores for all publications
2. Identify papers with high news/policy citations
3. Read mentions to understand public perception
4. Compare with citation metrics

**Outcome**: Understand public vs. academic impact

### Use Case 2: Identifying Trending Research

**Scenario**: Find emerging hot topics in a field

**Steps**:
1. Search recent papers in field
2. Sort by Altmetric score
3. Filter for recent publications (< 6 months)
4. Analyze attention sources

**Outcome**: Identify trending topics and emerging areas

### Use Case 3: Tracking Research Dissemination

**Scenario**: Monitor how research spreads online

**Steps**:
1. Track Altmetric score over time
2. Identify attention spikes
3. Analyze which sources drive attention
4. Measure dissemination speed

**Outcome**: Understand dissemination patterns

### Use Case 4: Cross-Verifying Expert Lists

**Scenario**: Validate expert lists with public impact

**Steps**:
1. Gather Altmetric scores for all experts
2. Calculate average scores per expert
3. Identify experts with high public impact
4. Cross-verify with citation metrics

**Outcome**: Balanced expert list (academic + public impact)

---

## 11. Key Research Findings

**From Comparative Studies**:

1. **Coverage Differences**:
   - PlumX tracks more sources overall (93% vs. 50.6%)
   - Altmetric better for news/blogs/tweets
   - PlumX better for Mendeley readers

2. **Data Quality**:
   - Significant differences between aggregators
   - No single "best" provider
   - Choice depends on use case

3. **Correlation with Citations**:
   - Weak to moderate correlation (r = 0.2-0.4)
   - Different time dynamics
   - Measure different aspects of impact

4. **Disciplinary Variation**:
   - STEM fields: Higher altmetric activity
   - Humanities: Lower altmetric activity
   - Social sciences: Moderate activity

---

## 12. Resources

### Official Documentation
- Altmetric Help Center: https://help.altmetric.com/
- Altmetric API Docs: https://api.altmetric.com/
- PlumX Metrics: https://plumanalytics.com/
- ImpactStory: https://profiles.impactstory.org/

### Research Papers
- "How is the Altmetric Attention Score calculated?" (Altmetric)
- "Reliability and accuracy of altmetric providers" (Springer, 2018)
- "Critical review on altmetrics" (PMC, 2021)

### Tools
- Altmetric Bookmarklet: Free browser extension
- PyAltmetric: Python library
- Altmetric Explorer: Institutional tool
- Webometric Analyst: Free Windows program

---

## Quick Reference: Evaluation Checklist

- [ ] Gather Altmetric Attention Score
- [ ] Check percentile ranking (e.g., "Top 5%")
- [ ] Analyze attention sources (news/social/policy)
- [ ] Read actual mentions (positive/negative?)
- [ ] Compare with citation count
- [ ] Check Mendeley readers
- [ ] Consider article age and field
- [ ] Use field-normalized metrics
- [ ] Combine with traditional metrics
- [ ] Provide context in reporting

---

*Version: v1.0.0*
*Created: 2026-01-11*
*Sources: Altmetric.com, PlumX, ImpactStory, Dimensions, Exa research*
