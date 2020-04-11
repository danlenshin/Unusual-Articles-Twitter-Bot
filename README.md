# Unusual-Articles-Twitter-Bot
A Twitter bot which uploads a random article from Twitter's List of Unusual Articles. This is currently the code used by the Twitter bot @UArticleBot. This repository includes 6 files:

**TweetRandom.sh**
This file is a bash script which first downloads the raw HTML from https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles using wget, and overwrites the existing HTML file if it exists in the same directory. It then runs `parser.py` and `tweeter.py`.

**Wikipedia:Unusual_articles**
This is the HTML of https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles downloaded by `TweetRandom.sh` and used by the two python scripts. The file in this repository is the HTML from this webpage as it was on April 10, 2020.

**parser.py**
This is a Python script which parses through the HTML and returns a list in the form of a .json file. This list is made up of extensions and titles of Wikipedia articles. This list is formatted to include the article's extension first then the title, for example:
`["Breast-shaped_hill", "Breast-shaped hill", "Eiffel_Tower_replicas_and_derivatives", "Eiffel Tower replicas and derivatives",..]`

**UAList.json**
This is the .json file generated by `parser.py`.

**Tweeter.py**
This is a Python script which takes a random extension (even-numbered) element and its respective title (the element after the extension) from the array in `UAList.json` and updates the status of the Twitter app defined with the API and auth keys.

**Blacklist.json**
This is a .json file containing an array which includes extensions which `tweeter.py` should not tweet. This can be modified to include any extensions in `UAList.json`.
