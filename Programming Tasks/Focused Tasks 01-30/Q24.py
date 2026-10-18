'''24. Score analyzer (list operations)
Collect a chosen number of quiz scores into a list. Report the scores, count, minimum, maximum, total, and average.
Do not use min/max until the basic version has found them with a loop.
Extension: Sort a copy of the list and display the median.'''

scores = []
n = int(input("How many scores? "))

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)

if n > 0:
    total = 0
    minimum = scores[0]
    maximum = scores[0]

    for score in scores:
        total += score

        if score < minimum:
            minimum = score

        if score > maximum:
            maximum = score

    average = total / n

    print("Scores:", scores)
    print("Count:", n)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Total:", total)
    print("Average:", average)

    sorted_scores = sorted(scores)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    print("Median:", median)
else:
    print("Enter at least one score")