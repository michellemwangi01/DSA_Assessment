# Dictionaries:

# Question 3: Implement a function word_frequency(sentence) that takes
# a sentence and returns a dictionary containing the frequency of each
# word in the sentence.

# Ignore punctuation and consider words in a case-insensitive manner.

# sample input =

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)

print("-------------------------------------------------------------------")


def word_frequency(sentence):
    frequency_dict = {}
    for word in sentence.lower().replace(".", "").split(" "):
        if word not in frequency_dict.keys():
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    print(frequency_dict)


word_frequency("This is a test sentence. This sentence is a test. with a")
