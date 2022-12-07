#!/usr/bin/env python
from unittest import main
from movies import TMDB

if __name__ == "__main__":
    print("Some loved movies".strip().upper().center(40, "*"))
    print(str(TMDB(333339)).strip().center(40))
    print(str(TMDB(105)).strip().center(40))
    print(str(TMDB(602)).strip().center(40))
    print("".center(40, "*"))

    main(module="tests", exit=False)
