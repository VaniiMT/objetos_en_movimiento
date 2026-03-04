import time
class Human:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.strength = self.assign_strength()
        self.alive = True

    def assign_strength(self):
        return int(time.time() * 1000) % 10 + 1 #Fuerza random casera

    def move(self):
        direction = int(time.time() * 1000) % 2  
        speed = int(time.time() * 1000) % 5 + 1
        #Make movement more random by also changing direction randomly (positive or negative)
        if direction == 0:
            self.x += speed if int(time.time() * 100) % 2 == 0 else -speed
        else:
            self.y += speed if int(time.time() * 100) % 2 == 0 else -speed
        #Mostrar movimiento de cada humano
        while self.alive:
            print(f"{self.name} moves to ({self.x}, {self.y}) with strength {self.strength}")
            time.sleep(0.5)
            break

    def fight(self, other):
        if self.strength > other.strength:
            print(f"{self.name} wins against {other.name}")
            return self
        elif self.strength < other.strength:
            print(f"{other.name} wins against {self.name}")
            return other
        else:
            print(f"{self.name} and {other.name} both die")
            return None
    def is_at_same_location(self, other):
        return self.x == other.x and self.y == other.y
    def limit_position(self):
        self.x = max(0, min(15, self.x))
        self.y = max(0, min(15, self.y))
    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y}) with strength {self.strength}"
#Generar humanos
def generate_humans(num_humans):
    humans = []
    for i in range(num_humans):
        human = Human(f"Human_{i}")
        while any(h.is_at_same_location(human) for h in humans):
            human.move()  
            human.limit_position()  #Dentro del limite del arena
        humans.append(human)
    return humans
#Core de la simulacion
def main():
    num_humans = 5
    humans = generate_humans(num_humans)
    while len(humans) > 1:
        for human in humans:
            human.move()
            human.limit_position()
        for i in range(len(humans)):
            for j in range(i + 1, len(humans)):
                if humans[i].is_at_same_location(humans[j]):
                    winner = humans[i].fight(humans[j])
                    if winner is None:
                        humans.pop(j)  # Both die
                        humans.pop(i)
                    elif winner == humans[i]:
                        humans.pop(j)  
                    else:
                        humans.pop(i)  
                    break
    if humans:
        print(f"The last remaining human is: {humans[0]}")
        exit()
#Ejecutar la simulacion
if __name__ == "__main__":
    main()