import yaml
import math
import numpy as np
import enchant
from sklearn.feature_extraction.text import CountVectorizer

# ---------------- Tokenlize trainning data set -----------------
corpus_positive = []
corpus_negative = []
corpus = []
tokenlize_list_positive = []
tokenlize_list_negative = []
tokenlize_list = []
stop_list = []
remove_list = []

# Load reviews
with open('TrainingReviewSet.yaml','r') as yamlfile:
# with open('t1.yaml','r') as yamlfile:
    database = yaml.safe_load(yamlfile) 
    for k, v in database['Reviews'].items():
        # Append positive reviews in a list
        if database['Reviews'][k]["p/n"] == "Positive":
            if database['Reviews'][k]["text"] != "default":
                corpus_positive.append(database['Reviews'][k]["text"])

        # Append negative reviews in a list
        if database['Reviews'][k]["p/n"] == "Negative":
            if database['Reviews'][k]["text"] != "default":
                corpus_negative.append(database['Reviews'][k]["text"])

        # Append all reviews in a list
        corpus.append(database['Reviews'][k]["text"])

# Load remove.txt into a list
with open("remove.txt", "r") as remove:
    content = remove.read() 
    stop_list = content.split()
    remove.close()

# Convert to lowercase and tokenlize the words
vectorizer_p = CountVectorizer(stop_words = stop_list)
vectorizer_n = CountVectorizer(stop_words = stop_list)
vectorizer = CountVectorizer(stop_words = stop_list)

token_p = vectorizer_p.fit_transform(corpus_positive)
token_n = vectorizer_n.fit_transform(corpus_negative)
token = vectorizer.fit_transform(corpus)

# words list
tokenlize_list_positive = vectorizer_p.get_feature_names()
tokenlize_list_negative = vectorizer_n.get_feature_names()
tokenlize_list = vectorizer.get_feature_names()

# Get the frequency for each words in training set
frequency_list_p = token_p.toarray()
frequency_list_n = token_n.toarray()

# frequency list
frequency_p = frequency_list_p.sum(axis=0)
frequency_n = frequency_list_n.sum(axis=0)
# for x in range(100):
#     print(tokenlize_list[x])
# print(tokenlize_list)
# ---------------------------------------------------------------

# # --------------------- Update stopword.txt ---------------------
# # We try to remove none english word, random typing and all the numbers with low probility
# english_check = enchant.Dict("en_US")

# for x in tokenlize_list:
#     if not english_check.check(x):
#         remove_list.append(x)

# # Load remove_list to a temp file
# with open('remove.txt', 'a') as remove2:
#     for item in remove_list:
#         try:
#             remove2.write("%s\n" % item)
#         except:
#             pass
#     remove2.close()
# # ---------------------------------------------------------------

# ------ Compute conditional probility with smooth of 1 ---------
wordsCount = 1

with open('model.txt', 'w') as model:
    for x in range(0, len(tokenlize_list_positive)):
        # Word only in positive reviews but not in negative reviews
        if tokenlize_list_positive[x] not in tokenlize_list_negative:
            prob_positive : float = 0.0
            prob_negative : float = 0.0

            prob_positive = (frequency_p[x] + 1)/(len(tokenlize_list_positive) + len(tokenlize_list))
            prob_negative = 1/(len(tokenlize_list_negative) + len(tokenlize_list))
            
            try:
                model.write("No.%d %s\n" % (wordsCount,tokenlize_list_positive[x]))
                model.write(str(frequency_p[x]) + ", " + str(prob_positive) + ", " + 
                            str(0) + ", " + str(prob_negative) + "\n")
                wordsCount += 1
            except:
                pass
    
    for y in range(0, len(tokenlize_list_negative)):
        # Word only in negative reviews but not in positive reviews
        if tokenlize_list_negative[y] not in tokenlize_list_positive:
            prob_positive : float = 0.0
            prob_negative : float = 0.0

            prob_positive = 1/(len(tokenlize_list_positive) + len(tokenlize_list))
            prob_negative = (frequency_n[y] + 1)/(len(tokenlize_list_negative) + len(tokenlize_list))
            
            try:
                model.write("No.%d %s\n" % (wordsCount,tokenlize_list_negative[y]))
                model.write(str(0) + ", " + str(prob_positive) + ", " + 
                            str(frequency_n[y]) + ", " + str(prob_negative) + "\n")
                wordsCount += 1
            except:
                pass

    for x in range(0, len(tokenlize_list_positive)):
        for y in range(0, len(tokenlize_list_negative)):
            # Word both have in positive reviews and negative reviews
            if tokenlize_list_positive[x] == tokenlize_list_negative[y]:
                prob_positive : float = 0.0
                prob_negative : float = 0.0

                prob_positive = (frequency_p[x] + 1)/(len(tokenlize_list_positive) + len(tokenlize_list))
                prob_negative = (frequency_n[y] + 1)/(len(tokenlize_list_negative) + len(tokenlize_list))
                
                model.write("No.%d %s\n" % (wordsCount,tokenlize_list_positive[x]))
                model.write(str(frequency_p[x]) + ", " + str(prob_positive) + ", " + 
                            str(frequency_n[y]) + ", " + str(prob_negative) + "\n")
                wordsCount += 1

    model.close()
# ---------------------------------------------------------------