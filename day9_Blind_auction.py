import os  # Imports the 'os' module so we can clear the screen later

# Dictionary to store all bids.
# Keys = bidder names, Values = bid amounts
bids = {}

# Controls whether the auction continues asking for bidders
auction_running = True

def clear_screen():
    """
    Clears the terminal screen.
    Works on:
    - Windows (uses 'cls')
    - macOS/Linux (uses 'clear')
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def find_winner(bidding_record):
    """
    Determines the highest bidder.
    Parameters:
        bidding_record (dict): A dictionary of name: bid pairs
    Returns:
        (winner_name, highest_bid)
    """
    highest_bid = 0      # Tracks the highest bid found so far
    winner = ""          # Tracks the name of the highest bidder

    # Loop through each bidder in the dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Get their bid
        if bid_amount > highest_bid:         # Check if it's the highest so far
            highest_bid = bid_amount
            winner = bidder

    return winner, highest_bid

# Main auction loop
while auction_running:
    name = input("Enter your name: ")  # Ask bidder for their name
    bid = int(input("Enter your bid amount: $"))  # Ask for bid and convert to integer

    bids[name] = bid  # Store the bid in the dictionary

    # Ask if more bidders will participate
    more_bidders = input("Are there more bidders? (yes/no): ").lower()

    if more_bidders == "no":
        auction_running = False  # Stop the loop if no more bidders
    else:
        clear_screen()  # Clear screen so next bidder can't see previous bids

# After loop ends, determine the winner
winner, amount = find_winner(bids)

# Display the result
print(f"\nThe winner is {winner} with a bid of ${amount}")