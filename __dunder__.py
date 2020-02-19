class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt2 = sodium + chlorine
print(salt)
print(salt2)


class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        if lawyer in self.lawyers:
            return True


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
