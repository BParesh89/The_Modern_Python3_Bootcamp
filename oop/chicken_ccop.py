class Chicken:

    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


# testing
c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
assert(Chicken.total_eggs == 0)
assert(c1.lay_egg() == 1)
assert(Chicken.total_eggs == 1)
assert(c2.lay_egg() == 1)
assert(c2.lay_egg() == 2)
assert(Chicken.total_eggs == 3)
