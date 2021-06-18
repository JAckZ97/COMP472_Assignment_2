import yaml
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count_positive = 0
count_negative = 0
prob_positive : float = 0.0
prob_negative : float = 0.0
prob_word_positive : float = 0.0
prob_word_negative : float = 0.0
corpus = []
tokenlize_list = []
count_right = 0
count_wrong = 0
prediction_of_correctness : float = 0.0
item_list = [[]]

# ------- Get probility of potive and negative in reviews -------
# with open('TrainingReviewSet.yaml','r') as yamlfile:
with open('t1.yaml','r') as yamlfile:
    database = yaml.safe_load(yamlfile) 
    for k, v in database['Reviews'].items():

        if database['Reviews'][k]["p/n"] == "Positive":
            count_positive += 1
        
        if database['Reviews'][k]["p/n"] == "Negative":
            count_negative += 1

prob_positive = count_positive / (count_positive + count_negative)
prob_negative = count_negative / (count_positive + count_negative)
# ---------------------------------------------------------------


# ----------------- Tokenlize testing data set ------------------
# Get P(ri|positive) and P(ri|negative) and load it into result.txt
# with open('TestingReviewSet.yaml','r') as yamlfile:
with open('t2.yaml','r') as yamlfile:
    database = yaml.safe_load(yamlfile) 
    for k, v in database['Reviews'].items():
        # Append all reviews in a list
        corpus.append(database['Reviews'][k]["text"])

vectorizer = CountVectorizer()
token = vectorizer.fit_transform(corpus)
# words list
tokenlize_list = vectorizer.get_feature_names()
# frequency list
frequency_list = token.toarray()
# ---------------------------------------------------------------


# ----------------- Load model.txt into a list ------------------
# Count total line number of model.txt
with open("model2.txt", "r") as line_count:
    lineCount = 0
    for line in line_count:
        if line != "\n":
            lineCount += 1
    line_count.close()

# Load model.txt into a list
count = 0
with open("model2.txt", "r") as model:
    for count, line in enumerate(model):
        temp_list = []

        if count % 2 == 0:
            content = line.rstrip()
            s = content.split()
            print(s)
            temp_list.append(s[1])
            count += 1

        elif count % 2 == 1:
            content = line.rstrip()
            z = content.split(", ")
            print(z)
            temp_list.append(z[1])
            temp_list.append(z[3])
            count += 1

        item_list.append(temp_list)
    item_list.pop(0)
    # print(item_list)

    model.close()
# ---------------------------------------------------------------

