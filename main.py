#! python3

import portions_classes as pc

bottle = pc.new_bottle()
print()
print("Bottle Info:")
print(f"Name: {bottle.name}")
print(f"Winner: {bottle.winner}")
print(f"Price: ${bottle.price}")
if bottle.volume >= 1000:
    print(f"{bottle.volume/1000}l")
else:
    print(f"Size: {bottle.volume}ml")

print("\nJust hit 'Enter' if the member is 'out'")
for person in pc.MEMBERS:
    bottle.i_am_in(person)

print(f"\nThere are {len(bottle.members)} participating members:")
# print names and choices in a table format
first_tab = len(max(pc.MEMBERS, key=len))
for member in bottle.members:
    spaces = first_tab - len(member.name)
    if member.cut:
        # bit of cleverness, calc the num spaces between end of name and
        #  the rest of the sentence, then print a space, 'spaces' times
        print(member.name, " "*spaces, "cut")
    else:
        print(member.name, " "*spaces, f"{member.shares} shares")

# ############################ Portion Calculator ###########################
# order shares, ascending
# for each share, distribute that many shares among participating members
# if sum of shares is more than available
#   then divide available by the number of participating members and distribute
# if there is any booze left, then divide available by the number of participating members and distribute
sharers = [n for n in bottle.members if n.shares]  # list of members
shares = [n.shares for n in bottle.members if n.shares]  # list of share request values
shares = list(set(shares))  # a very non-intuitive way to eliminate duplicate values
shares.sort()
print(shares)

for share in shares:
    # portion out 'share' number of shares to everyone who hasn't gotten all of their requested booze
    if bottle.amount_unclaimed > (share * bottle.share_size):
        portion += (share * bottle.share_size)
    else:
        portion = (bottle.amount_unclaimed/len(bottle.members))
    for member in bottle.members:
        member.portion += portion
    if bottle.amount_unclaimed < bottle.share_size:
        break

if bottle.amount_unclaimed:

