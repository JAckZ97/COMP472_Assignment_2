# -------------------------------------------------------
# Assignment 2
# Written by Zejun Zhang (40021402)
# For COMP 472 Section AI-X – Summer 2021
# Team: Sonic_1
# --------------------------------------------------------

from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import yaml

# ---------------- Fetch data to create data.csv ----------------
# Lists to store the scraped data in
ep_names = []
ep_season_list = []
ep_review_link_list = []
ep_year = []
ep_season = ['1', '2', '3', '4', '5']
url = 'https://www.imdb.com/title/tt0455275/episodes?season='

for x in ep_season:
    # Get season 1 to 5 url
    response = get(url + x)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_ = 'info')

    for i in range(0, len(movie_containers)):
        split_time = []

        # Get episode name
        ep_names.append(movie_containers[i].strong.a.text)
        # Get each season number for different episode
        ep_season_list.append(x)
        # Get episode reviews link
        ep_review_link_list.append('https://www.imdb.com' + movie_containers[i].strong.a['href'] + 'reviews')
        # Get episode year
        split_time = movie_containers[i].find('div', class_ = 'airdate').text.split()
        ep_year.append(split_time[2])

df = pd.DataFrame({
    'Name': ep_names,
    'Season': ep_season_list,
    'Review Link': ep_review_link_list,
    'Year': ep_year
})
# Create data.csv file
df.to_csv('data.csv')
# ---------------------------------------------------------------


# -------------- Parse user reviews into yaml file --------------
'''
Structure of the database:
Reviews:
    count:
        score: 9
        p/n: Positive
        text: default
'''
count = 0
count1 = 0
ep_review_link_list_new = []

# Load reveiw link list to a new list
rd = pd.read_csv('data.csv')
ep_review_link_list_new = rd['Review Link'].tolist()

for i in ep_review_link_list_new:
    response = get(i)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_ = 'imdb-user-review')

    for j in movie_containers:
        try:
            review_text = j.find('div', class_ = 'text').text
            score = j.find('span', class_ = 'rating-other-user-rating').span.text

            if int(score) >= 8:
                with open('PositiveReviewSet.yaml','r') as yamlfile:
                    databaseUpdate = yaml.safe_load(yamlfile) # Note the safe_load
                    databaseUpdate['Reviews'].update({hash(review_text): {'count':count, 'score':score, 'p/n':'Positive', 'text':review_text}})
                    count += 1

                if databaseUpdate:
                    with open('PositiveReviewSet.yaml','w') as yamlfile:
                        yaml.safe_dump(databaseUpdate, yamlfile) # Also note the safe_dump
            
            if int(score) < 8:
                with open('NegativeReviewSet.yaml','r') as yamlfile:
                    databaseUpdate = yaml.safe_load(yamlfile) # Note the safe_load
                    databaseUpdate['Reviews'].update({hash(review_text): {'count':count1, 'score':score, 'p/n':'Negative', 'text':review_text}})
                    count1 += 1

                if databaseUpdate:
                    with open('NegativeReviewSet.yaml','w') as yamlfile:
                        yaml.safe_dump(databaseUpdate, yamlfile) # Also note the safe_dump
        except:
            pass
# ---------------------------------------------------------------


# -------- Devide the reviews into training and test set --------
# Move half of positive review set to training set and the other half to testing set
with open('PositiveReviewSet.yaml','r') as yamlfile:
    database = yaml.safe_load(yamlfile) 
    for k, v in database['Reviews'].items():

        # Even count number of reviews move to TESTING set
        if database['Reviews'][k]["count"] % 2 == 0:
            with open('TestingReviewSet.yaml','r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) 
                databaseUpdate['Reviews'].update({k : v})

            if databaseUpdate:
                with open('TestingReviewSet.yaml','w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) 

        # Odd count number of reviews move to TRAINING set
        if database['Reviews'][k]["count"] % 2 == 1:
            with open('TrainingReviewSet.yaml','r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) 
                databaseUpdate['Reviews'].update({k : v})

            if databaseUpdate:
                with open('TrainingReviewSet.yaml','w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) 

# Same thing for negative review set
with open('NegativeReviewSet.yaml','r') as yamlfile:
    database = yaml.safe_load(yamlfile) 
    for k, v in database['Reviews'].items():

        if database['Reviews'][k]["count"] % 2 == 0:
            with open('TestingReviewSet.yaml','r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) 
                databaseUpdate['Reviews'].update({k : v})

            if databaseUpdate:
                with open('TestingReviewSet.yaml','w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) 

        if database['Reviews'][k]["count"] % 2 == 1:
            with open('TrainingReviewSet.yaml','r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) 
                databaseUpdate['Reviews'].update({k : v})

            if databaseUpdate:
                with open('TrainingReviewSet.yaml','w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) 
# ---------------------------------------------------------------
