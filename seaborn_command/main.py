import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


def parse_seaborn_args(args):
    seaborn_args = {}
    for arg in args:
        if arg.startswith("--"):
            opt = arg[2:]
        else:
            seaborn_args[opt] = arg
    return seaborn_args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plot", help="subcommand")
    parser.add_argument("-d", "--delimiter", help="delimiter", default="\t")
    parser.add_argument("--format", help="outout image file format", default="svg")
    parser.add_argument("--show", help="call plt.show()", action="store_true")
    parser.add_argument("--debug", help="print seaborn args", action="store_true")
    args, unknown_args = parser.parse_known_args()

    seaborn_args = parse_seaborn_args(unknown_args)

    if args.debug:
        print(seaborn_args)

    df = pd.read_csv(sys.stdin, sep=args.delimiter)
    getattr(seaborn, args.plot)(data=df, **seaborn_args)

    if args.show:
        plt.show()
    else:
        plt.savefig(sys.stdout.buffer, format=args.format)
