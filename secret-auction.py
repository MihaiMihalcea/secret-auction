import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidders = {}
more_bidders = True
highest_bid = 0

while more_bidders == True:
    name = input("Please state your name: ")
    bid_amount = int(input("Please state your bid amount: "))
    bidders[name] = bid_amount
    more_bids = input("Are there more bidders? Y/N: ")
    if more_bids == "Y":
        clearConsole()
    else:
        more_bidders = False
        clearConsole()

for name, value in bidders.items():
    if value > highest_bid:
        highest_bid = value
        highest_bidder = name

print(f"The winner of the auction is {highest_bidder} with a total bid amount of ${highest_bid}")
