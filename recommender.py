# Tech Stack Recommender  -  Project 3
# AI Recommendation Logic (DecodeLabs Industrial Training Kit)
# What it does:
# You type in 3 skills you like, and the program tells you
# which career path (job role) matches you the best.
#
# How it works:
# 1. TF IDF vectorization
# 2. Cosine similarity comparison
# 3. Rank job roles
# 4. Show Top 3 recommendations

import csv
import math

# Load job roles from CSV
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

# Step 3: Compute IDF
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

# Step 4: Create TF IDF vector
def make_vector(doc, vocab, idf):
    vector = []
    for word in vocab:
        tf = doc.count(word) /len(doc)
        weight = tf * idf[word]
        vector.append(weight)
    return vector


# Step 5: Cosine Similarity
def cosine_similarity(vec1, vec2):
    point = 0
    for i in range(len(vec1)):
        point += vec1[i] * vec2[i]
    size1 = math.sqrt(sum(v * v for v in vec1))
    size2 = math.sqrt(sum(v * v for v in vec2))

    # cold-start protection
    if size1 == 0 or size2 == 0:
        return 0

    return point / (size1 * size2)


# MAIN PROGRAM
def main():
    print("TECH STACK RECOMMENDER")
    print("Enter 3 skills you enjoy.\n")

    # load dataset
    roles, role_skills = load_data("raw_skills.csv")

    # prepare vocabulary and IDF
    vocab = build_vocab(role_skills)
    idf = compute_idf(vocab, role_skills)

    # user input
    user_skills = []

    for i in range(3):
        skill = input("Enter skill " + str(i + 1) + ": ")
        user_skills.append(skill.lower().strip())

    print("\nYour skills:", user_skills)

    # vectorize user profile
    user_vector = make_vector(user_skills, vocab, idf)

    # compute similarity scores
    scores = []

    for i in range(len(roles)):
        role_vector = make_vector(role_skills[i], vocab, idf)
        score = cosine_similarity(user_vector, role_vector)
        scores.append((roles[i], score))
    # sort descending
    scores.sort(key=lambda x: x[1], reverse=True)
    # show top 3
    print("\nTOP 3 RECOMMENDATIONS")

    for i in range(3):
        role = scores[i][0]
        match = scores[i][1] * 100
        print(str(i + 1) + ". " + role + " -> " + str(round(match, 1)) + "% match")

    # cold-start message
    if scores[0][1] == 0:
        print("\nNo matching skills found.")
        print("Try skills like: python, sql, docker, aws")


main()