import argparse
from yaml import load, SafeLoader

from bingo.bingo import BingoCard

def cli():
    parser = argparse.ArgumentParser(prog="bingo")
    parser.add_argument("config")

    args = parser.parse_args()

    with open(args.config, "r") as fp:
        cfg_dict = load(fp, Loader=SafeLoader)

    card = BingoCard(**cfg_dict)
    card.validate()

    card.get()
