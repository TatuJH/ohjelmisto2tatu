import random

#Tehtävä 10.1
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 0
    def kerros_ylös(self, kerros):
        self.kerros += 1
        print(self.kerros)
    def kerros_alas(self, kerros):
        self.kerros -= 1
        print(self.kerros)
    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if kerros < self.kerros:
                self.kerros_alas(kerros)
            else:
                self.kerros_ylös(kerros)

def main():
    h = Hissi(1, 100)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(h.alin)

main()

#Tehtävä 10.2
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 0
    def kerros_ylös(self, kerros):
        self.kerros += 1
        print(self.kerros)
    def kerros_alas(self, kerros):
        self.kerros -= 1
        print(self.kerros)
    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if kerros < self.kerros:
                self.kerros_alas(kerros)
            else:
                self.kerros_ylös(kerros)

class Talo:
    def __init__(self, alin, ylin, määrä):
        self.alin = alin
        self.ylin = ylin
        self.määrä = määrä
        self.hissit = []
        for hissi in range(määrä):
            h = Hissi(alin, ylin)
            self.hissit.append(h)

    def aja_hissiä(self, numero, kerros):
        self.hissit[numero-1].siirry_kerrokseen(kerros)

def main():
    t = Talo(1, 100, 5)
    for i in range(5):
        t.aja_hissiä(i, random.randint(1, 100))

main()

#Tehtävä 10.3
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 0
    def kerros_ylös(self, kerros):
        self.kerros += 1
        print(self.kerros)
    def kerros_alas(self, kerros):
        self.kerros -= 1
        print(self.kerros)
    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if kerros < self.kerros:
                self.kerros_alas(kerros)
            else:
                self.kerros_ylös(kerros)

class Talo:
    def __init__(self, alin, ylin, määrä):
        self.alin = alin
        self.ylin = ylin
        self.määrä = määrä
        self.hissit = []
        for hissi in range(määrä):
            h = Hissi(alin, ylin)
            self.hissit.append(h)

    def aja_hissiä(self, numero, kerros):
        self.hissit[numero-1].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for hissi in range(len(self.hissit)):
            self.hissit[hissi].siirry_kerrokseen(self.alin)

def main():
    t = Talo(1, 100, 5)
    for i in range(5):
        t.aja_hissiä(i, random.randint(1, 100))
    t.palohälytys()

main()

#Tehtävä 10.4
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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10,15))
            auto.kulje(1)
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"{auto.rekkari} | max. {auto.mnopeus}km/h | {auto.nopeus}km/h | {auto.matka}km\n------------------------------------------")

def main():
    autot =[]
    for i in range(1,11):
        rekkari = f"ABC-{i}"
        mnopeus = random.randint(100, 200)
        auto = Auto(rekkari, mnopeus)
        autot.append(auto)

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0

    ohi = False

    while not ohi:
        tunnit += 1
        kilpailu.tunti_kuluu()
        ohi = kilpailu.kilpailu_ohi()
        if tunnit % 10 == 0:
            print(f"Tunteja kulunut: {tunnit}")
            kilpailu.tulosta_tilanne()

    print(f"Lopputilanne (tunti {tunnit}):")
    kilpailu.tulosta_tilanne()

main()