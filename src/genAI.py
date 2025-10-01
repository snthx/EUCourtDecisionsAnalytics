import os
import json

ai_setup = False
username = None
password = None

# Might be not working without object oriented approach ==> TODO, Handbuch S. 179 f.
def setupAI():
    global ai_setup, username, password
    # Definiere den Pfad zur Datei mit den Anmeldeinformationen
    ai_config = '../data/ai_config_file.json'  # Ändere den Dateinamen nach Bedarf

    # Überprüfe, ob die Datei vorhanden ist
    if not os.path.exists(ai_config):
        raise FileNotFoundError(f"Die Datei '{ai_config}' wurde nicht gefunden. Bitte stelle sicher, dass die Datei vorhanden ist.")

    # Lade die Anmeldeinformationen aus der Datei
    with open(ai_config, 'r') as file:
        credentials = json.load(file)
        username = credentials.get('username')
        password = credentials.get('password')

    # Überprüfe, ob Benutzername und Passwort vorhanden sind
    if not username or not password:
        raise ValueError("Benutzername oder Passwort fehlen in der Anmeldeinformationsdatei.")

    ai_setup = True
    print("Setting up AI environment...")
   
    # Maybe add test call to check if credentials are valid TODO

def runPrompt(prompt):
    if not ai_setup:
        raise RuntimeError("AI environment is not set up. Please call setupAI() first.")
    
    print(f"Running prompt: {prompt}")
    return "Prompt result"