#Time:        44     89     96     91
#Distance:   277   1136   1890   1768

races = [[44, 277], [89, 1136], [96, 1890], [91, 1768], [44899691, 277113618901768]]
winning_counts = []

for race in races:
    winning_results = []

    for i in range(0, race[0] + 1):
        distance = i * (race[0] - i)
        if distance > race[1]:
            win_until = race[0] - i
            winning_counts.append(win_until - i + 1)
            break

print(winning_counts)

total = 1
for win in winning_counts[:-1]:
    total = total * win
print(total)
