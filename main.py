# Morse code intrepretor
# disctionary nisi of morse code , google  e gelei paabi


TEXT_MORSE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def text_to_morse(text):
    Morse_code = ""  # morse code ta jeikhane store hobe sheita

    for char in text.upper():  # looping text.upper cuz choto boro input dileo boro ta dhorei kaaj korbe
        if char in TEXT_MORSE_DICT:
            Morse_code += TEXT_MORSE_DICT[char] + " "  # wil check if  char is in morse code  #char is characer variable

        else:
            Morse_code += char + " "

    return Morse_code.strip()


# User_input = input("Enter your text :").split() #
# print("MOrse code ", text_to_morse(User_input))


MORSE_TEXT_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                   '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                   '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                   '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                   '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                   '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
                   '-....-': '-', '-.--.': '(', '-.--.-': ')'}


def morse_to_text(morse):
    Text_code = ""
    morse = morse.split()
    for mar in morse:
        if mar in MORSE_TEXT_DICT:
            Text_code += MORSE_TEXT_DICT[mar] + ""
        else:
            Text_code += mar + ""
    return Text_code.strip()


# User_input = input("Enter your morse :").split()
# print("Text code ", morse_to_text(User_input))

print("1 -  text  to Morse ,\n2 -  Morse To Text ", )

option = input("choose 1 or 2 : ")
option = option.strip()
if option == "1" or option == "2":
    text = input("enter the text :")
    if option == "1":
        output = text_to_morse(text)
        print(output)
    elif option == "2":
        output = morse_to_text(text)
        print(output)



