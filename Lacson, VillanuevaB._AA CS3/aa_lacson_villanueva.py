class Plant:
    def __init__ (self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack (self, zombie):
        print (f"{self.name} attacks {zombie.name} with {self.damage} damage.")
        
    def take_damage(self, amount):
        if self.health > 0:
            self.health -= amount 
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage. (Health: {self.health})")
     
class Zombie:
    def __init__ (self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
          if self.distance > 0:
              self.distance -= 1 
          print(f"{self.name} moves towards the plants. (Distance: {self.distance})")

    def attack (self, plant):
        print(f"{self.name} attacks {plant.name} with {self.damage}.")
        plant.take_damage(plant.damage)
        
def take_damage(self, amount):
    if self.health > 0:
        self.health -= amount 
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage. (Health: {self.health})")
    

def run_game():
    plant1 = Plant("Charles_Cabbage", 100, 15)
    plant2 = Plant("Peter Peashooter", 100, 35)

    zombie = Zombie("Barney", 100, 50, 2)

    turn = 1

    while True:
        print(f"Turn {turn}")

        if plant1.health > 0:
            target = plant1
        elif plant2.health > 0:
            target = plant2
        else:
            target = None

        if zombie.health == 0:
            print(f"{zombie.name} was defeated!")
            return

        if plant2.health > 0:
            plant2.attack(zombie)

        if zombie.health == 0:
            print("The plants saved the day!")
            return

        if zombie.distance > 0:
            zombie.move()
        else:
            zombie.attack(target)

        if plant1.health == 0 and plant2.health == 0:
            print("Both plants were eliminated. Zombie rules! >:)")
            return

    turn += 1

if __name__ == "__main__":
    run_game()
