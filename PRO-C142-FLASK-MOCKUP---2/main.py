from flask import Flask,jsonify,request
import csv
from demo_filt import df1_final_filt
from content_filt import get_recomm
from storage import all_articles,liked_articles,disliked_articles
    
app=Flask(__name__)

@app.route('/get-articles')
def get_articles():
    # article_data={
    #     "id":all_articles[0][0],
    #     "title":all_articles[0][11],
    #     "url":all_articles[0][10],
    #     "lang":all_articles[0][13],
    #     "text":all_articles[0][12]
    # }
    return jsonify(
        {
            "data":all_articles,
            "status":"success"
        }
    )

@app.route('/liked-movie',methods=['POST'])
def liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)
    
@app.route('/disliked-movie',methods=['POST'])
def disliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)
    
@app.route('/popular-articles')
def get_popular_articles():
    article_data = []
    for article in df1_final_filt:
        _d = {
            "url": article[10],
            "title": article[11],
            "text": article[12],
            "lang": article[13],
            "total_events": article[14]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    },200)


@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recomm(liked_article[11])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200
    
if(__name__=="__main__"):
    app.run()