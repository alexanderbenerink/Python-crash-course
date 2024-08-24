# Python cursus (mini)
Een python verfrisser

## Opdrachten
* Collatz
* Lambda
* Custom logger
* DB connectie (sqlite3)
* Decorators
* OOP & URL get requests

### Collatz
    Maak een functie die het volgende doet gebaseerd op een getal:
    - If the number is even, divide it by two.
    - If the number is odd, triple it and add one.

    (BONUS): 
    - Toon het aantal stappen
    - Toon het hoogste getal in de reeks

    Eindresultaat:
        [Start: 5]
        [16]
        [8]
        [4]
        [2]
        [1]
        [Number of steps: 5]
        [Highest number in sequence: 16]

### Lambda
    - Gebruik een lambda functie om in een list van getallen,
      elk getal tot de macht 2 te doen
    -  Gebruik een lambda functie om in een list van getallen,
      alleen de even getallen te tonen

    Eindresultaat:
        {1}
        l = [1, 2, 3, 4, 5]
        # Output: [1, 4, 9, 16, 25]
        {2}
        l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Output: [2, 4, 6, 8, 10]

### Custom logger (Tip: Voeg deze later toe aan een andere functie.)
    - Gebruik de 'import logging' functie van Python om zo een logger te bouwen.
      de logger moet in ieder geval het volgende tonen:
      * Huidige tijd
      * Huidige file
      * Logger niveau e.g. DEBUG / INFO / WARNING etc
      * Het logger bericht
    
    Eindresultaat:
        2024-08-23 20:51:05,606 - (wisselkoers) - DEBUG - Hoi dit is een bericht

### DB connectie (sqlite3)
    - Gebruik Python's built-in 'import sqlite3'
    - Maak een test.db file en creëer een tabel genaamd 'rekeningen',
      en voeg hier de volgende velden aan toe:
        *   id SERIAL PRIMARY KEY,
        *   rekeninghouder text NOT NULL,
        *   rekeningnummer text NOT NULL,
        *   saldo real
    - Gebruik een SQL 'INSERT INTO' commando om zo 1 (of meer) records aan te maken
    - Toon alle rows in de tabel

    Eindresultaat:
        Connected to pythonsqlite.db
        [(1, 'Tim Bolhoeve', 'NL01RABO0123456789', 1000.0)]
        Connection to pythonsqlite.db closed

### Decorators
    - Gebruik Python's 'from functools import wraps' om een decorator te maken
      die de executie tijd van een functie meet (En netjes logged / print).
    
    Eindresultaat:
        Function jouw_functie executed in 0.1s

### OOP & URL get requests
    - Maak een CurrencyConverter class met de volgende variabelen in de init:
    *   mijn_valuta
    *   valuta_symbool
    *   code
    *   symbol
    *   rate
    *   wisselkoers (hoeft niet per-se in de init, mag ook in de class definitie)

    - In de class moeten minimaal de volgende functies staan:
    *   update_wisselkoers
    *   convert_to

    (BONUS)
    -   Voeg een __str__ toe om zo een 'mooiere' print te krijgen.

    Voor het ophalen van de wisselkoers kun je de volgende link gebruiken:
    https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/jouw_valuta.json
    e.g.
    https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json

    Gebruik bij (en na) het ophalen van de gegevens de volgende (ingebouwde) 
    Python modules: 'import urllib.request, json'

    Eindresultaat:
        Begin aantal: 100
        EUR (€) -> GBP (£): 0.84905746
        Converted: 84.90574600000001
        Converted + updated wisselkoers(x1.1): 93.39632060000001

    
