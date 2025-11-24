import random

def calc_classical_prob(fav_count, total_count):
    return fav_count / total_count

def calc_empirical_prob(results, condition_fn):
    # Prevent division by zero in case trials = 0.
    if len(results) == 0:
        return 0  

    # Count how many results satisfy the event condition.
    matches = sum(1 for r in results if condition_fn(r))
    return matches / len(results)

def roll_die_wt(weights):
    total_wt = sum(weights)
    roll_point = random.randint(1, total_wt)

    current_wt = 0

    # Walk through cumulative weights until passing the roll point.
    for i, wt in enumerate(weights):
        current_wt += wt
        if roll_point <= current_wt:
            return i + 1  # convert index to face number.

    return -1  # fallback (should never happen).

# Main Program
sides = int(input("Enter number of sides on the die: "))
event = input("Enter event ('even', 'odd', or 'custom'): ").lower()
trials = int(input("Enter number of trials for simulation: "))

weights = []
print(f"\nEnter weights for each face (1 to {sides}):")

for i in range(sides):
    w = int(input(f"Weight for face {i + 1}: "))
    weights.append(w)

# Classical Probability
if event == "even":
    fav_count = sides // 2
elif event == "odd":
    fav_count = sides - (sides // 2)
else:
    fav_count = int(input("Enter number of favorable outcomes: "))

classical_p = calc_classical_prob(fav_count, sides)
print(f"\nClassical P({event}) on d{sides} =", classical_p)

# Empirical Probability
results = [roll_die_wt(weights) for _ in range(trials)]

if event == "even":
    condition_fn = lambda x: x % 2 == 0
elif event == "odd":
    condition_fn = lambda x: x % 2 != 0
else:
    # Validate custom face input
    while True:
        custom_face = int(input("Enter the specific face number for the custom event: "))
        if 1 <= custom_face <= sides:
            break
        print(f"Invalid! Enter a number between 1 and {sides}.")
    condition_fn = lambda x: x == custom_face

empirical_p = calc_empirical_prob(results, condition_fn)

print(f"Empirical P({event}) from simulation ≈ {empirical_p}")