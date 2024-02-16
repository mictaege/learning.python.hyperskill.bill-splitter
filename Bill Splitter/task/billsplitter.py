# write your code here
import random
number = int(input("Enter the number of friends joining (including you):"))

if number < 1:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0, number):
        friends[input()] = 0
        
    bill = int(input("Enter the total bill value:"))

    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky_feature == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        share = round(bill / (number - 1), 2)
        for friend in friends:
            if friend != lucky_one:
                friends[friend] = share
        print(friends)
    else:
        print("No one is going to be lucky")
        share = round(bill / number, 2)
        for friend in friends:
            friends[friend] = share
        print(friends)

