

# Gets the words from a text file
#   Parameters:
#      filename - name of the file (string)
#   Return values:
#      words - all the words from the file (list of strings)
def get_words(filename):
    f = open(filename, 'r')

    words = []

    for word in f.read().split():
        # Strip off all punctuation
        bare_word = word.strip('.,!?()')
        lower_word = bare_word.lower()
        words.append(lower_word)

    return words


def main():
    words = get_words('GreenEggsAndHam.txt')

    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    for word in counts:
        print(word, counts[word])


main()
