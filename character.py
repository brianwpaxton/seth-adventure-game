class Character:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.original_hp = hp
        self.hp = hp
        self.attacks = attacks

    def __str__(self):
        return self.name

    def reset_hp(self):
        self.hp = self.original_hp
