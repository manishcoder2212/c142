import csv

all_articles=[]

liked_articles=[]
disliked_articles=[]

with open('articles.csv',encoding="utf8") as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    all_articles=data[1:]
