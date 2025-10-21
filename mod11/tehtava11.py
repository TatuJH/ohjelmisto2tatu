#Tehtävä 11.1
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, päätoimittaja {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, kirjoittanut {self.kirjoittaja}, sivuja {self.sivut}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta_tiedot()

#Tehtävä 11.2
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

class Sähköauto(Auto):
    def __init__(self, rekkari, mnopeus, akku):
        super().__init__(rekkari, mnopeus)
        self.akku = akku
        self.nopeus = 0
        self.matka = 0
    def mittari(self):
        print(f"{self.rekkari}, {self.nopeus} km/h, {self.akku} kWh, {self.matka} km")

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, mnopeus, tankki):
        super().__init__(rekkari, mnopeus)
        self.tankki = tankki
        self.nopeus = 0
        self.matka = 0
    def mittari(self):
        print(f"{self.rekkari}, {self.nopeus} km/h, {self.tankki} l, {self.matka} km")

def main():
    autot = []
    autot.append(Sähköauto("ABC-15", 180, 52.5))
    autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

    for auto in autot:
        auto.kiihdyta(50)
        auto.kulje(3)
        auto.mittari()

main()