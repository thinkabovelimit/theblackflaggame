import random
import sys
balance=0
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
def add_money(bet,balance):
    balance+=bet
    return balance
def sub_money(bet,balance):
    balance=balance-bet
    return balance
def check_balance(bet,balance):
    if balance<bet:
        return False
    else:
        return True
def purchace_coin(balance):
    amt=input("enter the amount")
    balance+=amt
    return balance
def place_bet():
    for i in values:
        print i
    place1=raw_input("hey!!enter your 1st bet")
    place2=raw_input("hey!!enter your 2nd bet")
    place3=raw_input("hey!!enter your 3rd bet")
    return (place1,place2,place3)
def winner(place,bet,balance):
    if place[0] ==random.choice(values.keys()):
        print "you won some money in your 1st bet"
        balance=add_money(bet,balance)
    elif place[1] ==random.choice(values.keys()):
        print "you won some money in your 2nd bet"
        balance=add_money(bet,balance)
    elif place[2] ==random.choice(values.keys()):
        print "you won some money in your 3rd bet"
        balance=add_money(bet,balance)
    else:
        print("sorry you lose your bet amount")
        balance=sub_money(bet,balance)
while True:
    bet=input("place your bet amount")
    while check_balance(bet,balance)==False:
        print("insufficient balance")
        choice1=raw_input("do you want to purchace more y/n")
        if choice1=="yes":
            print"hello"
            balance=purchace_coin(balance)
        elif choice1=="no":
            break
        else:
            continue
    if choice1=="no":
        sys.exit()
    place=place_bet()
    winner(place,bet,balance)
    choice2= raw_input("do you want to continue")
    if choice2=="no":
        sys.exit()
    elif choice2=="yes":
        continue
