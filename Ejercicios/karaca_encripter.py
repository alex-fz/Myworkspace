#!/usr/bin/env python3


'''aeiou == 01234 respectivamente'''

def encripter_des(text:str, encr:bool):
    
    kar_dict = {"a":"0", "e":"1", "i":"2", "o":"3", "u":"4"}
    
    if encr:
        new_text = ""
        for letter in text.lower():
            if letter in kar_dict.keys():
                new_text = new_text + kar_dict[letter]
            else:
                new_text = new_text + letter
        return new_text

    else:
        new_text = ""
        kar_values = list(kar_dict.values())
        kar_keys = list(kar_dict.keys())
        for letter in text.lower():
            try:
                index = kar_values.index(letter)
                new_text = new_text + kar_keys[index]
            except:
                new_text = new_text + letter

        return new_text
            


if __name__ == "__main__":
    print(encripter_des("1sp20 0m1r2c0n3 4 r4s3", False))
