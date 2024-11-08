# Python-kode for å sammenligne årlige kostnader mellom ⚡elbil og 🪨bensinbil
# Editor: VS Code 

# bruker math.ceil for å runde kronebeløp oppover
import math

# spesifikasjon av antall kilometer som kjøres årlig
antall_km_per_aar = 10000  # kan endres her

# forsikringskostnad (kr/år)
forsikring_elbil = 5000
forsikring_bensinbil = 7500

# Trafikkforsikringsavgift (kr/dag >>> år)
trafikkforsikringsavgift_per_dag = 8.38
trafikkforsikringsavgift_per_aar = trafikkforsikringsavgift_per_dag * 366 # hensyntatt skuddår i år... (2024, 2028)

# drivstoffkostnader per kilometer
drivstoffbruk_elbil_kwh_per_km = 0.2
stroempris_per_kwh = 2.0 # flat hjemmeladesats
drivstoffkostnad_elbil_per_km = drivstoffbruk_elbil_kwh_per_km * stroempris_per_kwh
drivstoffkostnad_bensinbil_per_km = 1.0

# bompengeavgift (per kilometer...)
bomavgift_elbil_per_km = 0.1
bomavgift_bensinbil_per_km = 0.3

# årlig kostnad for elbil
kostnader_elbil = math.ceil(
    forsikring_elbil +
    trafikkforsikringsavgift_per_aar +
    (drivstoffkostnad_elbil_per_km * antall_km_per_aar) +
    (bomavgift_elbil_per_km * antall_km_per_aar)
)

# årlig kostnad for bensinbil
kostnader_bensinbil = math.ceil(
    forsikring_bensinbil +
    trafikkforsikringsavgift_per_aar +
    (drivstoffkostnad_bensinbil_per_km * antall_km_per_aar) +
    (bomavgift_bensinbil_per_km * antall_km_per_aar)
)

# kostnadsforskjellen
kostnadsdifferanse = kostnader_bensinbil - kostnader_elbil

# resultat / utskrift
print("_________________________________________________")
print("\n 🪨  BENSINBIL versus ⚡ ELBIL")
print("_________________________________________________")
print(f" Årlig totalkostnad for bensinbil:\n {kostnader_bensinbil} kroner\n")
print(f" Årlig totalkostnad for elbil:\n {kostnader_elbil} kroner")
print("_________________________________________________")
print(f" Årlig kostnadsforskjell (bensinbil - elbil):\n {kostnadsdifferanse} kroner")
print("_________________________________________________")
print("_________________________________________________\n\n")

"""
Programmet skal inneholde passende beskrivelser i form av kommentarer innbakt i koden (blokkommentarer og linjekommentarer). 

Programmet skal lagres på en repo på din Github-konto.

Husk å sjekke at programmet virker som forventet før innleveringen. 

Oppgave 
Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil. 

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor.

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km. 
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år. 
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil. 
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km. 
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km. 
"""
