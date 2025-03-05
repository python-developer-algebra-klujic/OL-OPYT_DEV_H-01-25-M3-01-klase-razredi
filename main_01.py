'''
Zadatak 1.
Definirajte klasu Student s atributima:
    ime, prezime, broj indeksa i godina studija.

Kreirajte konstruktor za inicijalizaciju ovih atributa.
Dodajte metodu prikazi_podatke koja ispisuje sve podatke o studentu.
'''


ime = 'Pero'
prezime = 'Peric'
broj_indeksa = '123456'
godina_studija = 2021
prosjek_ocjena = 4.89

# Ispis podataka
print('Ispis iz varijabli')
print(ime)
print(prezime)
print(broj_indeksa)
print(godina_studija)
print(prosjek_ocjena)
print()





student = {
    'ime': 'Pero',
    'prezime': 'Peric',
    'broj_indeksa': '123456',
    'godina_studija': 2021,
    'prosjek_ocjena': 4.89
}

# Ispis podataka
print('Ispis iz rjecnika')
print(student['ime'])
print(student['prezime'])
print(student['broj_indeksa'])
print(student['godina_studija'])
print(student['prosjek_ocjena'])
print()



def create_student(ime, prezime, broj_indeksa, godina_studija, prosjek_ocjena):
    interna_var_ime = ime
    interna_var_prezime = prezime
    interna_var_broj_indeksa = broj_indeksa
    interna_var_godina_studija = godina_studija
    interna_var_prosjek_ocjena = prosjek_ocjena

create_student('Pero', 'Peric', '123456', 2021, 4.89)




class Student:
    # Konstruktor klase - bolji izraz konstruktor objekata ove klase
    def __init__(self, ime, prezime, broj_indeksa, godina_studija, prosjek_ocjena):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.godina_studija = godina_studija
        self.prosjek_ocjena = prosjek_ocjena

    def ispis(self):
        print(f'Ispis iz metode u klasi Student - {self.ime}')
        print(f'Ime: {self.ime}')
        print(f'Prezime: {self.prezime}')
        print(f'Broj indeksa: {self.broj_indeksa}')
        print(f'Godina studija {self.godina_studija}')
        print(f'Prosjek ocjena {self.prosjek_ocjena}')
        print()










pero = Student('Pero', 'Peric', '123456', 2021, 4.89)
# Ispis podataka
# print('Ispis iz klase Student - Pero')
# print(pero.ime)
# print(pero.prezime)
# print(pero.broj_indeksa)
# print(pero.godina_studija)
# print(pero.prosjek_ocjena)
# print()
pero.ispis()


ana = Student('Ana', 'Anic', '654321', 2024, 4.98)
# ana.ime = 'Ana'
# ana.prezime = 'Anic'
# ana.broj_indeksa = '654321'
# ana.godina_studija = 2024
# ana.prosjek_ocjena = 4.98
# Ispis podataka
# print('Ispis iz klase Student - Ana')
# print(ana.ime)
# print(ana.prezime)
# print(ana.broj_indeksa)
# print(ana.godina_studija)
# print(ana.prosjek_ocjena)
# print()
ana.ispis()
