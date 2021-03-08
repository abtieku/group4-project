import pandas
from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from connect_sql_db import build_engine
from pprint import pprint
import os
import json
import time

engine = build_engine(database_name="database1",host="35.225.193.21")

app = Flask(__name__)

run_with_ngrok(app)

df_1 = pandas.read_sql("select * from cleaned_table", con=engine)

@app.route('/', methods=["GET","POST"])
def first_page():
    df = df_1.copy()
    df.dropna(how="any", inplace=True)
    categories = df.drop(["address","city","state","business_id","city", "postal_code","latitude","longitude","stars","review_count","name"],axis=1).columns.tolist()
    lat_lng = {
        'state':df["state"].tolist(),
        'name': df["name"].tolist(), 
        'lat':df["latitude"].tolist(),
        'lng':df["longitude"].tolist(),
        'review_count': df["review_count"].tolist()
    }
    df.dropna(how="any", inplace=True)


    df2 = df_1.copy()
    
    if request.method == "POST":
        state = request.form["state"]
        selection = request.form["category"]

        return redirect(url_for("map",change_me="True",state=state,selection=selection,code=302,response=200,_scheme="https",_external=True))    
    
    return render_template(
        "homepage.html",
        latLng=lat_lng,
        categories=categories,
        table = df2[["name","state","stars","review_count"]].sort_values("review_count", ascending = False).set_index("name").to_html(table_id="dataframe"),
        state_count = df2.groupby("state").count()[["business_id"]].sort_values("business_id", ascending=False).to_html(table_id="state_count"), 
        category_2="select category",
        states=list(set(df2.state.tolist())),
        state_2="all"
    )
@app.route('/map', methods=["GET","POST"])
def map():
    answer = request.args.get("change_me")
    if answer == "True":
        
        state = request.args.get("state")
        print(state)
        if state != "all":
            df2 = df_1.loc[df_1.state == state].dropna(how="any")
        
        elif state == "all":
            df2 = df_1.copy().dropna(how="any")
        selection = request.args.get("selection")
        print(state)
        print(selection)
        
        df2 = df2.loc[df2[selection] == 1]

        lat_lng = {
            'state':df2["state"].tolist(),
            'name': df2["name"].tolist(), 
            'lat':df2["latitude"].tolist(),
            'lng':df2["longitude"].tolist(),
            'review_count': df2["review_count"].tolist()

        }

        categories = df_1.drop(["address","city","state","business_id","city", "postal_code","latitude","longitude","stars","review_count","name"],axis=1).columns.tolist()

        if request.method == "POST":
            state = request.form["state"]
            selection = request.form["category"]

            return redirect(url_for("map",change_me="True",state=state,selection=selection,code=302,response=200,_scheme="https",_external=True))    
    
    

    return render_template(
        "homepage.html",
        latLng=lat_lng,
        categories=categories,
        table = df2[["name","state","stars","review_count"]].sort_values("review_count", ascending = False).set_index("name").to_html(table_id="dataframe"),
        state_count = df2.groupby("state").count()[["business_id"]].sort_values("business_id", ascending=False).to_html(table_id="state_count"), 
        category_2=selection,
        states=list(set(df2.state.tolist())),
        state_2=state
    )


    



if __name__ == "__main__":
    app.run()