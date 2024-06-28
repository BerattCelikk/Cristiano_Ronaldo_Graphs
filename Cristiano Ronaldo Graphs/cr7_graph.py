import matplotlib.pyplot as plt

score_types = ["Inside the Penalty Area", "Penalty Goal", "Free Kick Goal", "Outside the Penalty", "Head Goal", "Assist"]
amount_of_scores = [502, 163, 59, 98, 145, 252]
colors1 = ["orange", "g", "y", "r", "pink", "purple"]

match_types = ["Won", "Lost", "Draw"]
amount_of_matches = [963, 238, 164]
colors2 = ["g", "r", "y"]

fig,(ax1, ax2) = plt.subplots(1, 2,figsize=(14, 7))

ax1.pie(amount_of_scores, labels=[f"{score_types[i]} ({amount_of_scores[i]})" for i in range(len(score_types))], colors=colors1, autopct="%1.1f%%", startangle=90)
ax1.set_title("Score Types and Amounts")

ax2.pie(amount_of_matches, labels=[f"{match_types[i]} ({amount_of_matches[i]})" for i in range(len(match_types))], colors=colors2, autopct="%1.1f%%", startangle=90)
ax2.set_title("Total Matches (All Season)")

plt.tight_layout()
plt.show()
