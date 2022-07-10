from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()

categories = ['rec.sport.baseball', 'rec.sport.hockey']

print(emails.data[5])
print(emails.target[5])