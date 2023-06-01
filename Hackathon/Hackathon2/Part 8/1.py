high_scores = [78, 56, 67]
new_score = int(input("Input new score: "))

high_scores.append(new_score)
high_scores.sort(reverse=True)

print("High scores:")
for i, score in enumerate(high_scores, 1):
    print(f"{i}. {score}")
