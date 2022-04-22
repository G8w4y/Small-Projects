biddersAndBids = []

def add_bidder(name,bidValue):
    import os
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
    newBidderWithBid = {}
    newBidderWithBid["Bidder"] = ¨str(name)
    newBidderWithBid["Bid"] = int(bidValue)
    biddersAndBids.append(newBidderWithBid)

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# https://www.adamsmith.haus/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python

def winning_bid():
    for element in biddersAndBids:

