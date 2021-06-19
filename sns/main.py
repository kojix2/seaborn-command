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
    args = parser.parse_args()
    
    df = pd.read_csv(sys.stdin, sep='\t')
    sns.pairplot(df, hue="species")
    plt.savefig(sys.stdout.buffer, format="svg")