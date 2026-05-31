import csv

def load_data(filename):
    roles = []
    role_skills = []

    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            roles.append(row[0])
            skills = row[1].lower().split(",")
            role_skills.append(skills)
    return roles, role_skills

def build_vocab(role_skills):
    vocab = []
    for skills in role_skills:
        for skill in skills:
            if skill not in vocab:
                vocab.append(skill)
    return vocab

roles, role_skills = load_data("raw_skills.csv")
print(roles)
print(role_skills)

vocab = build_vocab(role_skills)
print(vocab)