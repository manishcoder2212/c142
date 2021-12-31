import pandas as pd

df2=pd.read_csv('interactions.csv')
df1=pd.read_csv('articles.csv')

df1_filtered=df1[df1['eventType']!="CONTENT REMOVED"]

def find_total_events(df1_row):
  total_views = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"]== "VIEW")].shape[0]
  total_follows = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"]== "FOLLOW")].shape[0]
  total_bookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"]== "BOOKMARK")].shape[0]
  total_likes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"]== "LIKE")].shape[0]
  total_comments = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"]== "COMMENT CREATED")].shape[0]
  return total_likes+total_views+total_follows+total_bookmarks+total_comments

df1_filtered['total_events']=df1_filtered.apply(find_total_events,axis=1)
df1_filtered=df1_filtered.sort_values(["total_events"],ascending=[False])

df1_final_filt=df1_filtered[df1_filtered['lang']=="en"] 
print(df1_final_filt.head(10))