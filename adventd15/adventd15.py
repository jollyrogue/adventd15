#!/usr/bin/env python3
'''
Advent of Code: 2017, Day 15

Serial implementation
'''
from libadventd15c import generator_calc_c


def generator_a(start):
    return generator_calc_c(start, 16807)


def generator_b(start):
    return generator_calc_c(start, 48271)


def judge(mask, gen_a_num, gen_b_num):
    if (gen_a_num & mask) == (gen_b_num & mask):
        return True
    else:
        return False


def main():
    '''
    Main function. This is where all the magic happens.
    '''
    match_total = 0
    mask = int('1111111111111111', 2)
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
