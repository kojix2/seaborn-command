import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delimiter", help="delimiter", default='\t')
    parser.add_argument("-x", help="X")
    parser.add_argument("-y", help="Y")
    parser.add_argument("--format", help="outout image file format")
    parser.add_argument("--show", help="call plt.show()", action='store_true')
    args = parser.parse_args()
    
    df = pd.read_csv(sys.stdin, sep=args.delimiter)
    sns.pairplot(df, hue="species")
    if args.show:
      plt.show()
    else:
      plt.savefig(sys.stdout.buffer, format=args.format)