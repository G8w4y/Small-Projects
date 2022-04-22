import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

biddersAndBids = []

def add_bidder(name,bidValue):
    clear()
    bidder = []
    bids = []
    newBidderWithBid = {}
    newBidderWithBid["Bidder"] = str(name)
    newBidderWithBid["Bid"] = int(bidValue)
    bidder, bids = zip(newBidderWithBid.items())
    print(bidder)
    print(f"Your bid is {bids}NOK")

name = input(f"input your name: ")
bidValue = input(f"you much would you like to bid?")
add_bidder(name,bidValue)


# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# https://www.adamsmith.haus/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python

# def winning_bid():
#     for element in biddersAndBids:

