import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # get 4-ngram words
    ngram_words = words[:4]
    # create 4-ngram string
    ngram = " ".join(ngram_words)

    print '%s\t%s' % (ngram, 1)
