"""Corma, one time report to rule them all!"""


import argparse

# corma report test-dev -t 7h -d 2020-10-12
# corma report vacation
# corma submit bombardier -t 2020-09


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("register")
    parser.parse_args()
