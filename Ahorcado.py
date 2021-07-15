#! /usr/bin/env python3


def guess():
    letter = input("Ingresa la letra que quieres probar: ")
    guesses.append(letter)
    return letter

def jugarDeNuevo():
    rta = input("Querés jugar de nuevo? (S/N): ").lower()
    if rta == 's':
        return [[], [], '', [], 0, True]
    elif rta == 'n':
        return [[], [], '', [], 0, False]
    elif len(rta) > 1:
        print('Tu respuesta debe ser "S" o "N"')
        jugarDeNuevo()
    else: 
        print("Disculpá, no entendí tu rta.")
        jugarDeNuevo()


wordLetters = []
hiddenLettersList = []
hiddenLetters = ''
guesses = []
attempts = 0
jugar = True

while jugar == True:

    word = input("Ingresa la palabra que quieres que adivinen: ")

    for i in word:
        wordLetters.append(i)
        hiddenLetters += "_ "
        hiddenLettersList.append(i)
    print("\n\nTenés 7 intentos para tratar de adivinar todas las letras de la palabra escondida.")
    print(hiddenLetters)
    print(wordLetters)

    while "_ " in hiddenLetters and attempts < 7:
        letter = guess()
        if letter not in wordLetters:
            attempts += 1
        hiddenLetters = ""
        for i in wordLetters:
            if i not in guesses:
                hiddenLetters += "_ "
            else: hiddenLetters += i
        print(hiddenLetters)
        if 7-attempts > 0 and "_ " in hiddenLetters:
            print(f'Te quedan {7 - attempts} intentos')

    if attempts == 7:
        print("No adivinaste la palabra. Mas suerte la proxima!")
    else:
        print(f"Felicitaciones! Adivinaste la palabra '{word}'!")
    
    vals = jugarDeNuevo()

    wordLetters = vals[0]
    hiddenLettersList = vals[1]
    hiddenLetters = vals[2]
    guesses = vals[3]
    attempts = vals[4]
    jugar = vals[5]

print('Gracias por jugar!\nNos vemos la próxima!')




