# name = ["Aang", "Zuko","Appa", "Katara", "Sokka", "Momo", "Uncle Iroh", "Toph"]

# for receiver in name:
#     with open(f'day24-automate_letter\letter_for_{receiver}.txt', "w") as file:
#         file.write(f"Dear {receiver}, \n\n You are invited to my birthday this Saturday.\n\n Hope you can make it! \n\n Charlie")
PLACEHOLDER = "[name]"

with open("day24-automate_letter/Input/Names/invited_names.txt", "r") as names_file :
    names = names_file.readlines()
    
with open("day24-automate_letter/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, strip_name)
        with open(f"day24-automate_letter/Output/letter_for_{strip_name}", "w") as new:
            new.write(f"{new_letter}")
        