# Oppgave 1 – 2025 Edition
print("O_1\n")
print("Alder er bare et tall")

# Spør om fødselsår
alder = int(input("Hvilket år er du født? "))  # Inndata fødselsår

# Beregne (høyeste) alder for 2025 ved å trekke fødselsåret fra 2025
alder_i_2025 = 2025 - alder  # Beregne alderen i år

# Alder i 2025
print("I 2025 vil du fylle", alder_i_2025, "år gammel.")  # Resultatvisning

print("\n– – – \n")


# Oppgave 2
print("O_2\n")
print("Pizzaklassefest")

import math  # Går en tur på mattebiblioteket

# Antall elever
antall_elever = int(input("Skriv inn antall elever: "))

# Hver elev spiser 1/4 pizza – totalt blir det antall_elever * 1/4
pizzabehov = antall_elever * 0.25

# Vi kan ikke kjøpe deler av en pizza -> runder opp til nærmeste heltall
antall_pizza = math.ceil(pizzabehov)

# Skriver ut antall pizza
print("Du må bestille", antall_pizza, "pizzaer.")

print("\n– – – \n")


# Oppgave 3
print("O_3\n")
print("Geometri")

import numpy as np  # Trengs for π

# Vi forvandler fra grader til radianer ved bruk av formelen "v_rad = v_grad * np.pi / 180"
def grader_til_radianer(vinkel_grad):
    vinkel_rad = vinkel_grad * np.pi / 180
    return vinkel_rad

# Inndata <- gradverdi
v_grad = float(input("Skriv inn gradtallet: "))

# Mattemagisk utregning av radianverdien ved å bruke funksjonen grader_til_radianer
v_rad = grader_til_radianer(v_grad)

# Svar til skjerm med to streker under
print("Vinkelen i radianer er:", v_rad)
print("==========")

print("\n– – – \n")


# Oppgave 4 a
print("O_4_a\n")
print("✅ landinfo data ok")
# Etablerer "landordboken" landinfo med hovedsteder og innbyggertall (i millioner)
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

print("\n– – – \n")


# Oppgave 4 b
print("O_4_b\n")
print("🔍 hent landinfo")

# Kor ska vi reis hen?
land = input("Skriv inn et land: ")

# Bla i ordboken etter land
if land in data:
    hovedstad, innbyggertall = data[land]  # parameterbygging
    # Skriv ut setningen med riktig informasjon
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggertall} mill. innbyggere i {hovedstad}")
else:
    print("404 😵‍💫")

print("\n– – – \n")


# Oppgave 4 c
print("O_4_c\n")
print("➕ legg til landinfo")

# Legg til et nytt land i landinfo
nytt_land = input("Hvilket land vil du legge til?")

# Inndata <- hovedstaden
ny_hovedstad = input("Skriv inn navnet på hovedstaden i " + nytt_land + ": ")

# Inndata <- innbyggertall (i millioner)
ny_innbyggertall = float(input("Hvor mange millioner personer bor det i " + ny_hovedstad + ": "))

# Legg til oppføringen i landinfo-ordboken
data[nytt_land] = [ny_hovedstad, ny_innbyggertall]

# Ordbokutlisting
print("Oppdatert landinfo:")
print(data)

print("\n– – – \n")


# Oppgave 5
print("O_5\n")
print("📏 geometri 2")

import math
def figur_areal_omkrets(a, b):
    """
    Funksjonsbeskrivelse

    Vi tar inn to parametre til behandling
    a = diameteren til halvsirkelen, som er lik én av katetene i trekanten
    b = den andre kateten i trekanten.

    Funksjonen regner ut og returnerer to verdier

    1: Arealet av figuren (trekant + halvsirkel)
    2: Ytre omkrets (b + hypotenus + halvsirkelen)
    """
    # Areal til trekanten (1/2 = 0.5)
    areal_trekant = a * b * 0.5

    # Areal av halv (0.5) sirkel
    areal_halvsirkel = 0.5 * math.pi * ((a/2)**2)

    # Totalareal
    totalt_areal = areal_trekant + areal_halvsirkel

    # hypotenus via katetene a og b (Pytagoras' setning)
    hyp = math.sqrt(a**2 + b**2)

    # Halvsirkelbue (halv sirkel = pi*a/2)
    halvsirkelbue = (math.pi * a) / 2

    # Ytre omkrets
    ytre_omkrets = b + hyp + halvsirkelbue

    return totalt_areal, ytre_omkrets

# Inndataspørring
a = float(input("Skriv inn tall a (diameteren til halvsirkelen = katet i trekanten): "))
b = float(input("Skriv inn tall b (den andre kateten i trekanten): "))

# Funksjonen anvendt
areal, omkrets = figur_areal_omkrets(a, b)

# Print svar
print(f"Arealet av figuren (trekant + halvsirkel) er {areal:.3f}.")
print(f"Ytre omkrets av figuren er {omkrets:.3f}.")

print("\n– – – \n")


# Oppgave 6
print("O_6\n")
print("Putti, putti, plot")

import numpy as np
import matplotlib.pyplot as plt

# Fordele x-verdier i anbefalt område
x_verdier = np.linspace(-10, 10, 200)

# Regn ut f(x) = -x^2 - 5 for hver verdi i x_verdier
y_verdier = -(x_verdier ** 2) - 5

# Plotte funksjonen
plt.plot(x_verdier, y_verdier, label="f(x) = -x^2 - 5")

# Titteltekst og labling
plt.title("Grafen til f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")

# Aktiver rutenett
plt.grid(True)
plt.legend()

# Skriv ut til skjerm
plt.show()

print("\n– – – – – –\n")
