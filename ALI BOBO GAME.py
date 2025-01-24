"""
        ALI BOBO VA QIRQ QAROQCHI O'YINI
            O'YIN  HAQIDA QISQACHA
                O'YINDA BULAR
                    1 ta ishtirokchi : 🧍
                    1 ta qo'shimcha jon : 🔋+20%
                    1 ta qurol: ⚔️
                    4 ta dushman: ☠️
                O'yinda  istalgan tomonga faqat 1 qadam yurish mumkin:
                    -1: tepaga yoki chapga
                    1: o'ngga yoki pastga
                    o: yurmaslik
                qurol bilan faqat 1 ta dushmanni o'ldirish mumkin va qurol kuchi tugaydi
                marraga yetib borsangiz siz g'olib bo'lasz


"""
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.soul = 100
        self.x = 0
        self.y = 0
        self.bag = []

    def go(self, dx, dy):
        if 0 <= self.x + dx < 10 and 0 <= self.y + dy < 10:
            hudud[self.y][self.x] = "*"
            self.x += dx
            self.y += dy
            hudud[self.y][self.x] = "🧍"
        else:
            print("Chegaradan chiqib ketmaslikka harakat qiling!")

        if self.x == D.x and self.y == D.y and "dori" not in self.bag:
            self.bag.append("dori")
            self.soul += D.tasiri
            print(f"Siz dorini topdingiz! Joningiz +{D.tasiri}%")

        # Qurol topish
        if self.x == qurol.x and self.y == qurol.y and qurol not in self.bag:
            print("Siz qurolni topdingiz! Endi dushman bilan jang qilishingiz mumkin.")
            self.bag.append(qurol)

class Anjomlar:
    pass

class Qurol(Anjomlar):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kuchi = 50

qurol = Qurol(2, 2)

class Dori(Anjomlar):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tasiri = 20

D = Dori(6, 4)

class Dushman:
    def __init__(self, x, y):
        self.joni = 50
        self.zarari = 50
        self.x = x
        self.y = y

    def dushman_yursin(self):
        hudud[self.y][self.x] = "*"  # Dushmanning eski pozitsiyasini tozalash
        while True:
            x_e = random.randint(-1, 1)
            y_e = random.randint(-1, 1)

            if 0 <= self.x + x_e < 10 and 0 <= self.y + y_e < 10:
                self.x += x_e
                self.y += y_e

                if self.x == player.x and self.y == player.y:
                    if qurol in player.bag:
                        self.joni -= qurol.kuchi
                        if self.joni <= 0:
                            print("Siz dushmanni o'ldirdingiz!")
                            break
                        else:
                            player.soul -= self.zarari
                            print(f"Dushman sizni yaraladi! Joningiz: {player.soul}%")
                    else:
                        player.soul -= self.zarari
                        if player.soul <= 0:
                            print(f"{player.name}, siz mag'lub bo'ldingiz!")
                            break
                hudud[self.y][self.x] = "☠️"  # Yangi pozitsiyada dushman belgisi
                break

            else:
                continue

dushman1 = Dushman(2, 5)
dushman2 = Dushman(3, 6)
dushman3 = Dushman(4, 7)
dushman4 = Dushman(5, 9)

hudud = [["*" for _ in range(10)] for _ in range(10)]

def print_hudud():
    for row in hudud:
        print("  ".join(row))
    print()

player = Player(input("Ismingizni kiriting: "))
hudud[player.y][player.x] = "🧍"
hudud[D.y][D.x] = "🔋"
hudud[qurol.y][qurol.x] = "⚔️"
hudud[dushman1.y][dushman1.x] = "☠️"
hudud[dushman2.y][dushman2.x] = "☠️"
hudud[dushman3.y][dushman3.x] = "☠️"
hudud[dushman4.y][dushman4.x] = "☠️"
print_hudud()

def game():
    while player.soul > 0:
        print(f"Jon: {player.soul}% | Anjomlar: {player.bag}")
        try:
            dx = int(input("X yo'nalishi (-1/0/1): "))
            dy = int(input("Y yo'nalishi (-1/0/1): "))
            if dx in [-1, 0, 1] and dy in [-1, 0, 1]:
                player.go(dx, dy)
            else:
                print("Faqat -1, 0 yoki 1 ni kiriting!")
                continue
        except ValueError:
            print("Faqat raqam kiriting!")
            continue

        dushman1.dushman_yursin()
        dushman2.dushman_yursin()
        dushman3.dushman_yursin()
        dushman4.dushman_yursin()

        if player.x == 9 and player.y == 9:
            hudud[player.y][player.x] = "🤴"
            print_hudud()
            print(f"Tabriklaymiz, {player.name}! Siz xazinaga yetib keldingiz! 🏆")
            break

        print_hudud()

game()
