from ctypes.wintypes import tagMSG
import random

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

# meuTanque = Tank("Bob")
# meuTanque2 = Tank("Jack")
# meuTanque.fire_at(meuTanque2)
# print(meuTanque)
# print(meuTanque2)


tank_arr = [] # tank array

# tank1 = Tank("Tank1")
# tank2 = Tank("Tank2")
# tank3 = Tank("Tank3")
# tank4 = Tank("Tank4")
# tank5 = Tank("Tank5")

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
