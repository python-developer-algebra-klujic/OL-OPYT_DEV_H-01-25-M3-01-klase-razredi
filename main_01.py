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

# Ispis podataka
print('Ispis iz varijabli')
print(ime)
print(prezime)
print(broj_indeksa)
print(godina_studija)
print()





student = {
    'ime': 'Pero',
    'prezime': 'Peric',
    'broj_indeksa': '123456',
    'godina_studija': 2021
}

# Ispis podataka
print('Ispis iz rjecnika')
print(student['ime'])
print(student['prezime'])
print(student['broj_indeksa'])
print(student['godina_studija'])
print()










class Student:
    ime = 'Pero'
    prezime = 'Peric'
    broj_indeksa = '123456'
    godina_studija = 2021


pero = Student()

# Ispis podataka
print('Ispis iz klase Student')
print(pero.ime)
print(pero.prezime)
print(pero.broj_indeksa)
print(pero.godina_studija)
print()
