from operator import itemgetter
import sys
import csv

current_ngram = None
current_count = 0
ngram = None

with open('pregunta1.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["ngram","count"])
    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        ngram, count = line.split('\t', 1)

        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: ngram) before it is passed to the reducer
        if current_ngram == ngram:
            current_count += count
        else:
            if current_ngram:
                # write result to STDOUT
                writer.writerow([current_ngram, current_count])
            current_count = count
            current_ngram = ngram
