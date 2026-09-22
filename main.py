from art import logo


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of £{highest_bid}")


print(logo)
bids ={}
continue_bidding = True
while continue_bidding is True:
    name = input("Please tell me your name:  ")
    price = int(input("Please enter your bid: £"))
    bids[name] = price

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()


    if another_bidder == "no":
        continue_bidding = False
        find_highest_bidder(bids)

    elif continue_bidding == "yes":
            print("\n"*20)




            