1. Requirement libraries to run the program:

    pip install -U scikit-learn
    pip install pyyaml
    pip install requests
    pip install beautifulsoup4
    pip install pandas
    pip install pyenchant
    pip install matplotlib
    pip install numpy


2. Instruction for running the program
    
    2.1 Edit the url in "FetchImdbData.py" on line 20 to scrap the reviews under each episodes.
        By default, it will scrap the TV series "Prison Break" season 1 - 5
    
    2.2 Ignore the step 2.1 if already have the "data.csv" file. Comment out line 13 to 50 in "FetchImdbData.py" to start the program.
        It will update the "PositiveReviewSet.yaml" and "NegativeReviewSet.yaml" first as the temp file, 
        and then update the "TrainingReviewSet.yaml" and "TestingReviewSet.yaml" from those temp files.
    
    2.3 Make sure have "remove.txt" ready and running program "BuildModel.py".
        It will generate the "model.txt" based on "TrainingReviewSet.yaml"
    
    2.4 Running "TestDataset.py" to test the "TestingReviewSet.yaml". 
        It will generate the "result.txt" as the result of testing
    
    2.5 As the team of one, I pick Task 2.3 word length filtering.
        Go to Word_length_filtering folder and running "PerformencePlot.py" to generate bar graph of required results.
        The image "Correctness_plot.png" under Word_length_filtering folder is the saved image of results.
        (* "length-model.txt" is the copy of "model_9.txt" and "length-result.txt" is the copy of "result_9.txt" *)
