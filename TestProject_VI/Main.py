# Importing the Libraries
import csv
import visualization as vis

myList = []

csv_file_path = 'bearbeitete_csv_datei.csv'


# Importing the original CSV file
with open ('Artikel.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        myList.append(row)

# Showing the content to user with printing out the row number 3
print("Pruefen Sie die Angaben der CSV datei unten")
for i in range(len(myList)):
    print("Row" + str(i) + " : " + str(myList[i]))

# Editing the CSV file with user preferences 4
while True:
    try:
        editRow = int(input(f"\nWelche Zeile soll editiert werden? (1 - {len(myList)}): ")) - 1
        if 0 <= editRow < len(myList):
            break
        else:
            print(f"Bitte geben Sie eine Zahl zwischen 1 und {len(myList)} ein.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

print("Bitte fuellen Sie die naechsten Felder aus:")

# Taking the input about editing the CSV 5
for i in range (len(myList[0])):
    newDetails = input("Tippen Sie neue Info fuer " + str(myList[0][i]) + " ein:")
    myList[editRow][i] = newDetails

# Showing the result to user and confirm changes
print("\n Bitte pruefen Sie Ihre Angaben unten:")
for i in range(len(myList)):
    print("Row" + str(i) + " : " + str(myList[i]))


 # Asking if user wants to save the updates
changeCSV = input ("\n Moechten Sie die Aenderungen speichern? (J/N):").lower()

if changeCSV == ("j"):
    with open ('bearbeitete_csv_datei', 'w', encoding='utf8', newline='') as file:
        correctedCSV = csv.writer(file)
        for i in range (len(myList)):
            correctedCSV.writerow(myList[i])
    print("Die Aenderungen wurden erfolgreich gespeichert im File unter Namen 'bearbeitete_csv_datei.csv' im Ordner des Projekts ")
    vis.visualizer(myList)
# Close the Program if not saving the results
if changeCSV == ("n"):
    print ("Die Aenderungen wurden abgebrochen. Programm wird geschlossen.")
