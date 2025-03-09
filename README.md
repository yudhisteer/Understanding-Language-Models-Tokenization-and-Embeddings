# Understanding-Language-Models-Tokenization-and-Embeddings

## Plan of Action
1. [Word Vectors](#word-vectors)
2. Tokens and Embeddings
3. 






----------------------------------------
<a id="word-vectors"></a>
## 1. Word Vectors

### 1.1 Bag-of-Words

Earlier on we used to represent unstructred text as a **bag-of-words**. Suppose we have the following sentences from which we want to create a **vocabulary**. 

```python
data = """Coding became my passion. 
I love programming in Python daily, yet remain oddly scared of actual python snakes in zoos."""
```

Our first step would be **tokenization** which is nothing but splitting the sentences into words or sub-words (tokens). Now there are various methods of tokenization but the simplest one is to split by whitespace creating a vocabulary.

```python
Vocabulary: {'programming', 'python', 'became', 'Coding', 'scared', 'oddly', 'actual', 'snakes', 'in', 'zoos.', 'love', 'I', 'my', 'of', 'Python', 'yet', 'remain', 'daily,', 'passion.'}
```

Now if we have an input sentence, we can create a bag-of-words from it.

```python
sentence_1 = "I love programming in Python"
sentence_2 = "I am scared of python snakes"
```

From the sentences above, we count how often each word appears in the vocabulary. Notice how we went from representing sentences made of words to representing as a **vector** also known as **vector representations**.

```python
Bag of words for sentence 1: [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
Bag of words for sentence 2: [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
```

The drawback is that we have lost **semantic representation** of the words.

### 1.2 Word Embeddings
In order to capture the meaning of the words, we can use **word2vec** which is a framework for learning **word embeddings**. word2vec uses a **neural network** to learn the embeddings.

*You shall know a word by the company it keeps ([Firth, J. R. 1957:11](https://en.wikipedia.org/wiki/John_Rupert_Firth))*

word2vec analyze which words tends to appear in the **neighborhood** of other words in a given sentence. Initially, we randomly initialized the vectors for every words then in the training process we look at pairs of words from the training data to predict if the words are likely to appear in the neighborhood of each other in a sentence. word2vec learns the **relationship between words** and this relationship is encoded in the vector representations - embeddings. For e.g, if two words tend to appear in the neighborhood of each other, their embeddings will be close to each other.


Notice how this differ from the bag-of-words concept where now we can use the embeddings to measure the semantic similarity between words.

Note:  

1. The term "embedding" refers to the fact that we are **encoding** aspects of a word's meaning in a **lower dimensional space**. This dimensionality reduction maintains semantic relationships; for instance, *doctor* and *hospital* will be closer than *doctor* and *dog*.

2. Bag-of-words creates embeddings at at the document level since it counts the frequency of words in the document. Whereas, word2vec creates embeddings for words only.


Now for words which have different meanings such as "bank", word2vec will create a static representations of that word irrespective of the context in which it is used. E.g, bank can refer to a financial institution or the side of a river. Which means that the word "bank" should have different embeddings for different contexts.






















---------------------------------------------

## References
1. https://www.youtube.com/watch?v=rmVRLeJRkl4&list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4
2. https://web.stanford.edu/class/cs224n/
3. https://github.com/HandsOnLLM
4. https://github.com/aburkov/theLMbook
5. 