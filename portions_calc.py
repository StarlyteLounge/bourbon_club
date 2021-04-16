# ############################ Portion Calculator ###########################
# order shares, ascending
# for each share, distribute that many shares among participating members
# if sum of shares is more than available
#   then divide available by the number of participating members and distribute
# if there is any booze left, then divide available by the number of participating members and distribute
class PortionCalculator:
    """Utility that calculates the portions and charges for every member of a bottle"""
    def __init__(self, bottle):
        self.bottle = bottle
        self.members_who_want_shares = [n for n in bottle.members if n.shares]  # list of members
        shares = [n.shares for n in bottle.members if n.shares]  # list of share request values
        self.shares = list(set(shares))  # a very non-intuitive way to eliminate duplicate values
        self.shares.sort()

    def pour_shares(self):
        """Allocate shares to members who want shares, and to members who want cuts"""
        still_thirsty = set(list(self.bottle.members))
        """list of members who haven't gotten their pour of shares"""
        shares_given = 0
        for share in self.shares:
            share = share - shares_given  # if someone wanted 3 shares, but had already been given 1, then give 2 more
            filled_up = set()  # a set of members whose wants were satisfied in this round of pours
            portion = 0
            # portion out 'share' number of shares to everyone who hasn't gotten all of their requested booze
            if self.bottle.amount_unclaimed >= (share * self.bottle.share_size * len(still_thirsty)):
                portion = (share * self.bottle.share_size)
            else:
                portion = (self.bottle.amount_unclaimed/len(still_thirsty))
            for drinker in still_thirsty:
                if (share <= drinker.shares) or drinker.cut:
                    # pour a portion out of the bottle and into the drinker's cup
                    self.bottle.amount_unclaimed -= portion
                    drinker.portion += portion
                    drinker.shares -= share  # keep track of how many shares the drinkers still wants
                if drinker.shares == 0:  # note that 'cut' people will have negative shares at this point
                    filled_up.add(drinker)
            shares_given += share  # keep track of how many we've doled out (per round)
            still_thirsty -= filled_up
            if self.bottle.amount_unclaimed < self.bottle.share_size:
                break

    def pour_cuts(self):
        """Divide the rest of the bottle among the people who want cuts"""
        if self.bottle.amount_unclaimed:  # doling out the shares may have emptied the bottle
            members_who_want_cuts = [n for n in self.bottle.members if n.cut]
            number_of_cuts = len(members_who_want_cuts)
            portion = self.bottle.amount_unclaimed/number_of_cuts
            for drinker in members_who_want_cuts:
                drinker.portion += portion

    def print_portions_ml(self):
        print(f"\n{self.bottle.winner} gets {int(self.bottle.winners_cut)}ml")
        for drinker in self.bottle.members:
            print(f"{drinker.name} gets {int(drinker.portion)}ml")

    def print_costs(self):
        cost_per_ml = self.bottle.price / (self.bottle.volume - self.bottle.winners_cut)
        for member in self.bottle.members:
            member.owes = member.portion * cost_per_ml
