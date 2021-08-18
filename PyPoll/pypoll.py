#imports libaries
import os
import csv

#create variable needed
total_votes = int(0)
poll = {}
csvpath = os.path.join ("/Users/Jared/Desktop/DATA HW/python-challenge/PyPoll/Resources/election_data.csv")


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #Adding vote count
        total_votes += 1
        #Adding votes to poll dict.
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1


print(
    "",
    "Election Results\n",
    "-------------------------\n", 
    "Total Votes:",total_votes, "\n",
    "-------------------------\n",
)
#Calculating and Print Each Canidate's Vote Count
for candidate in poll:
    print(candidate, ":", round(poll[candidate]/total_votes*100, 1), "% (", poll[candidate], ")")
print("-------------------------")
#Calculating and Printing The Winner
for candidate in poll:
    if poll[candidate] >= total_votes/2:
        print("Winner:", candidate)


#Writing to Outside Txt File
with open('election_results.txt', "w") as text:
    text.write("\n")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Values:" + str(total_votes) + "\n")
    text.write("-------------------------\n")
    for candidate in poll:
        text.write(str(candidate) + ":" + str(round(poll[candidate]/total_votes*100 + 1)) + "% (" + str(poll[candidate]) + ")\n")
    text.write("-------------------------\n")
    for candidate in poll:
        if poll[candidate] >= total_votes/2:
           text.write("Winner:" + str(candidate))