import abc

class Postac:
    lista_postaci = []
    rodzaj = ""
    @abc.abstractmethod
    def __init__(self) -> None:
        pass
    def stworz(self):
        pass
    def pokaz(self):
        pass
    def atakuj(self):
        pass
    def ulecz_sie(self):
        pass
    def awansuj(self):
        pass
    def usun(self):
        pass

class Wojownik(Postac):
    rodzaj = "Wojownik"
    imie = ""
    zdrowie = 0
    obrazenia = 0
    def __init__(self, imie = None, zdrowie = None, obrazenia = None):
        super().__init__()
        if imie is not None:
            self.imie = imie
            self.zdrowie = zdrowie
            self.obrazenia = obrazenia
        else:
            self.stworz()
        
    def stworz(self):
        self.imie = input("Podaj imie: ")
        specjalizacja = int(input("Wybierz specjalizację: \n1. Zdrowie: 100, Obrazenia: 10 \n2. Zdrowie: 120, Obrazenia: 8 \n3. Zdrowie: 150, Obrazenia: 5 \n Wybieram: "))
        if specjalizacja == 1:
            self.zdrowie = 100
            self.obrazenia = 10
        elif specjalizacja == 2:
            self.zdrowie = 120
            self.obrazenia = 8
        elif specjalizacja == 3:
            self.zdrowie = 150
            self.obrazenia = 5
        else:
            print("Nie ma takiej specjalizacji")
            print("Wybierz jeszcze raz\n")
            self.stworz()
        statystyki = tuple((self.rodzaj, self.imie, self.zdrowie, self.obrazenia))
        Postac.lista_postaci.append(statystyki)
    def pokaz(self):
        print(f"\nWojownik: {self.imie} \nZdrowie: {self.zdrowie} \nObrazenia: {self.obrazenia}\n")
    def atakuj(self, Postac):
        if Postac.zdrowie <= 0:
            raise AttributeError(print(f"{Postac.imie} nie zyje"))
        Postac.zdrowie -= self.obrazenia
        print(f"{self.imie} atakuje {Postac.imie} i zadaje {self.obrazenia} obrażen fizycznych")
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} umiera")
            return
    def ulecz_sie(self):
        self.zdrowie += 10
        print(f"{self.imie} używa mikstury i zyskuje 10 zdrowia")
    def awansuj(self):
        self.obrazenia += 5
        print(f"{self.imie} awansuje i zyskuje 5 obrażen")
    def usun(self):
        Postac.lista_postaci.remove((self.rodzaj, self.imie, self.zdrowie, self.obrazenia))
        print(f"{self.imie} umiera")
        del Postac.lista_postaci[-1]
        
class Mag(Postac):
    rodzaj = "Mag"
    imie = ""
    zdrowie = 0
    moc = 0
    def __init__(self, imie = None, zdrowie = None, moc = None):
        super().__init__()
        if imie is not None:
            self.imie = imie
            self.zdrowie = zdrowie
            self.moc = moc
        else:
            self.stworz()
    def stworz(self):
        self.imie = input("Podaj imie: ")
        specjalizacja = int(input("Wybierz specjalizację: \n1. Zdrowie: 100, Moc: 10 \n2. Zdrowie: 120, Moc: 8 \n3. Zdrowie: 150, Moc: 5 \n Wybieram: "))
        if specjalizacja == 1:
            self.zdrowie = 100
            self.moc = 10
        elif specjalizacja == 2:
            self.zdrowie = 120
            self.moc = 8
        elif specjalizacja == 3:
            self.zdrowie = 150
            self.moc = 5
        else:
            print("Nie ma takiej specjalizacji")
            print("Wybierz jeszcze raz\n")
            self.stworz()
        statystyki = tuple((self.rodzaj, self.imie, self.zdrowie, self.moc))
        Postac.lista_postaci.append(statystyki)
    def pokaz(self):
        print(f"\nMag: {self.imie} \nZdrowie: {self.zdrowie} \nMoc: {self.moc}\n")
    def atakuj(self, Postac):
        if Postac.zdrowie <= 0:
            raise AttributeError(print(f"{Postac.imie} nie zyje"))
        Postac.zdrowie -= self.moc
        print(f"{self.imie} atakuje {Postac.imie} i zadaje {self.moc} obrażen magicznych")
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} umiera")
            return
    def ulecz_sie(self):
        self.zdrowie += 10
        print(f"{self.imie} używa mikstury i zyskuje 10 zdrowia")
    def awansuj(self):
        self.moc += 5
        print(f"{self.imie} awansuje i zyskuje 5 mocy")
    def usun(self):
        Postac.lista_postaci.remove((self.rodzaj, self.imie, self.zdrowie, self.moc))
        print(f"{self.imie} umiera")
        del Postac.lista_postaci[-1]

def zapisz_do_pliku():
    with open("postacie.txt", "w") as file:
        for line in Postac.lista_postaci:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")
            
def odczytaj_z_pliku():
    with open("postacie.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
            Postac.lista_postaci.append(line)
        lista_postaci = list(Postac.lista_postaci)
        return lista_postaci

def wyswietl_postacie():
    licznik = 1
    for line in Postac.lista_postaci:
        if line[0] == "Wojownik":
            print (f"{licznik}. {line[0]}: {line[1]} \nZdrowie: {line[2]} | Obrażenia: {line[3]}\n")
        if line[0] == "Mag":
            print (f"{licznik}. {line[0]}: {line[1]} \nZdrowie: {line[2]} | Moc: {line[3]}\n")    
        licznik += 1

odczytaj_z_pliku()

for element in Postac.lista_postaci:
    print(element)

zapisz_do_pliku()
