import abc

class Postac:
    lista_postaci = []
    @abc.abstractmethod
    def __init__(self) -> None:
        pass
    def pokaz(self):
        pass
    def atakuj(self):
        pass
    def wez_miksture(self):
        pass
    def odczytaj(self):
        pass
    def zapisz(self):
        pass

class Wojownik(Postac):
    def __init__(self, imie, zdrowie, obrazenia):
        super().__init__()
        self.imie = imie
        self.zdrowie = zdrowie
        self.obrazenia = obrazenia
        Postac.lista_postaci.append(self.imie)
        Postac.lista_postaci.append(self.zdrowie)
        Postac.lista_postaci.append(self.obrazenia)

    def pokaz(self):
        print(
            f"Wojownik: {self.imie}, zdrowie: {self.zdrowie}, obrazenia: {self.obrazenia}")
    
    def atakuj(self, Postac):
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} nie zyje")
            return
        
        Postac.zdrowie -= self.obrazenia
        print(f"{self.imie} atakuje {Postac.imie} i zadaje {self.obrazenia} obrazen")
        
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} umiera")
            return
    def wez_miksture(self):
        self.zdrowie += 10
        self.obrazenia += 5
        print(f"{self.imie} bierze miksture i zyskuje 10 zdrowia i 5 obrazen")
    def odczytaj(self):
        with open("wojownicy.txt", "r") as file:
            for line in file:
                self.imie, self.zdrowie, self.obrazenia = line.split(',')
                self.zdrowie = int(self.zdrowie)
                self.obrazenia = int(self.obrazenia)
                print(f"{self.imie} {self.zdrowie} {self.obrazenia}")
                self.lista_postaci.append(self.imie)
                self.lista_postaci.append(self.zdrowie)
                self.lista_postaci.append(self.obrazenia)
        print(self.lista_postaci)
    def zapisz(self):
        with open("wojownicy.txt", "w") as file:
            for i in range(0, len(Postac.lista_postaci), 3):
                file.write(f"{Postac.lista_postaci[i]},{Postac.lista_postaci[i+1]},{Postac.lista_postaci[i+2]}\n")
        print("Zapisano do pliku")
        


class Lucznik(Postac):
    def __init__(self, imie, zdrowie, obrazenia, zasieg):
        super().__init__()
        self.imie = imie
        self.zdrowie = zdrowie
        self.obrazenia = obrazenia
        self.zasieg = zasieg
        Postac.lista_postaci.append(self.imie)

    def pokaz(self):
        print(
            f"Lucznik: {self.imie}, zdrowie: {self.zdrowie}, obrazenia: {self.obrazenia}, zasieg: {self.zasieg}")
        
    def atakuj(self, Postac):
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} nie zyje")
            return
        
        Postac.zdrowie -= self.obrazenia
        print(f"{self.imie} atakuje {Postac.imie} i zadaje {self.obrazenia} obrazen")
        
        if Postac.zdrowie <= 0:
            print(f"{Postac.imie} umiera")
            return
    
    def wez_miksture(self):
        self.zdrowie += 5
        self.obrazenia += 8
        print(f"{self.imie} bierze miksture i zyskuje 5 zdrowia i 8 obrazen")
        
def pojedynek(Postac1, Postac2):
    while Postac1.zdrowie > 0 and Postac2.zdrowie > 0:
        Postac1.atakuj(Postac2)
        Postac2.atakuj(Postac1)
        print("")
        Postac1.pokaz()
        Postac2.pokaz()
        print("")
        if Postac1.zdrowie <= 0:
            print(f"{Postac1.imie} umiera")
            return
        if Postac2.zdrowie <= 0:
            print(f"{Postac2.imie} umiera")
            return
    


#p1 = Wojownik("Anders", 40, 20)
#p2 = Lucznik("Grido", 100, 10, 50)
#p3 = Wojownik("Karl", 50, 30)
#p4 = Lucznik("Trup", 0, 30, 50)

Wojownik.odczytaj(Wojownik)
