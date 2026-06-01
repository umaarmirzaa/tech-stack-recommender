import csv
import math


# Load data from CSV
def load_data(filename):
    roles = []
    role_skills = []

    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            role_name = row[0]
            skills = row[1].lower().split(",")
            skills = [s.strip() for s in skills]
            roles.append(role_name)
            role_skills.append(skills)
    return roles, role_skills


# Build vocabulary
def build_vocab(role_skills):
    vocab = []
    for skills in role_skills:
        for skill in skills:
            if skill not in vocab:
                vocab.append(skill)

    return vocab


# Compute IDF
def compute_idf(vocab, all_docs):
    idf = {}
    total_docs = len(all_docs)
    for word in vocab:
        count = 0
        for doc in all_docs:
            if word in doc:
                count += 1
        idf[word] = math.log(total_docs / count)

    return idf


# Create TF IDF vector
def make_vector(doc, vocab, idf):
    vector = []

    for word in vocab:
        tf = doc.count(word) / len(doc)
        weight = tf * idf[word]
        vector.append(weight)

    return vector


# MAIN
roles, role_skills = load_data("raw_skills.csv")
print("ROLES:")
print(roles)
print("\nROLE SKILLS:")
print(role_skills)
vocab = build_vocab(role_skills)
print("\nVOCAB:")
print(vocab)
idf = compute_idf(vocab, role_skills)
print("\nIDF VALUES:")
print(idf)
sample_vector = make_vector(role_skills[0], vocab, idf)
print("\nSAMPLE TF-IDF VECTOR:")
print(sample_vector)
