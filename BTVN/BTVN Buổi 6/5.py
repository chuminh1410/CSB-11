def count_unique_words(sentence):
    word_list = sentence.split(' ')
    unique_words = set(word_list)
    return len(unique_words)

sentence = input("Write a sentence: ")

num_unique_words = count_unique_words(sentence)
print("Number of unique words:", num_unique_words)
