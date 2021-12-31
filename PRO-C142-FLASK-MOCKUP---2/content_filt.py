import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df1=pd.read_csv('articles.csv')
df1_filtered=df1[df1['eventType']!="CONTENT REMOVED"]

title_soup=df1_filtered['title'].to_list()

for i in range(len(title_soup)):
  title_soup[i]=title_soup[i].lower()

count=CountVectorizer(stop_words='english')
count_matrix=count.fit_transform(title_soup)

cosine_sim=cosine_similarity(count_matrix,count_matrix)

df1_filtered=df1_filtered.reset_index()
indices=pd.Series(df1_filtered.index,index=df1_filtered['title'])

def get_recomm(title,cosine_sim2):
  idx=indices[title]
  sim_scores=list(enumerate(cosine_sim2[idx]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]
  movies_indices=[i[0] for i in sim_scores]
  return df1_filtered['title'].iloc[movies_indices]


get_recomm("Task management app Asana raises $50M at a $600M valuation led by YC's Sam Altman",cosine_sim)

