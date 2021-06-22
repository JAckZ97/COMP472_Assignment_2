# COMP472_Assignment_2
COMP472_Assignment_2

### pip install list
```
pip install -U scikit-learn
pip install pyyaml
pip install requests
pip install beautifulsoup4
pip install pandas
pip install pyenchant
pip install matplotlib
pip install numpy
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
- None english word
- Random typing

### TODO
~~- Optimal task 1.3 (3 for loop overlap)~~  
~~- Create dictionary for check prob value~~  
~~- Or yaml file to store prob value with yaml search function~~  
~~- complete task 2.1 or 2.2 or 2.3 one of them~~  
~~- prepare README~~  
~~- maybe try task 2.1 if have time~~  
~~- prepare demo procedure (jupyter notebook)~~  
~~- Try everything before submit~~  