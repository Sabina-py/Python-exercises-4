import random

N = int(input("How many random points to generate for Pi estimation? "))
count_inside = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        count_inside += 1
    i += 1

pi_approx = 4 * count_inside / N
print(f"Approximate value of Pi using {N} points: {pi_approx}")
