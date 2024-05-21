
import random

class Player:
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.wisdom = 0
        self.intelligence = 0
        self.constitution = 0
        self.charisma = 0
        self.agility = 0
        self.perception = 0
    def distribute_points_randomly(self, total_points,max_per_attribute):
        attributes = ['strength', 'dexterity', 'wisdom', 'intelligence','constitution', 'charisma', 'agility', 'perception']
        random.shuffle(attributes)
        for attribute in attributes:
            if total_points <= 0:
                break
            
            max_points_for_attribute = min(max_per_attribute, total_points, 20 -getattr(self, attribute))
            points = random.randint(1, max_points_for_attribute)
            setattr(self, attribute, getattr(self, attribute) + points)
            total_points -= points

num_players = 4

players = [Player() for _ in range(num_players)]

print(players)
for player in players:
    player.distribute_points_randomly(64, 20)
    

print("Final attributes for each player:")
print("Player\t\tAttribute\t\tValue")
print("______________________________________________")
for i, player in enumerate(players):
    for attribute in vars(player):
         print(f"Player {i+1}\t{attribute.capitalize()}\t\t{getattr(player,attribute)}")