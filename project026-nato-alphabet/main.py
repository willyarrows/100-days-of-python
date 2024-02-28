import pandas as pd

df_nato = pd.read_csv("nato_phonetic_alphabet.csv")
dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}

input_word = input("Enter a word : ").upper()
nato_alphabet = [dict_nato[alphabet] for alphabet in input_word]
print(nato_alphabet)

