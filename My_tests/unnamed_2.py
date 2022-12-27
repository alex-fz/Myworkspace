#!/usr/bin/env python3


#Dict comprehension

def main_comprehension():

    dict_compressed = {key:value for key, value in enume:rate(range(1,10))}
    return dict_compressed


if __name__ == "__main__":
    print(main_comprehension())
