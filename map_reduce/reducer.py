from operator import itemgetter
import sys

current_ngram = None
current_count = 0
ngram = None

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
            print '%s\t%s' % (current_ngram, current_count)
        current_count = count
        current_ngram = ngram

# do not forget to output the last ngram if needed!
if current_ngram == ngram:
    print '%s\t%s' % (current_ngram, current_count)
