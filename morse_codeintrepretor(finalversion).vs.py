"""
#Morse code intrepretor
#disctionary nisi of morse code , google  e gelei paabi 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def text_to_morse(text):
    Morse_code = ""  # morse code ta jeikhane store hobe sheita

    for char in text.upper(): # looping text.upper cuz choto boro input dileo boro ta dhorei kaaj korbe
        if char in MORSE_CODE_DICT:
            Morse_code += MORSE_CODE_DICT[char] + " " # wil check if  char is in morse code  #char is characer variable
        
        else:
            Morse_code += char + " "

    return Morse_code.strip()

User_input = input("Enter your text :").split()
print("MOrse code ", text_to_morse(User_input))

"""
MORSE_CODE_DICT2 = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
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

    for mar in morse:
        if mar in MORSE_CODE_DICT2:
            Text_code += MORSE_CODE_DICT2[mar] + ""
        else:
            Text_code += mar + ""
    return Text_code.strip()


User_input = input("Enter your morse :").split()
print("Text code ", morse_to_text(User_input))
