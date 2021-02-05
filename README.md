# SENTIMENT CLASSIFIER

This is the final Project of the course "Python Functions, Files, and Dictionaries". This course is part of the Python 3 Programming Specialization offer by University of Michigan in Coursera. 

The goal of this project is to use the tools introduced during the course: manipulating csv files, using dictionaries, and defining functions.  

## DESCRIPTION

Some (semi-randomly generated) twitter data is provided in a csv file named "twitter_input_data.csv" which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files "positive_words.txt" and "negative_words.txt".

The task is to build a sentiment classifier, which detects how positive or negative each tweet is. We create a csv file, named "twitter_output_data.csv"  which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, we use matplotlib to produce a graph of the Net Score vs Number of Retweets, it is in the file "score_vs_retweets.png".

The code is in the file "sentiment_classifier.py". 


