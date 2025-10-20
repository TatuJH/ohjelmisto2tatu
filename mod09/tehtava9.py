import random

#Tehtävä 9.1
class Auto:
    def __init__(self, rekkari, mnopeus):
        self.rekkari = rekkari
        self.mnopeus = mnopeus
        self.nopeus = 0
        self.matka = 0
def main():
    auto2 = Auto("ABC-123", 142)
    print(f"{auto2.rekkari}, {auto2.mnopeus}km/h, {auto2.nopeus}, {auto2.matka}")
main()

#Tehtävä 9.2
class Auto:
    def __init__(self, rekkari, mnopeus):
        self.rekkari = rekkari
        self.mnopeus = mnopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdyta(self, muutos):
        if self.nopeus + muutos <= self.mnopeus and self.nopeus + muutos >= 0:
            self.nopeus += muutos
        elif self.nopeus + muutos > self.mnopeus:
            self.nopeus = self.mnopeus
        elif self.nopeus + muutos < 0:
            self.nopeus = 0

def main():
    auto2 = Auto("ABC-123", 142)
    print(f"{auto2.rekkari}, {auto2.mnopeus}km/h, {auto2.nopeus}, {auto2.matka}")
    auto2.kiihdyta(30)
    auto2.kiihdyta(70)
    auto2.kiihdyta(100)
    print(f"{auto2.nopeus}km/h")
    auto2.kiihdyta(-200)
    print(f"{auto2.nopeus}km/h")
main()

#Tehtävä 9.3
class Auto:
    def __init__(self, rekkari, mnopeus):
        self.rekkari = rekkari
        self.mnopeus = mnopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdyta(self, muutos):
        if self.nopeus + muutos <= self.mnopeus and self.nopeus + muutos >= 0:
            self.nopeus += muutos
        elif self.nopeus + muutos > self.mnopeus:
            self.nopeus = self.mnopeus
        elif self.nopeus + muutos < 0:
            self.nopeus = 0
    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

def main():
    auto2 = Auto("ABC-123", 142)
    print(f"{auto2.rekkari}, {auto2.mnopeus}km/h, {auto2.nopeus}, {auto2.matka}")
    auto2.kiihdyta(30)
    auto2.kiihdyta(70)
    auto2.kiihdyta(100)
    print(f"{auto2.nopeus}km/h")
    auto2.kiihdyta(-200)
    print(f"{auto2.nopeus}km/h")
    auto2.matka = 2000
    auto2.nopeus = 60
    auto2.kulje(1.5)
    print(f"{auto2.matka}km")
main()

#Tehtävä 9.4
class Auto:
    def __init__(self, rekkari, mnopeus):
        self.rekkari = rekkari
        self.mnopeus = mnopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdyta(self, muutos):
        if self.nopeus + muutos <= self.mnopeus and self.nopeus + muutos >= 0:
            self.nopeus += muutos
        elif self.nopeus + muutos > self.mnopeus:
            self.nopeus = self.mnopeus
        elif self.nopeus + muutos < 0:
            self.nopeus = 0
    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

def main():
    autot =[]
    for i in range(1,11):
        rekkari = f"ABC-{i}"
        mnopeus = random.randint(100, 200)
        auto = Auto(rekkari, mnopeus)
        autot.append(auto)

    tunnit = 0
    ohi = False

    while not ohi:
        tunnit += 1
        for auto in autot:
            auto.kiihdyta(random.randint(-10,15))
            auto.kulje(1)
            if auto.matka >= 10000:
                ohi = True

    for auto in autot:
        print(f"{auto.rekkari}, {auto.mnopeus}km/h, {auto.nopeus}, {auto.matka}")

main()


