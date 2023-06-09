import abc
import os
import msvcrt

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
    def __init__(self, rodzaj = None, imie = None, zdrowie = None, obrazenia = None):
        super().__init__()
        if imie is not None:
            self.rodzaj = rodzaj
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
        print(f"Wojownik: \t{self.imie} | Zdrowie: {self.zdrowie} | Obrazenia: {self.obrazenia}\n")
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
    def __init__(self, rodzaj = None, imie = None, zdrowie = None, moc = None):
        super().__init__()
        if imie is not None:
            self.rodzaj = rodzaj
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
        print(f"Mag: \t{self.imie} | Zdrowie: {self.zdrowie} | Moc: {self.moc}\n")
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

            
def zapisz_do_pliku(Postac = list()):
    with open("postacie.txt", "w") as file:
        for element in Postac:    
            if element.rodzaj == "Wojownik":
                file.write(f"Wojownik,{element.imie},{element.zdrowie},{element.obrazenia}\n")
            if element.rodzaj == "Mag":
                file.write(f"Mag,{element.imie},{element.zdrowie},{element.moc}\n")
            
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
        
def utworz_obiekty():
    obiekty = []
    for line in Postac.lista_postaci:
        if line[0] == "Wojownik":
            line[2] = int(line[2])
            line[3] = int(line[3])
            obiekty.append(Wojownik(line[0],line[1], line[2], line[3]))
        if line[0] == "Mag":
            line[2] = int(line[2])
            line[3] = int(line[3])
            obiekty.append(Mag(line[0],line[1], line[2], line[3]))
    return obiekty

def menu():
    os.system("cls")
    print("Witaj w grze RPG!")
    print()
    print("Wybierz opcję: ")
    print("1. Stwórz postać")
    print("2. Wyświetl postacie")
    print("3. Atakuj")
    print("4. Ulecz się")
    print("5. Awansuj")
    print("6. Usuń postać")
    print("7. Zakończ program")
    
    try:
        print("Wybieram: ", end="")
        wybor = int(msvcrt.getch())
        print()
    except ValueError:
        print("Nie ma takiej opcji")
        wybor = menu()
    return wybor

def wykonaj(wybor, lista):
    if wybor == 1:
        print("1. Wojownik")
        print("2. Mag")
        wybor = int(input("Wybieram: "))
        if wybor == 1:
            lista.append(Wojownik())
            print("Dodano Wojownika!")
            os.system("pause")
        elif wybor == 2:
            lista.append(Mag())
            print("Dodano Maga!")
            os.system("pause")
        else:
            print("Nie ma takiej opcji")
            os.system("pause")
    elif wybor == 2:
        licznik = 1
        for element in lista:
            print(licznik, end=". ")
            element.pokaz()
            licznik += 1
        os.system("pause")
    elif wybor == 3:
        licznik = 1
        for element in lista:
            print(licznik, end=". ")
            element.pokaz()
            licznik += 1
        wybor = int(input("Wybierz postać atakującą: "))
        wybor2 = int(input("Wybierz postać atakowaną: "))
        lista[wybor-1].atakuj(lista[wybor2-1])
        os.system("pause")
    elif wybor == 4:
        licznik = 1
        for element in lista:
            print(licznik, end=". ")
            element.pokaz()
            licznik += 1
        wybor = int(input("Wybierz postać do uleczenia: "))
        lista[wybor-1].ulecz_sie()
        os.system("pause")
    elif wybor == 5:
        licznik = 1
        for element in lista:
            print(licznik, end=". ")
            element.pokaz()
            licznik += 1
        wybor = int(input("Wybierz postać do awansu: "))
        cel = lista[wybor-1]
        cel.awansuj()
        os.system("pause")
    elif wybor == 6:
        licznik = 1
        for element in lista:
            print(licznik, end=". ")
            element.pokaz()
            licznik += 1
        wybor = int(input("Wybierz postać do usunięcia: "))
        del lista[wybor - 1]
        print("Postać została usunięta")
        os.system("pause")
    elif wybor == 7:
        zapisz_do_pliku(lista)
        print("Zapisano do pliku!")
        print("Do zobaczenia!")
        exit()
    else:
        print("Nie ma takiej opcji")
        os.system("pause")

#Aplikacja
odczytaj_z_pliku() #odczytujemy z pliku i zapisujemy do listy obiektów
Lista_postaci_temp = list(utworz_obiekty()) #lista obiektów, na których działamy w programie
    
while True:
    wykonaj(menu(), Lista_postaci_temp)
