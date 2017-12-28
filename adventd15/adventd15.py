#!/usr/bin/env python3
'''
Advent of Code: 2017, Day 15

Serial implementation
'''
from libadventd15c import generator_a
from libadventd15c import generator_b
from libadventd15c import judge


def main():
    '''
    Main function. This is where all the magic happens.
    '''
    match_total = 0
    mask = 65535
    generator_a_num = 65
    generator_b_num = 8921

    for i in range(40000000):
        generator_a_num = generator_a(generator_a_num)
        generator_b_num = generator_b(generator_b_num)

        if judge(mask, generator_a_num, generator_b_num):
            match_total += 1

    print("Match Total: {}".format(match_total))

    return 0


if __name__ == '__main__':
    main()
