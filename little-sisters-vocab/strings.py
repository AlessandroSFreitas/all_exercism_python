def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return f"un{word}"


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    all_new_words = []

    for word in vocab_words[1:]:
        new_word = f"{vocab_words[0]}{word}"
        all_new_words.append(new_word)

    new_list = []

    for i in all_new_words:
        if not i == all_new_words[-1]:
            new_list.append(f"{i} :: ")

    new_string = ""

    for i in new_list:
        new_string = new_string + i

    return f"{vocab_words[0]} :: " + new_string + all_new_words[-1]


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    if word.endswith("iness"):
        new_word = word.replace("iness", "y")
        return new_word

    if word.endswith("ness"):
        new_word = word.replace("ness", "")
        return new_word



def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    split_sentence = sentence.split(" ")

    new_sentence = split_sentence[index]

    sentence_replaced = new_sentence.replace(".", "")

    return sentence_replaced + "en"
