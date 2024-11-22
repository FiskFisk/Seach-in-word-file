# Filviser og Søkeapplikasjon

Dette Python-skriptet er en grafisk applikasjon som lar brukeren velge tekstfiler, vise innholdet i dem og søke etter spesifikke ord eller uttrykk i teksten. Skriptet bruker **CustomTkinter** for et moderne og responsivt grensesnitt.

## Funksjonalitet

1. **Åpne tekstfiler**:  
   Brukeren kan velge tekstfiler fra datamaskinen ved hjelp av en filvelger. Skriptet støtter både `.txt`-filer og andre tekstbaserte filer. Det håndterer forskjellige filkodingsformater, som UTF-8 og `latin1`, for å sikre at filen åpnes korrekt.

2. **Vise filinnhold**:  
   Innholdet i den valgte filen vises i en rullbar tekstboks med ordinnpakning, som gir en god leseopplevelse. Brukeren kan enkelt bla gjennom teksten ved hjelp av rullefeltet.

3. **Søke etter ord**:  
   Brukeren kan skrive inn et søkeord eller en frase i et dedikert søkefelt. Når søket utføres:  
   - Alle treff markeres med gul bakgrunn.  
   - Antall treff vises i en etikett under søkefeltet.

4. **Moderne design**:  
   Applikasjonen benytter CustomTkinter for et oppdatert utseende, inkludert støtte for lys og mørk modus.

## Hvordan det fungerer

### Filvalg
- Når brukeren klikker på "Select a File", åpnes et dialogvindu som lar brukeren velge en fil.
- Programmet prøver å lese filen med UTF-8-koding. Hvis det oppstår en feil, brukes `latin1` som fallback.

### Tekstvisning
- Filinnholdet lastes inn og vises i tekstboksen.
- Teksten er rullbar, og linjene brytes ved ordgrenser for bedre lesbarhet.

### Søkemekanisme
- Brukeren skriver inn et søkeord i søkefeltet og trykker på "Search".
- Alle forekomster av ordet markeres i teksten med gul bakgrunn.
- Programmet teller antall treff og oppdaterer en etikett for å vise resultatet.

## Bruksanvisning

1. Installer nødvendige avhengigheter:
   ```bash
   pip install customtkinter

2. Starte scriptet
   - Lagre skriptet i en fil, for eksempel app.py.
   - Kjør programmet:
   ```bash
   python app.py

3. Du kan følge disse trinnene i programmet:
  - Klikk på "Select a File" for å åpne en fil.
  - Les filens innhold i tekstboksen.
  - Skriv inn et søkeord i feltet og trykk på "Search" for å finne ordet i teksten.

## Krav
1. Python-versjon: Python 3.9 eller nyere.
2. Avhengigheter:
3. customtkinter (installeres med pip).
