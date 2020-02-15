
import random
possible_char=[]
with open("data/character.lst","r") as l_f:
           file_value= l_f.read()
for char in file_value:
    possible_char.append(char)

len_pos_char_list=int(len(possible_char))


def chrc(integer):
    value=possible_char[int(integer)]
    return value

def ordin(string):
    value=possible_char.index(str(string))
    return value

def return_randomint(not_take_value):
    randomint=random.randrange(0, len_pos_char_list)
    while int(randomint)==int(not_take_value):
        randomint=random.randrange(0, len_pos_char_list)
    return randomint

def convert_chunk(value_text):
    c_file_value=""
    key_file_value=""
    for character in value_text:
        char_int=ordin(str(character))
        key_int=return_randomint(char_int)
        conv_int=int(char_int)-int(key_int)
        c_file_value=c_file_value+chrc(conv_int)
        key_file_value=key_file_value+chrc(key_int)
    with open("data/converted_text.txt", 'a', encoding="utf-8") as c_f:
        c_f.write(c_file_value)
    with open("data/key_text.txt", 'a', encoding="utf-8") as key_f:
        key_f.write(key_file_value)




def main():
    with open("data/converted_text.txt", 'w') as c_f:
        c_f.write("")
    with open("data/key_text.txt", 'w') as key_f:
       key_f.write("")

    with open("data/text_to_convert.txt", encoding="utf-8") as nc_f:
        for chunk in iter(lambda: nc_f.read(200), ""):
            convert_chunk(chunk)
            print("Hier  ")
main()
