from recommendation import recommend_career
from roadmap import generate_roadmap

print("Enter your skills (comma separated): ")
user_input = input()

user_skills = [skill.strip() for skill in user_input.split(",")]

career = recommend_career(user_skills)

print("\nRecommended Career:", career)

roadmap = generate_roadmap(career)

print("\nYour Learning Roadmap:")
for step in roadmap:
    print("-", step)