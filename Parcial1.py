import random #nunca lo usamos por el momento por que si lo vamos a usar XD :D

class hero:
    def create_hero(name, attack=15, health=100):
        print(
            "Name: " + name,
            "Attack: " + attack,
            "Health: " + health
        )

        return hero

class enemy:
    def create_enemy(name, attack=10 , health=100):

        enemy={
            "Name": name,
            "Attack": attack,
            "Health": health
        }

        return enemy

#class boss(enemy):  //es una opcion esto 


class war:
    def battle(hero,enemy):
        return battle 

    def lose_health():
        if hero['health'] == 0 :
            print("You lose")
        return hero


hero = input("Create a hero") 