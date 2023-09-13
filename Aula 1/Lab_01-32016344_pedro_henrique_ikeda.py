import random
import time

class Tank(object):
    def __init__(self, name):
        self.name = name    #nome do tanque
        self.alive = True   #para saber se o tanque está vivo ou não
        self.ammo = 5       #para armazenar a munição do tanque
        self.armor = 60     #para armazenar a armadura do tanque

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")
    
    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def fire_at(self, enemy):
        if self.ammo >=1: #verifica a qtde de balas
            self.ammo -=1 #subtrai uma bala ref a um tiro
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")


def auto():
    tank_arr = [] # tank array


    tank_arr.append(Tank("Tank1"))
    tank_arr.append(Tank("Tank2"))
    tank_arr.append(Tank("Tank3"))
    tank_arr.append(Tank("Tank4"))
    tank_arr.append(Tank("Tank5"))


    while len(tank_arr) > 1:

        print("-----------------------")
        print("Attack phase:")
        print("-----------------------")

        attacker = random.randrange(0,len(tank_arr))

        target = random.randrange(0,len(tank_arr))
        while target == attacker:
            target = random.randrange(0,len(tank_arr))

        tank_arr[attacker].fire_at(tank_arr[target])
        print(tank_arr[attacker])
        print(tank_arr[target])

        if not tank_arr[target].alive:
            tank_arr.pop(target)

        if len(tank_arr) > 1:
            print("-----------------------")
            print("Tanks still alive:")
            for tank in tank_arr:
                print(tank)
        
            if len(tank_arr) == 2:
                if tank_arr[0].ammo == 0 and tank_arr[1].ammo == 0:
                    print("\n-------------------------------------------")
                    print("** Game tied! Both tanks are out of ammo **")
                    print("-------------------------------------------")
                    break
        
        
            
        else:
            print("\n-------------------------------------------")
            print(f"** Winner is {tank_arr[0]} **")
            print("-------------------------------------------")

def player():
    nTanks = int(input("How many tanks do you want to create? (min 2 | max 10)\n"))
    while nTanks < 2 or nTanks > 10:
        print("\n**Number not in range, choose a number between 2 and 10.**\n")
        nTanks = int(input("How many tanks do you want to create? (min 2 | max 10)\n"))
    tank_dict = {}
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'O']


    for nTank in range (nTanks):
        tank_dict[chr(ord("A") + nTank)] = Tank(input(f"Enter the tank #{nTank +1} name:\n"))

    for key, value in tank_dict.items():
        print(f"{key}: {value}")

    players_arr = list(tank_dict.keys())

    while True:       
        time.sleep(0.5)

        if len(tank_dict) > 1:
            print("=====================\nStarting Round\n=====================") 
            print("-----------------------")
            print("\rTanks still alive:")
            for key, value in tank_dict.items():
                print(f"{key}: {value}")
            
            if len(tank_dict) == 2:
                cont = 0
                for key, value in tank_dict.items():
                    if value.ammo == 0:
                        cont += 1
                
                if cont == 2:
                    print("\n-------------------------------------------")
                    print("** Game tied! Both tanks are out of ammo **")
                    print("-------------------------------------------")
                    break
            

        
            random.shuffle(players_arr)
            
            for attacker in players_arr:
                
                tmp_dict = dict(tank_dict)
                tmp_dict.pop(attacker)

                print('\n=======================')
                print(f"{tank_dict[attacker].name}\'s tank turn to attack")
                time.sleep(0.2)
                print("Choose your target:\n=======================")

                for key, value in tmp_dict.items():
                    print(f"{key}: {value}")
                print('=======================')

                while True:
                    target_key = input("Target: ").upper()
                    if target_key in tmp_dict.keys():
                        break
                    else:
                        print("Target not valid, choose one from the list below:\n")
                        print('=======================')
                        for key, value in tmp_dict.items():
                            print(f"{key}: {value}")
                        print('=======================')
                
                print(f"You chose to attack {tank_dict[target_key]}")
                time.sleep(0.5)
                tank_dict[attacker].fire_at(tank_dict[target_key])

                if not tank_dict[target_key].alive:
                    print(target_key)
                    tank_dict.pop(str(target_key))
                    players_arr.remove(target_key)

                print('=======================')
                print("Current status")
                print('=======================')
                for key, value in tank_dict.items():
                    print(f"{key}: {value}")
                print('=======================')
                time.sleep(0.5)

                
        
        else:
            print("\n-------------------------------------------")
            print(f"** Winner is ", end='')
            for key, value in tank_dict.items():
                print(f"{key}: {value}")
            print("-------------------------------------------\n")
            break
            


playing = True   
while playing:
    while True:
        print("Choose a mode:")
        print("(1) - Automatic (Ex 1 & 2)")
        print("(2) - Player (Ex 3)")
        print("(3) - Exit")

        mode = int(input("Mode: "))

        if mode == 1 or mode == 2:
            break
    
    if mode == 1:
        auto()
    elif mode == 2:
        player()
    elif mode == 3:
        playing = False
    else:
        print("\n** Invalid option! Choose from 1 to 3 **\n")
    