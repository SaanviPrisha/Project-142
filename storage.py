import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]