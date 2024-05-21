class Assassin:
    def __init__(self):
        self.constitution = 10
        self.dexterity = 18
        self.intelligence = 14
        self.strength = 8
        self.wisdom = 8
        self.charisma = 8

    def __str__(self):
        return f"Assassin attributes:\nConstitution: {self.constitution}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nStrength: {self.strength}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"

class Brute:
    def __init__(self):
        self.constitution = 14
        self.dexterity = 12
        self.intelligence = 8
        self.strength = 18
        self.wisdom = 8
        self.charisma = 8

    def __str__(self):
        return f"Brute attributes:\nConstitution: {self.constitution}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nStrength: {self.strength}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"

class Fighter:
    def __init__(self):
        self.constitution = 14
        self.dexterity = 10
        self.intelligence = 6
        self.strength = 16
        self.wisdom = 8
        self.charisma = 4

    def __str__(self):
        return f"Fighter attributes:\nConstitution: {self.constitution}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nStrength: {self.strength}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"

assassin = Assassin()
brute = Brute()
fighter = Fighter()

print(assassin)
print()
print(brute)
print()
print(fighter)

