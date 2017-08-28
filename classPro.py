class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1
    
    def checklife(self):
        if self.life <= 0:
            print("you are out of game")
        else:
            print(str(self.life)+" life left")

Enemy1 = Enemy()
Enemy2 = Enemy()
Enemy1.attack()
Enemy1.checklife()
Enemy2.checklife()