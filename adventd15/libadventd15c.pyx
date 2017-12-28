cdef int generator_calc(int start, int factor):
    return (start * factor) % 2147483647


def generator_a(int start):
    return generator_calc(start, 16807)


def generator_b(int start):
    return generator_calc(start, 48271)
