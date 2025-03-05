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










class Student:
    ime = 'Pero'
    prezime = 'Peric'
    broj_indeksa = '123456'
    godina_studija = 2021
    prosjek_ocjena = 4.89


pero = Student()

# Ispis podataka
print('Ispis iz klase Student - Pero')
print(pero.ime)
print(pero.prezime)
print(pero.broj_indeksa)
print(pero.godina_studija)
print(pero.prosjek_ocjena)
print()


ana = Student()
# Ispis podataka
print('Ispis iz klase Student - Ana')
print(ana.ime)
print(ana.prezime)
print(ana.broj_indeksa)
print(ana.godina_studija)
print(ana.prosjek_ocjena)
print()
