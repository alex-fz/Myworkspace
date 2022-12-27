#!/usr/bin/env python3


#Dict comprehension

def main_comprehension():

    dict_compressed = {key:value for key, value in enumerate(range(1,10))}
    return dict_compressed


if __name__ == "__main__":
    result = main_comprehension()
    for k,v in result.items(): print("{} ... {}".format(k, v))

