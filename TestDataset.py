import yaml
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count_positive = 0
count_negative = 0
prob_positive : float = 0.0
prob_negative : float = 0.0
corpus = []
tokenlize_list = []
count_right = 0
count_wrong = 0
prediction_of_correctness : float = 0.0
item_list = [[]]
result_list = []

# ------- Get probility of potive and negative in reviews -------
with open('TrainingReviewSet.yaml','r') as yamlfile:
# with open('t1.yaml','r') as yamlfile:
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
with open('TestingReviewSet.yaml','r') as yamlfile1:
# with open('t2.yaml','r') as yamlfile1:
    database = yaml.safe_load(yamlfile1) 
    for k, v in database['Reviews'].items():
        # Append all reviews in a list
        corpus.append(database['Reviews'][k]["text"])
        result_list.append(database['Reviews'][k]["p/n"])

vectorizer = CountVectorizer()
token = vectorizer.fit_transform(corpus)
# words list
tokenlize_list = vectorizer.get_feature_names()
# frequency list
frequency_list = token.toarray()
# ---------------------------------------------------------------


# ----------------- Load model.txt into a list ------------------
# # Count total line number of model.txt
# with open("model.txt", "r") as line_count:
#     lineCount = 0
#     for line in line_count:
#         if line != "\n":
#             lineCount += 1
#     line_count.close()

# Load model.txt into a list
count = 0
with open("model.txt", "r") as model:
    for count, line in enumerate(model):
        temp_list = []

        if count % 2 == 0:
            content = line.rstrip()
            s = content.split()
            temp_list.append(s[1])
            count += 1

        elif count % 2 == 1:
            content = line.rstrip()
            z = content.split(", ")
            temp_list.append(z[1])
            temp_list.append(z[3])
            count += 1

        item_list.append(temp_list)
    item_list.pop(0)
    model.close()
# ---------------------------------------------------------------


# Get P(ri|positive) and P(ri|negative) and load it into result.txt
reviewCount = 1
rightNum = 0
wrongNum = 0

with open('result.txt', 'w') as results:
    # Example: frequency_list = [[1 0 1 0 3][1 3 4 0 1]]
    for x in range(0, len(frequency_list)):
        prob_word_positive : float = 0.0
        prob_word_negative : float = 0.0
        for y in range(0, len(frequency_list[0])):
            # Example: [['brought'], ['0.2', '0.125'], ['spoilers'], ['0.2', '0.125']]
            for z in range(0, int(len(item_list)/2)):
                # if review have the training words
                if int(frequency_list[x][y]) > 0:

                    if item_list[2*z][0] == tokenlize_list[y]:

                        prob_word_positive += math.log10(float(item_list[2*z +1][0]))
                        prob_word_negative += math.log10(float(item_list[2*z +1][1]))
                        # print(prob_word_positive)
                        # print(prob_word_negative)

        prob_word_positive += math.log10(prob_positive)
        prob_word_negative += math.log10(prob_negative)
        
        if prob_positive >= prob_word_negative:
            result = "Positive"
        else:
            result = "Negative"

        if result == result_list[x]:
            correntness = "right"
            rightNum += 1
        else:
            correntness = "wrong"
            wrongNum += 1

        # print(prob_word_positive)
        # print(prob_word_negative)
        # print("======")

        try:
            results.write("No.%d -- %s\n" % (reviewCount,corpus[x]))
            results.write(str(prob_word_positive) + ", " + str(prob_word_negative) + ", " + 
                        result + ", " + result_list[x] + ", " + correntness + "\n")
            reviewCount += 1
        except:
            pass
        print(reviewCount-1)
    
    accuricy : float = rightNum / (rightNum + wrongNum)
    results.write("The prediction correctness is %f" % (accuricy) + "%\n")
    results.close()


