#!/usr/bin/env python3
'''
Advent of Code: 2017, Day 15

Serial implementation
'''
import random


def generator_a(start):
    return (start * 16807) % 2147483647


def generator_b(start):
    return (start * 48271) % 2147483647


def judge(gen_a_num, gen_b_num):
    return 0


def main():
    '''
    Main function. This is where all the magic happens.
    '''
    random_range = 40000
    judge_range = 40000000
    match_total = 0
    #generator_a_start = random.randrange(random_range)
    #generator_b_start = random.randrange(random_range)
    generator_a_num = 65
    generator_b_num = 8921

    for i in range(judge_range):
        generator_a_num = generator_a(generator_a_num)
        generator_b_num = generator_b(generator_b_num)
        if judge(generator_a_num, generator_b_num) == 1:
            match_total += 1

    return 0


if __name__ == '__main__':
    main()
