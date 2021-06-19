# COMP472_Assignment_2
COMP472_Assignment_2

### pip install list
```
pip install -U scikit-learn
pip install pyyaml
pip install requests
pip install beautifulsoup4
pip install pandas
```

### Training and testing set
- Training and testing dataset are based on TV series "Prison Break" season 1 - 5
- We scrap the reviews under each episodes from season 1 - 5
- First. we classify the reviews into positive and negative reviews
- Second. we parse them in different yaml files
- Third. we pick odd number of reviews in different yaml files as trainning set and even number of reviews as testing set

### Remove list (stop_word)
- Original stopword.txt from moodle
- All the numbers with low probility considerd as noise
- TO ADD:
    - None english word
    - Random typing

### TODO
- Optimal task 1.3 (3 for loop overlap)
    - Create dictionary for check prob value
    - Or yaml file to store prob value with yaml search function