# -------------------------------------------------------
# Assignment 2
# Written by Zejun Zhang (40021402)
# For COMP 472 Section AI-X – Summer 2021
# Team: Sonic_1
# --------------------------------------------------------

import matplotlib.pyplot as plt

xCoor = ['baseline', 'rm_len_less_2', 'rm_len_less_4', 'rm_len_greater_9']
# yCoor as correctness_list
correctness_list = []

with open('Word_length_filtering/result_0.txt', 'r', encoding='utf-8') as result:
    lineList = result.readlines()
    lastLine = lineList[-1]
    last_line_split = lastLine.split()
    correctness_list.append(float(last_line_split[-2]))
    result.close()

with open('Word_length_filtering/result_2.txt', 'r', encoding='utf-8') as result2:
    lineList = result2.readlines()
    lastLine = lineList[-1]
    last_line_split = lastLine.split()
    correctness_list.append(float(last_line_split[-2]))
    result2.close()

with open('Word_length_filtering/result_4.txt', 'r', encoding='utf-8') as result4:
    lineList = result4.readlines()
    lastLine = lineList[-1]
    last_line_split = lastLine.split()
    correctness_list.append(float(last_line_split[-2]))
    result4.close()

with open('Word_length_filtering/result_9.txt', 'r', encoding='utf-8') as result9:
    lineList = result9.readlines()
    lastLine = lineList[-1]
    last_line_split = lastLine.split()
    correctness_list.append(float(last_line_split[-2]))
    result9.close()

plt.title('Word length filtering classifier')
plt.xlabel('Size of models')
plt.ylabel('Correctness of prediction')

# label number for each bar
def labelText(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height), xy = (rect.get_x() + rect.get_width() / 2, height),
                    xytext = (0, 3), textcoords = "offset points", ha = 'center', va= 'bottom')

bar = plt.bar(xCoor, correctness_list, label = "Percentage of accuricy")
labelText(bar)
plt.tight_layout()
plt.legend()
plt.ylim(ymax=1)

plt.savefig("Word_length_filtering/Correctness_plot.png")
plt.show()