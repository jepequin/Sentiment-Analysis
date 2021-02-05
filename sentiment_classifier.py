#!/usr/bin/python
### Import necessary modules
import csv
from matplotlib import pyplot as plt

def twitter_data():
	'''Returns dictionary with key:value pairs for tweets, number of retweets, and number of replies (values are lists)'''
	data = {'tweets':[],'retweet_count':[],'reply_count':[]}
	with open('data/twitter_input_data.csv','r') as twitter_csv:
		## Use next function to avoid header
		next(twitter_csv)
		for line in twitter_csv:
			tweet, retweet_count, reply_count = line.split(',')
			data['tweets'].append(tweet)
			data['retweet_count'].append(retweet_count)
			data['reply_count'].append(reply_count)
	return data

def sentiment_dictionary():
	'''Returns dictionary with key:value pairs for negative, and positive words (values are lists)'''
	words = {} 
	with open('data/negative_words.txt','r') as negative_txt:
		## Get content of 'negative_words.txt' as string
		text = negative_txt.read()
		## Negative words appear after empty line
		negative_words = text.split('\n\n')[1]
		## Get list of negative words 
		words['negative'] = negative_words.split('\n')   
	with open('data/positive_words.txt','r') as positive_txt:
		text = positive_txt.read()
		positive_words = text.split('\n\n')[1]
		words['positive'] = positive_words.split('\n')
	return words

def parse(tweet):
	'''Strips tweet of non-alpha-numerical characters and returns it as list of lower case words'''
	chars_to_remove = ['@','#',':','…','!','?','.',"'","’"]
	parsed_tweet = tweet.lower()
	for char in chars_to_remove:
		lst = parsed_tweet.split(char)
		parsed_tweet = ''.join(lst)
	## Returned list might contain characters '-'
	return parsed_tweet.split()


def tweet_scores(tweets, negative_words, positive_words):
	'''Returns dictionary with key:value pairs for negative, positive, and net scores (values are lists)'''
	scores = {'negative':[],'positive':[],'net':[]}
	for tweet in tweets:
		negative_score = 0
		positive_score = 0
		parsed_tweet = parse(tweet)
		for word in parsed_tweet:
			if word in negative_words:
				negative_score -= 1
			if word in positive_words:
				positive_score +=1
		net_score = negative_score + positive_score
		scores['negative'].append(str(negative_score))
		scores['positive'].append(str(positive_score))
		scores['net'].append(str(net_score))
	return scores

### Obtain data necessary for output csvfile
data = twitter_data()
words = sentiment_dictionary()
scores = tweet_scores(data['tweets'], words['negative'], words['positive'])

### Create list whose elements are tuples, each of which corresponds to a line of output csvfile  
metrics = zip(scores['negative'],scores['positive'],scores['net'],data['retweet_count'],data['reply_count'])

### Write csv file
with open('data/tweet_output_data.csv','w') as csvfile:
	csvfile.write('Negative score,Positive score,Net score,Number of retweets,Number of replies\n')
	for metric in metrics:
		csvfile.write(','.join(metric))

### Plot Net score vs. Number of Retweets
## Change string to integer (matplotlib treats strings as “categories”, and plots them in the order supplied)
net_scores = [int(score) for score in scores['net']]
retweet_count = [int(retweet) for retweet in data['retweet_count']]
plt.scatter(net_scores,retweet_count)
plt.xlabel('Net score')
plt.ylabel('Number of retweets')
plt.show()



