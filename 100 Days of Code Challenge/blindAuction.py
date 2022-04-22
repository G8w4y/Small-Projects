import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#define master list of bidders with bids
biddersAndBids = []

#define function that adds new bidder to master list
def add_bidder(name,bidValue):
    clear()
    bidder = []
    bids = []
    newBidderWithBid = {}
    newBidderWithBid["Bidder"] = str(name)
    newBidderWithBid["Bid"] = int(bidValue)
    #bidder, bids = zip(newBidderWithBid.items())
    #print(bidder)
    #print(f"Your bid is {bids}NOK")
    print(newBidderWithBid)
    print(biddersAndBids)
    biddersAndBids.append(newBidderWithBid)
    print(biddersAndBids)


not_exit = True

while not_exit:

    name = input(f"input your name: ")
    bidValue = input(f"how much would you like to bid?")
    add_bidder(name,bidValue)
    not_finished = input("Type yes to add another bidder, and no to show the end results.\n").lower()
    if "y" in not_finished or "ye" in not_finished or "yes" in not_finished:
        continue
    else:
        not_exit = False

#show the bidder that won
highest_bid = max(biddersAndBids, key=lambda x:x["Bid"])
winning_bidder = highest_bid["Bidder"]
winning_bid = highest_bid["Bid"]
print(highest_bid)
print(winning_bidder)
print(winning_bid)
print(f"{winning_bidder} had the highest bid of {winning_bid} NOK!\n\nOverview of all bids:")
for index in biddersAndBids:
    print(biddersAndBids[index]["Bidder"])




# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# https://www.adamsmith.haus/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python

# def winning_bid():
#     for element in biddersAndBids:

