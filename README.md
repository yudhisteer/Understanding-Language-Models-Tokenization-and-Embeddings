# Understanding-Language-Models-Tokenization-and-Embeddings

## Plan of Action
1. [Word Vectors](#word-vectors)
2. Tokens and Embeddings
3. 






----------------------------------------
<a id="word-vectors"></a>
## 1. Word Vectors
Earlier on we used to represent unstructred text as a **bag-of-words**. Suppose we have the following sentences from which we want to create a **vocabulary**. 

```python
data = """Coding became my passion. 
I love programming in Python daily, yet remain oddly scared of actual python snakes in zoos."""
```

Our first step would be **tokenization** which is nothing but splitting the sentences into words or sub-words (tokens). Now there are various methods of tokenization but the simplest one is to split by whitespace.


```python
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
```

We create a vocabulary from the list of words.

```python
Vocabulary: {'programming', 'python', 'became', 'Coding', 'scared', 'oddly', 'actual', 'snakes', 'in', 'zoos.', 'love', 'I', 'my', 'of', 'Python', 'yet', 'remain', 'daily,', 'passion.'}
```

Now if we have an input sentence, we can create a bag-of-words from it.

```python
sentence_1 = "I love programming in Python"
sentence_2 = "I am scared of python snakes"
```

From the sentences above, we count how often each word appears in the vocabulary. Notice how we went from representing out sentences made of words to representing it to a **vector** of numbers also known as **vector representations**.

```python
Bag of words for sentence 1: [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
Bag of words for sentence 2: [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
```

The drawback is that we have lost **semantic representation** of the words.






















---------------------------------------------

## References
1. https://www.youtube.com/watch?v=rmVRLeJRkl4&list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4
2. https://web.stanford.edu/class/cs224n/
3. https://github.com/HandsOnLLM
4. https://github.com/aburkov/theLMbook
5. 