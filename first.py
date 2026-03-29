import random

subjects = [
    "Nilay sinha",
    "Aryan",
    "Anand",
    "Harsh",
    "Rishi",
    "a mumbai cat",
    "a man who killed his wife",
    "shah rukh khan",
    "nirmala sitharaman",
    "Virat kohli",
    "Prime minister Modi"
]

actions = [
    "launches",
    "rides",
    "drinks",
    "saw",
    "jumps",
    "cancels",
    "dances",
    "eats",
    "declares a war",
    "orders",
    "celebrates"
]

places_or_things= [
    "at red fort",
    "in mumbai",
    "his watch",
    "buffalo",
    "mercury",
    "ripe orange juice",
    "wax",
    "fresh lemon",
    "on moon",
    "in pakistan",
    "for heaven",  
    "ipl win"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    answer = input("\nDo You Want Another Headline? (yes/no) ").strip().lower()
    if answer == "no":
        print("Thank you for using the headline generator!")
        break