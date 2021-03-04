import pandas as pd
import csv
import io
import numpy as np

def makeCorpus(file):
    df = pd.read_csv(file)
    # windows-1252 encoding
    with open('data/corpus.txt', 'w', encoding="utf-8") as f:
        np.savetxt(f, df['text'], fmt="%s", delimiter='/n')
    f.close()
    return 0

if __name__ == "__main__":
    makeCorpus("source_tweets.csv")