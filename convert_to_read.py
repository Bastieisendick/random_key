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


def convert_chunk(chunk_key,chunk_text):
    for key,character in zip(chunk_key,chunk_text):
        char_int=ordin(str(character))
        key_int=ordin(str(key))
        conv_int=int(char_int)+int(key_int)
        if(int(conv_int)>=len_pos_char_list):
            conv_int=int(conv_int)-len_pos_char_list
        with open("data/output_text.txt", 'a', encoding="utf-8") as output_f:
            output_f.write(str(chrc(conv_int)))




def main():
    with open("data/output_text.txt", 'w') as output_f:
        output_f.write("")

    with open("data/converted_text.txt", encoding="utf-8") as c_f:
        with open("data/key_text.txt", encoding="utf-8") as key_f:
            for chunk_key,chunk_text in zip(iter(lambda: key_f.read(200), ""),iter(lambda: c_f.read(200), "")):
                convert_chunk(chunk_key,chunk_text)
main()
