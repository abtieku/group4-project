import pandas
from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from connect_sql_db import build_engine
import os
import time


#testing df


engine = build_engine(database_name="database1",host="35.225.193.21")

app = Flask(__name__)

run_with_ngrok(app)

df = pandas.read_sql("select * from cleaned_table", con=engine)






@app.route('/', methods=["GET","POST"])
def first_page():

    df = pandas.read_sql("select * from cleaned_table", con=engine)

    df.dropna(how="any", inplace=True)

    categories = df.columns.tolist()

    lat_lng = {
        "state":df["state"].tolist(),
        "name": df["name"].tolist(), 
        "lat":df["latitude"].tolist(),
        "lng":df["longitude"].tolist(),
        "review_count": df["review_count"].tolist()

    }


    df = pandas.read_sql("select * from cleaned_table", con=engine)

    df.dropna(how="any", inplace=True)

    if request.method == "POST":
        
        df2 = df.loc[df[request.form["category"]] == 1]
        lat_lng = {
            "state":df2["state"].tolist(),
            "name": df2["name"].tolist(), 
            "lat":df2["latitude"].tolist(),
            "lng":df2["longitude"].tolist(),
            "review_count": df2["review_count"].tolist()

        }

        print(lat_lng)
        
        return render_template("homepage.html", latLng=lat_lng, categories=categories)

    return render_template("homepage.html", latLng=lat_lng, categories=categories)




if __name__ == "__main__":
    app.run()