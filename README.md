# Tech Stack Recommender

A content-based recommendation engine that suggests technology career paths based on a user's technical skills using TF-IDF vectorization and cosine similarity.

---

## Features

* Content-based filtering
* TF-IDF feature weighting
* Cosine similarity scoring
* Top-3 ranked recommendations
* Cold-start handling
* No external libraries required

---

## Technologies Used

* Python
* CSV
* Math module

---

## How It Works

### Step 1 — Load Dataset

Job roles and skills are loaded from a CSV dataset.

### Step 2 — Build Vocabulary

A shared vocabulary of unique skills is created.

### Step 3 — TF-IDF Vectorization

Each role and user profile is converted into weighted numerical vectors.

```text
TF = occurrences of skill / total skills

IDF = log(total roles / roles containing skill)

TF-IDF = TF × IDF
```

### Step 4 — Cosine Similarity

The similarity between the user vector and each role vector is calculated.

```text
cosine = (A · B) / (||A|| × ||B||)
```

### Step 5 — Recommendation Ranking

Scores are sorted in descending order and the Top 3 roles are displayed.

---

## Example

Input:

```text
python
machine learning
statistics
```

Output:

```text
1. Data Scientist -> 75.6% match
2. ML Engineer -> 55.5% match
3. Data Analyst -> 13.9% match
```

---

## File Structure

```text
tech-stack-recommender/
├── recommender.py
├── raw_skills.csv
└── README.md
```

---

## Future Improvements

* GUI version
* Web deployment
* Larger datasets
* Skill proficiency weighting
* NLP preprocessing
