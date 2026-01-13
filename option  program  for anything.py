def highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    amount = int(input("Enter your bid amount: "))
    bids[name] = amount
    should_continue = input("Do you want to continue (y/n)? ").lower()
    if should_continue == "n":
        continue_bidding = False
        highest_bidder(bids)
    elif should_continue == "y":
        print("\n" * 20)
