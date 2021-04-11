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
members_who_want_shares = [n for n in bottle.members if n.shares]  # list of members
shares = [n.shares for n in bottle.members if n.shares]  # list of share request values
shares = list(set(shares))  # a very non-intuitive way to eliminate duplicate values
shares.sort()
print(shares)

still_thirsty = set(list(bottle.members))
shares_given = 0
for share in shares:
    share = share - shares_given  # if someone wanted 3 shares, but had already been given 1, then give 2 more
    filled_up = set()  # a set of members whose wants were satisfied in this round of pours
    portion = 0
    # portion out 'share' number of shares to everyone who hasn't gotten all of their requested booze
    if bottle.amount_unclaimed >= (share * bottle.share_size * len(still_thirsty)):
        portion = (share * bottle.share_size)
    else:
        portion = (bottle.amount_unclaimed/len(still_thirsty))
    for member in still_thirsty:
        if (share <= member.shares) or member.cut:
            member.portion += portion
            bottle.amount_unclaimed -= portion
            member.shares -= share  # keep track of how many shares the member still wants
        if member.shares == 0:  # note that 'cut' people will have negative shares at this point
            filled_up.add(member)
    shares_given += share  # keep track of how many we've doled out (per round)
    still_thirsty -= filled_up
    if bottle.amount_unclaimed < bottle.share_size:
        break

# We've either satisfied all of the share requests, or there is no more booze left
# give the rest of the booze to the members who wanted a cut (if there's any left)
if bottle.amount_unclaimed:
    members_who_want_cuts = [n for n in bottle.members if n.cut]
    number_of_cuts = len(members_who_want_cuts)
    portion = bottle.amount_unclaimed/number_of_cuts
    for member in members_who_want_cuts:
        member.portion += portion

print(f"\n{bottle.winner} gets {int(bottle.winners_cut)}ml")
for member in bottle.members:
    print(f"{member.name} gets {int(member.portion)}ml")


# ##########################Cost Calculator#########################
cost_per_ml = bottle.price / (bottle.volume - bottle.winners_cut)
for member in bottle.members:
    member.owes = member.portion * cost_per_ml

print()
for member in bottle.members:
    print(f"{member.name} owes ${member.owes:.2f}")

