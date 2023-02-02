from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Engima import Enigma

# historical rotor settings
rotors = [Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", "I"), Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", "II"), Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", "III"), Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J", "IV"), Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z", "V")]

# historical reflector settings
reflectors = [Reflector("EJMZALYXVBWFCRQUONTSPIKHGD", "A"), Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", "B"), Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL", "C")]

# read the settings from the file
file = open("settings.txt", "r")
settings = file.readlines()
settings = [x.strip() for x in settings]
file.close()

# format the settings
plugboardSettings = list(settings[0].split(" "))
for reflector in reflectors:
    if reflector.name in settings[1]:
        reflectorSettings = reflector
rotorSettings = [rotor for rotor in rotors if rotor.name in settings[2].split(" ")]
rotorSettings.reverse()
ringSettings = tuple(map(int, settings[3].split(" ")))

# initialize keyboard and plugboard settings
KB = Keyboard()
PB = Plugboard(plugboardSettings)

# set enigma settings
enigma = Enigma(reflectorSettings, rotorSettings[0], rotorSettings[1], rotorSettings[2], PB, KB)
enigma.setRings(ringSettings)
enigma.setKey(settings[4])

# run the program
print("Welcome to the Enigma Machine!")
while(True):
    # take in the message to encipher and convert it to the proper format
    message = input("Please enter a message to encipher: ")
    message = message.upper()
    message = message.replace(" ", "")

    # print the enchiphered message
    print(enigma.encipherMessage(message))