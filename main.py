#! python3
# 'python main.py' and then answer the questions.

import portions_classes as pc
from portions_calc import PortionCalculator

# create a bottle, including interested members
bottle = pc.new_bottle()
print("\nBottle Info:")
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
second_column = len(max(pc.MEMBERS, key=len))
for member in bottle.members:
    spaces = second_column - len(member.name)
    if member.cut:
        # bit of cleverness, calc the num spaces between end of name and
        #  the start of the second column, then print a space, 'spaces' times between name and second column
        print(member.name, " "*spaces, "cut")
    else:
        print(member.name, " "*spaces, f"{member.shares} shares")

# do the actual work, now that the inputs are known
calcs = PortionCalculator(bottle)
calcs.pour_shares()  # MUST be called before pour_cuts. These should be wrapped in another method to enforce order
calcs.pour_cuts()
calcs.print_portions_ml()
calcs.print_costs()
