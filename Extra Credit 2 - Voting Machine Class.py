from classVotingMachine import VotingMachine

def main():

    vote = VotingMachine()
    
    vote.clear()
    vote.voteDemocrat()
    vote.voteDemocrat()
    vote.voteRepublican()
    vote.voteDemocrat()
    vote.voteRepublican()
    vote.voteDemocrat()
    vote.voteRepublican()

    print("Democrats: ",vote.getTalliesD())
    print("Republicans: ",vote.getTalliesR())

main()
