from twython import Twython
import json
import random

#Account verificaton
API_key = 'YOUR API KEY HERE'
API_secret_key = 'YOUR SECRET API KEY HERE'
Access_token = 'YOUR ACCESS TOKEN HERE'
Access_token_secret = 'YOUR SECRET ACCESS TOKEN HERE'
UArticlesBot = Twython(API_key, API_secret_key, Access_token, Access_token_secret)

articles = json.loads(open('UAList.json').read()) #Import array from json file
randomArticle = random.randrange(0, (len(articles)/2), 2) #Select random extension from array

#Get article extension and title using random article number
articleExtension = articles[randomArticle]
articleTitle = articles[randomArticle + 1]

#Send tweet
UArticlesBot.update_status(status = 'Today\'s article is: %s\nen.wikipedia.org/wiki/%s' %(articleTitle, articleExtension))
