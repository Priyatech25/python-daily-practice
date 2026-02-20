# IPL Mini Data Analysis Project

# Sample IPL match data
matches = [
    {"team1": "CSK", "team2": "MI", "winner": "CSK", "runs": 180},
    {"team1": "RCB", "team2": "CSK", "winner": "RCB", "runs": 200},
    {"team1": "MI", "team2": "RCB", "winner": "MI", "runs": 150},
    {"team1": "CSK", "team2": "RCB", "winner": "CSK", "runs": 170},
    {"team1": "MI", "team2": "CSK", "winner": "MI", "runs": 190}
]

# Total matches
total_matches = len(matches)

# Count wins
win_count = {}

for match in matches:
    winner = match["winner"]
    if winner in win_count:
        win_count[winner] += 1
    else:
        win_count[winner] = 1

# Find most winning team
most_wins = max(win_count, key=win_count.get)

# Calculate total runs
total_runs = 0
for match in matches:
    total_runs += match["runs"]

# Display Results
print("IPL MINI ANALYSIS")
print("------------------")
print("Total Matches:", total_matches)
print("Win Count:", win_count)
print("Most Successful Team:", most_wins)
print("Total Runs Scored:", total_runs)

print("Thank you for using IPL Analyzer!")

# User input feature
team_name = input("Enter team name to check wins: ")
print("Wins:", win_count.get(team_name, 0))