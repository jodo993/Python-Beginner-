# This program counts the number of votes for Democrats and Republicans
# Import class
from classVotingMachine import VotingMachine

def main():

    vote = VotingMachine()

    # Apply one vote per call
    vote.clear()
    vote.voteDemocrat()
    vote.voteDemocrat()
    vote.voteRepublican()
    vote.voteDemocrat()
    vote.voteRepublican()
    vote.voteDemocrat()
    vote.voteRepublican()

    # Display result
    print("Democrats: ",vote.getTalliesD())
    print("Republicans: ",vote.getTalliesR())

# Start program
main()
