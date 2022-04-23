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

    print(newBidderWithBid)
    #print(biddersAndBids)
    biddersAndBids.append(newBidderWithBid)
    #print(biddersAndBids)


not_exit = True

while not_exit:

    name = input(f"input your name: ")
    bidValue = input(f"how much would you like to bid?")
    add_bidder(name,bidValue)
    not_finished = input("Type yes to add another bidder, and no to show the end results.\n").lower()
    if "y" in not_finished or "ye" in not_finished or "yes" in not_finished:
        clear()
        continue
    else:
        not_exit = False

#show the bidder that won
highest_bid = max(biddersAndBids, key=lambda x:x["Bid"])
winning_bidder = highest_bid["Bidder"]
winning_bid = highest_bid["Bid"]
## For testing
#print(highest_bid)
#print(winning_bidder)
#print(winning_bid)
clear()
print("####################################################################")
print(f"{winning_bidder} had the highest bid of {winning_bid},- NOK!\n\nOverview of all bids in descending order:")


# Tester ut om vi kan sortere listen fra høyeste til laveste bud, slik at den blir penere å se på for folk
biddersAndBids = sorted(biddersAndBids, key=lambda d: d["Bid"], reverse=True)
### Koden under gjør det samme som koden over men vha et annet bibliotek.
#from operator import itemgetter
#biddersAndBids = sorted(biddersAndBids, key=itemgetter('Bid'), reverse=True)

# Går igjennom hvert element i listen og printer listeplassen +1, deretter henter ut Key:value parene ved hver posisjon i dictionariene
# Hver dictionary printes ut ut, før programmet hopper videre til neste element i listen og gjør det samme
# Dette foregår frem til listens slutt
for i, list_item in enumerate(biddersAndBids):
    print(f"{i + 1}. ", end='')
    for j, key in enumerate(list_item.keys()):
        print(f"{key}:{list_item[key]}{'' if j == len(list_item) - 1 else ', '}", end='')
        #print("")
    print("")
print("####################################################################")

#{key}:{list_item[key]}
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# https://www.adamsmith.haus/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python

# def winning_bid():
#     for element in biddersAndBids:

