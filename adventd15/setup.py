from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "Advent of Code: Day 15",
    ext_modules = cythonize("libadventd15c.pyx"),
)
