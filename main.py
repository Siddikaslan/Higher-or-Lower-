from shape import shape, vs
from game_data import data
import random

def most_popular_person(first_person, second_person):
    return first_person if first_person['follower_count'] > second_person['follower_count'] else second_person

def format_person(person, label):
    return f"{label}: {person['name']}, {person['description']}, from {person['country']}"

print(shape)
score = 0
game_continue = True


person_a = random.choice(data)

while game_continue:
    person_b = random.choice(data)
    while person_b == person_a:
        person_b = random.choice(data)

    print(f"\n{format_person(person_a, 'Compare A')}")
    print(vs)
    print(f"{format_person(person_b, 'Against B')}")

    vote = input("Who has more followers? Type 'A' or 'B': ").upper()
    correct_answer = 'A' if person_a['follower_count'] > person_b['follower_count'] else 'B'

    if vote == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        person_a = person_a if correct_answer == 'A' else person_b
    else:
        print("\n" * 10)
        print(shape)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
