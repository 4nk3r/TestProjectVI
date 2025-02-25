import csv
import matplotlib.pyplot as plt
import os
# Konstants for user options
YES_OPTION = "j"
VISUALIZATION_TYPES = {"1": "pie_chart", "2": "bar_chart", "3": "scatter_plot"}


def read_csv_file(filepath):
    #Reads the CSV file according to the path
    try:
        with open(filepath, 'r', encoding='utf8') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Die Datei '{filepath}' wurde nicht gefunden. Bitte versuchen Sie es erneut.")
    except Exception as e:
        print(f"Fehler beim Öffnen der Datei: {e}. Bitte versuchen Sie es erneut.")
    return []


def get_column_selection(data):
    # Returns columns to user to choose on of them for visualisation
    print("Spaltenübersicht: ")
    for i, column in enumerate(data[0]):
        print(f"{i + 1}. {column}")
    try:
        column_index = int(input("Welche Spalte möchten Sie visualisieren (Nummer eingeben)? ")) - 1
        if 0 <= column_index < len(data[0]):
            return column_index
        print("Ungültige Auswahl!")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")
    return None


def visualizer(data):
    # Visualises data from a CSV file
    print("Möchten Sie die Daten visualisieren?")
    if input("(J/N):").lower() != YES_OPTION:
        return

    # Dateipfad vom Benutzer abfragen
    while True:
        filepath = input("Bitte geben Sie den Dateipfad zur CSV-Datei an: ").strip()
        if os.path.exists(filepath):
            data = read_csv_file(filepath)
            if data:
                break
        print(f"Die Datei '{filepath}' wurde nicht gefunden. Bitte versuchen Sie es erneut.")

    # Visualisierungstyp auswählen
    while True:
        print("Wählen Sie den Typ der Visualisierung aus:")
        choice = input("1. Kuchendiagramm 2. Balkendiagramm").strip()
        if choice in VISUALIZATION_TYPES:
            globals()[VISUALIZATION_TYPES[choice]](data)
            print(f"{VISUALIZATION_TYPES[choice].replace('_', ' ').capitalize()} wurde erfolgreich erstellt.")
            break
        print("Ungültige Auswahl. Bitte geben Sie eine Zahl zwischen 1 und 2 ein.")


def pie_chart(data):
    #Creating a pie chart according to users input
    column_index = get_column_selection(data)
    if column_index is None:
        return
    try:
        labels = list(set(row[column_index] for row in data[1:] if row[column_index].strip()))
        sizes = [sum(1 for row in data[1:] if row[column_index] == label) for label in labels]
        if not labels or not sizes:
            print("Keine Daten oder unvollständige Spalte!")
            return
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.title(f"Kuchendiagramm: {data[0][column_index]}")
        plt.axis('equal')
        plt.show()
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def bar_chart(data):
    # Creating a bar chart according to user input
    column_index = get_column_selection(data)
    if column_index is None:
        return
    try:
        labels = list(set(row[column_index] for row in data[1:] if row[column_index].strip()))
        frequencies = [sum(1 for row in data[1:] if row[column_index] == label) for label in labels]
        if not labels or not frequencies:
            print("Keine Daten oder unvollständige Spalte!")
            return
        plt.bar(labels, frequencies)
        plt.title(f"Balkendiagramm: {data[0][column_index]}")
        plt.xlabel(data[0][column_index])
        plt.ylabel("Häufigkeit")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
