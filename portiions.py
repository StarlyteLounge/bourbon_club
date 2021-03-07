# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:20:29 2021

@author: mmcginnes
"""
# pythonic names: name, shares_wanted getting_shares  (snake case).
# as an aside, you have used camel case (SharesWanted) AND pascal case (Getting_shares)!

# create members dict  # where's Ruth?
members = {'Michael McG': {'Name': 'Michael McG', 'SharesWanted': 600, 'Getting_shares': 0},
 'Jon McC': {'Name': 'Jon McC', 'SharesWanted': 600, 'Getting_shares': 0},
 'Mike B': {'Name': 'Mike B', 'SharesWanted': 600, 'Getting_shares': 0},
 'Jay': {'Name': 'Jay', 'SharesWanted': 600, 'Getting_shares': 0},
 'Katie': {'Name': 'Katie', 'SharesWanted': 600, 'Getting_shares': 0},
 'Barbara': {'Name': 'Barbara', 'SharesWanted': 600, 'Getting_shares': 0},
 'John N': {'Name': 'John N', 'SharesWanted': 120, 'Getting_shares': 0},
 'Jim': {'Name': 'Jim', 'SharesWanted': 60, 'Getting_shares': 0}}

# member literals (hard-coded values) in more than one place can introduce errors.
# a better way might be to populate memberlist from members
memberlist = [name for name in members]  # member_list

members = {}

for name in memberlist:
    while True:
        choice = input(f"Does {name} want a cut, x shares, or are they out (cut,share,out)? ")
        if choice.lower().strip() not in ["cut", "share", "out"]:
            print('please enter "cut", "share", or "out"')
            continue
        elif choice.lower().strip() == "out":
            mlWanted = 0
            break
        elif choice.lower().strip() == "cut":
            mlWanted = 600
            break
        elif choice.lower().strip() == "share":
            while True:
                shares = input("How many 60ml shares would you like?")
                try:  # a more 'pythonic' name might be ml_wanted:
                    mlWanted = min(abs(int(shares)) * 60, 600)  # why abs()? Input validation should be done above..
                    choice = shares + choice
                    break
                except Exception as err:  # using a blanket 'except' is bad form.....
                    print(err)
                    print("A whole number, please")
                    continue
            break
    members[name] = ({"Name": name,
                      "Choice": choice,
                      "SharesWanted": mlWanted,  # mlWanted is actually out-of-scope here, but python is forgiving....
                      "Getting_shares": 0})

sharesavailable = 600
units = 1 / 1024  # you must have a very precise scale!!!!

'''           
I'm going to choose to use my time for something other than figuring out 
how to figure out how many people are left wanting more when there is less
than 60ml left for each of them.
'''

while sharesavailable > .001:
    try:
        #    print(sharesavailable)

        for member in members:
            if member.get("SharesWanted") >= units:
                member.update({"SharesWanted": member.get("SharesWanted") - units})
                member.update({"Getting_shares": member.get("Getting_shares") + units})
                sharesavailable -= units
        #       pprint.pprint (members)
        #       print (sharesavailable)
        if sharesavailable <= 0.01:
            raise ValueError  # "You gave away more shares than you have"
    except ValueError:  # very good, I would have used a custom error here
        print(f'{sharesavailable} ml left over')

for member in members.values():
    print(f' {member["Name"]} gets {member["Getting_shares"]} ml')
