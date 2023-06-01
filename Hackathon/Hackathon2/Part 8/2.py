high_scores = [78, 70, 67, 56, 45]
new_score = int(input("Input new score: "))
high_scores.append(new_score)
sorted_scores = sorted(high_scores, reverse=True)

print("High scores:")
for i, score in enumerate(sorted_scores[:5], start=1):
    print(f"{i}. {score}")
