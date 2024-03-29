import pandas as pd

df_nato = pd.read_csv("nato_phonetic_alphabet.csv")
dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}

is_exit = False
while not is_exit:
    input_word = input("Enter a word : ").upper()
    try:
        nato_alphabet = [dict_nato[alphabet] for alphabet in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_alphabet)
        is_exit = True


