# Tech Stack Recommender - Day 2

## Overview

This project is a content-based recommendation engine that maps technical skills to relevant technology career paths.

The system now supports TF-IDF vectorization for transforming job-role skills into weighted numerical representations.

---

## Progress Completed

### Day 1

* CSV dataset loading
* Skill extraction
* Vocabulary generation

### Day 2

* TF-IDF implementation
* Inverse Document Frequency computation
* Vector representation of job roles

---

## How TF-IDF Works

### TF (Term Frequency)

Measures how often a skill appears in a role.

```text
TF = occurrences of skill / total skills in role
```

### IDF (Inverse Document Frequency)

Measures how unique a skill is across all job roles.

```text
IDF = log(total roles / roles containing skill)
```

### TF-IDF Weight

```text
TF-IDF = TF × IDF
```

Skills that appear in many roles become less important, while specialized skills become stronger signals.

---

## Current Pipeline

```text
CSV Dataset
    ↓
Skill Extraction
    ↓
Vocabulary Construction
    ↓
TF-IDF Vectorization
```

---

## Current Status

✅ Dataset loading

✅ Vocabulary generation

✅ TF-IDF vectors

⬜ Cosine similarity

⬜ Recommendation ranking

⬜ Top-3 career suggestions

---

