"""Classes and Main for calculating bourbon portions"""

#  Bottles have members
#  Members have booze

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
    """
    Someone who is getting some booze from a particular bottle.
    'some' is 'none' by default
    """
    def __init__(self, name, cut=False, shares=0, portion=0):
        self.name = name
        self.cut = cut
        """as much of the bottle as they can get"""
        self.shares = shares
        """1/10th of the amt of booze to be shared, usually 60ml per share"""
        self.portion = portion
        """the amount of booze this Member actually gets"""
        self.owes = 0


class Bottle:
    """The interesting bottle of booze. Duh."""
    def __init__(self, name, winner, price, volume=750):
        self.name = name
        self.winner = winner
        self.price = price
        self.volume = volume
        self.members = []
        self.winners_cut = min(volume/5, 150)
        self.amount_unclaimed = volume - self.winners_cut
        self.share_size = self.amount_unclaimed/10

    def i_am_in(self, name):
        """add a Member if 'name' wants some booze"""
        while True:
            choice = input(f"\nDoes {name} want to share, a cut, or are they out? ").lower().strip()
            if choice == '':  # this Member does not want any of this booze
                return
            if choice not in ["c", "s", "o", "cut", "share", "out"]:
                print('please enter cut or c, share or s, or out or o\n')
                continue
            elif choice.startswith("c"):
                self.members.append(Member(name, cut=True))
                break
            elif choice.startswith("s"):
                while True:
                    shares = int(input(f"How many {self.share_size}ml shares does {name} want? "))
                    if shares < 1 or shares > 9:
                        print(f"{shares} is not a valid number. Choose from 1 to 9.")
                        continue
                    break  # end of choice.startswith("s") loop
                self.members.append(Member(name, shares=shares))
                break  # user input 'share' with a valid number of shares
            break  # user input a valid choice for this member
        return


def new_bottle():
    """the bottle of booze to be divided up"""
    while True:
        name = input("What's the name of the bottle? ")
        price = input("What's the total price? ")

        volume = ''
        volume_input = input("If it's a 750ml bottle, hit enter, otherwise input the bottle volume: ")
        for c in volume_input:  # strip any units at the end of the number
            if c.isdigit() or c == ".":
                volume += c
        volume = float(volume or "750")
        if volume < 10:
            volume = volume * 1000  # convert liters into milliliters

        print("Current Member list:\n" + '\n'.join(MEMBERS))
        while True:
            winner = input("Who is the winner? ")
            if winner in MEMBERS:
                break
            else:
                print(f"{winner} is not in the list. Try again.")
                print("Spelling and capitalization counts!")
                print("ctl-c to quit")
                continue

        return Bottle(name, winner, price, int(volume))
