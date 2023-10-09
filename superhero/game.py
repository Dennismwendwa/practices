from random import randint

class Characters:
    def __init__(self, name, power, life):
        self.name = name
        self.power = power
        self.life = life

    def __str__ (self):
        return f"{self.name} - {self.power} - {self.life}"

class Superhero(Characters):
    superhero_list = []
    def __init__ (self, name, power, life, movie):
        super().__init__(name, power, life)
        self.movie = movie

    @classmethod
    def create_superhero(cls, name, power, life, movie):
        superheros = cls(name, power, life, movie)
        cls.superhero_list.append(superheros)
        return superheros

    def __str__(self):
        return f"{self.name} {self.power} {self.life}"


class Villain(Characters):
    villian_list = []

    def __init__ (self, name, power, life, village):
        super().__init__(name, power, life)
        self.village = village

    @classmethod
    def create_villain(cls, name, power, life, village):
        villians = cls(name, power, life, village)
        cls.villian_list.append(villians)
        return villians

    def __str__(self):
        return f"{self.name} {self.power} {self.life} {self.village}"

Batman = Superhero.create_superhero("Batman", 400, 200, "movi1")
Ironman = Superhero.create_superhero("Ironman", 250, 300, "movi1")
Blackwidow = Superhero.create_superhero("Blackwidow", 700, 150, "movi2")
Spiderman = Superhero.create_superhero("Spiderman", 350, 250, "movie2")
Flash    = Superhero.create_superhero("Flash", 200, 270, "movie3")

Thanos = Villain.create_villain("Thanos", 1500, 700, "kruger")
Hulk = Villain.create_villain("Hulk", 1400, 550, "kruger")
Tick = Villain.create_villain("Tick", 1200, 600, "kruger")
Spawn = Villain.create_villain("Spawn", 1600, 800, "kruger")


