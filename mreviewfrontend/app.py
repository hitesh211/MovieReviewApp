from flask import Flask,request,render_template,redirect
import requests
import os

class Review(object):
    def __init__(self,name,movname,rating,review):
        self.name = name
        self.movname = movname
        self.rating = rating
        self.review = review
        
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        movname = request.form["movname"]
        rating = request.form["rating"]
        review = request.form["review"]

        res = requests.post("http://backend:5000/reviews/add",data={"name":name,"movname":movname,"rating":rating,"review":review})

        if res.status_code == 200:
            return redirect("/reviews")

    return render_template("index.html")

@app.route("/reviews",methods=["GET"])
def reviews():

    res = requests.post("http://backend:5000/reviews/list").json()
    reviews = []

    for review in res["list"]:
        reviews.append(Review(review[0],review[1],review[2],review[3]))

    return render_template("reviews.html",reviews=reviews)

app.run(host="0.0.0.0",port=5000)