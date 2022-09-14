# Pokemon Game Project

```python
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type  
        self.max_hp = max_hp
        self.hp = max_hp

    @staticmethod
    def typewheel(type1, type2):
        result_map = {0 : "lose", 1 : "win", -1 : "tie"}
        game_map = {"water": 0, "fire": 1, "grass": 2}

        rps_table = [
            [-1, 1, 0],
            [0, -1, 1],
            [1, 0, -1]
        ]
        result = rps_table[game_map[type1]][game_map[type2]]
        return result_map[result]
    
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"\n{self.name} recovered 1 HP.\n")
        else:
            print(f"\n{self.name} is full.\n")

    def battle(self, other):
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.hp = 0
            print(f"\n{self.name} fainted!\n")
        elif result == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f"\n{self.name} and {other.name} battled hard. It's a tie.\n")
        elif result == 'win':
            other.hp = 0
            print(f"\n{self.name} won. Congratulations!\n")

    def __str__(self):
        return f"{self.name} ({self.primary_type}): {self.hp}/{self.max_hp}"


if __name__ == "__main__":
    bulb = Pokemon('Bulbasaur', 'grass', 120)
    charm = Pokemon('Charmander', 'fire', 110)
    squi = Pokemon('Squirtle', 'water', 115)
    squi.battle(charm)
    
    ```
