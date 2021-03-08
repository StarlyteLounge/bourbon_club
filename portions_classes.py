"""Classes and Main for calculating bourbon portions"""

MEMBERS = \
    ['Michael McG',
    'Jon McC',
    'Mike B',
    'Jay',
    'Katie',
    'Barbara',
    'John N',
    'Jim']


class Member:
    def __init__(self, name, cut=False, shares=0, allocated=0):
        self.name = name
        self.cut = cut
        self.shares = shares
        self.allocated = allocated


class Bottle:
    def __init__(self, name, winner, price, volume=750):
        self.name = name
        self.winner = winner
        self.price = price
        self.volume = volume
        self.members = []
        self.winners_cut = min(volume/5, 150)
        self.amount_unclaimed = volume - self.winners_cut

    def whos_in(self, name):
        """adds a Member object if 'name' wants some booze"""
        while True:
            choice = input(f"Does {name} want to share, a cut, or are they out (cut,share,out)? ").lower().strip()
            if choice == '':  # bail on 'name' if user hits enter w/o any input
                return
            if choice not in ["cut", "share", "out"]:
                print('please enter "cut", "share", or "out"')
                continue
            elif choice == "cut":
                self.members.append(Member(name, cut=True))
                break
            elif choice == "share":
                while True:
                    shares = int(input(f"How many {self.amount_unclaimed/10}ml shares would you like? "))
                    if shares < 1 or shares > 9:
                        print(f"{shares} is not a valid number. Choose from 1 to 9.")
                        continue
                    break
                self.members.append(Member(name, shares=shares))
                break
            break
        return
#OIC
def new_bottle():
    while True:
        name = input("What's the name of the bottle? ")
        price = input("What's the total price? ")
        while True:
            winner = input("Who is the winner? ")
            if winner in MEMBERS:
                break
            else:
                print(f"{winner} is not in the list. Our current members are:")
                print(MEMBERS)
                print("Spelling counts!")

        volume_input = input("If it's a 750ml bottle, hit enter, otherwise input the bottle volume: ")
        volume = int(volume_input or "750")
        return Bottle(name, winner, price, volume)


bottle = new_bottle()
print(bottle.name)
print(bottle.price)
print(bottle.volume)
print(bottle.members)
print(bottle.winner)

for person in MEMBERS:
    bottle.whos_in(person)

for i in bottle.members:
    print(i.name)
