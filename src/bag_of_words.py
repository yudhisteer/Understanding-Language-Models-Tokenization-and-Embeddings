




def split_sentence(sentence: str) -> list[str]:
    """
    Split a sentence into words
    """
    return sentence.split()



def create_vocab(sentence_words: list[str]) -> set[str]:
    """
    Create a vocabulary from a list of words
    """
    return set(sentence_words)


def bag_of_words(sentence_words: list[str], vocab: set[str]) -> list[int]:
    """
    Create a bag of words from a list of words and a vocabulary
    """
    return [sentence_words.count(word) for word in vocab]





if __name__ == "__main__":

    # Load the data
    data = """Coding became my passion. 
    I love programming in Python daily, yet remain oddly scared of actual python snakes in zoos."""

    sentence_1 = "I love programming in Python"
    sentence_2 = "I am scared of python snakes"

    sentence_1_words = split_sentence(sentence_1)
    sentence_2_words = split_sentence(sentence_2)

    print("Sentence 1 words:", sentence_1_words)
    print("Sentence 2 words:", sentence_2_words)

    # Create a vocabulary from the data
    vocab_split = split_sentence(data)
    vocab = create_vocab(vocab_split)
    print("Vocabulary:", vocab)

    # Create a bag of words from the data
    bag_of_words_sentence_1 = bag_of_words(sentence_1_words, vocab)
    bag_of_words_sentence_2 = bag_of_words(sentence_2_words, vocab)
    print("Bag of words for sentence 1:", bag_of_words_sentence_1)
    print("Bag of words for sentence 2:", bag_of_words_sentence_2)
