PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file_invited_names:
    invited_names = file_invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as file_starting_letter:
    letter_content = file_starting_letter.read()

for names in invited_names:
    names = names.strip()
    with open(f"./Output/ReadyToSend/letter_to_{names}.txt", mode="a") as file_ready_to_send:
        letter_content_to_send = letter_content.replace(PLACEHOLDER, names)
        file_ready_to_send.write(letter_content_to_send)
