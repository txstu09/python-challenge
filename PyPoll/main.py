import os
import csv

csvpath = os.path.join('raw_data','election_data_2.csv')

candidates = []
vote_count = {}
row_count = 0
percents = []

with open(csvpath, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for line in election_data:
        row_count = row_count + 1
        if line[2] not in candidates:
            candidates.append(line[2])
            vote_count[line[2]] = 1
        else:
            vote_count[line[2]] = vote_count[line[2]] + 1
        
for x in range(len(candidates)):
    percents.append(round((vote_count[candidates[x]]/row_count)*100))

win_value = max(percents)
win_index = percents.index(win_value)

winner = candidates[win_index]


print("ELECTION RESULTS")
print("-----------------------")
print("Total Votes: " + str(row_count))
print("-----------------------")
for y in range(len(candidates)):
    print(f"{candidates[y]}: {percents[y]}% ({vote_count[candidates[y]]})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")