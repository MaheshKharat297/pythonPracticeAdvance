def bidder_info(name, bid_amt):
    bidders_dic = {}
    bidders_dic[name] = bid_amt
    return bidders_dic

def find_winner(bidders_dic):
    bidders_name = bidders_dic.keys()
    bidders_bid = bidders_dic.values()
    min_amt = min(bidders_bid)
    for name in bidders_name:
        if bidders_dic[name] == min_amt:
            winner = name
    return winner

def ask_bidder_info():
    name = input("Enter name of the bidder :")
    bid_amt = int(input("Enter bid amt : "))
    bidders_dic = bidder_info(name, bid_amt)
    return bidders_dic

if __name__ == "__main__":
    bidders_dic = {}
    flag = True
    while flag == True:
        bidders_dic = ask_bidder_info()
        ans = input("Are there any other bidders Yes/No:")

        if ans == "Yes":
            flag = True
        elif ans == "No":
            print("Thank you !")
            flag = False
        else:
            print("Invalid input !")

    winner = find_winner(bidders_dic)
    print(f"The winner is : {winner}")