import pandas
from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from connect_sql_db import build_engine
from pprint import pprint
import os
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
        "state":df["state"].tolist(),
        "name": df["name"].tolist(), 
        "lat":df["latitude"].tolist(),
        "lng":df["longitude"].tolist(),
        "review_count": df["review_count"].tolist()

    }



    df.dropna(how="any", inplace=True)

    if request.method == "POST":

        state = request.form["state"]

        if state != "all":
            df = df_1.loc[df_1.state == state]
        
        if state == "all":
            df = df_1.copy()

        df2 = df.loc[df[request.form["category"]] == 1]
        category = request.form["category"]

        lat_lng = {
            "state":df2["state"].tolist(),
            "name": df2["name"].tolist(), 
            "lat":df2["latitude"].tolist(),
            "lng":df2["longitude"].tolist(),
            "review_count": df2["review_count"].tolist()

        }

        pprint(lat_lng)

        table = df2.copy()

        selection = request.form["category"]



        return render_template(
            "homepage.html", 
            latLng=lat_lng, 
            categories=categories, 
            table = table[["name","state","stars","review_count",category]].sort_values("review_count", ascending=False).set_index("name").to_html(table_id="dataframe"), 
            state_count = table.groupby("state").count()[["business_id"]].sort_values("business_id", ascending=False).to_html(table_id="state_count"),
            category_2=selection, 
            states=list(set(df_1.state.tolist())),
            state_2="all"
        )

    df2 = df_1.copy()

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




if __name__ == "__main__":
    app.run()