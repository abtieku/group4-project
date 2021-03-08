import pandas
from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from connect_sql_db import build_engine
import os
import time


#testing df
final_table = pandas.read_csv("C:\\Users\\secam\\Downloads\\merged_table_1.csv",low_memory = False)


food_lst=[]
for i in final_table.columns:
    if "food" in i or "restaurant" in i:
        food_lst.append(i)
len(food_lst)


filtered_df = final_table.loc[
    (final_table[food_lst[0]] == 1) |
    (final_table[food_lst[1]] == 1) |
    (final_table[food_lst[2]] == 1) |
    (final_table[food_lst[3]] == 1) |
    (final_table[food_lst[4]] == 1) |
    (final_table[food_lst[5]] == 1) |
    (final_table[food_lst[6]] == 1) |
    (final_table[food_lst[7]] == 1) |
    (final_table[food_lst[8]] == 1) |
    (final_table[food_lst[9]] == 1) |
    (final_table[food_lst[10]] == 1) |
#     (final_table[food_lst[11]] == 1) |
    (final_table[food_lst[12]] == 1) |
    (final_table[food_lst[13]] == 1) |
    (final_table[food_lst[14]] == 1) |
    (final_table[food_lst[15]] == 1) |
    (final_table[food_lst[16]] == 1) |
    (final_table[food_lst[17]] == 1) |
    (final_table[food_lst[18]] == 1) |
    (final_table[food_lst[19]] == 1) |
    (final_table[food_lst[20]] == 1) |
    (final_table[food_lst[21]] == 1) |
    (final_table[food_lst[22]] == 1) |
    (final_table[food_lst[23]] == 1) |
    (final_table[food_lst[24]] == 1) |
    (final_table[food_lst[25]] == 1) |
    (final_table[food_lst[26]] == 1) |
    (final_table[food_lst[27]] == 1) |
    (final_table[food_lst[28]] == 1) |
    (final_table[food_lst[29]] == 1) |
    (final_table[food_lst[30]] == 1) 
    
].copy()

df = final_table[:100]
#engine = build_engine(database_name="database1",host="35.225.193.21")

#df = pandas.read_sql("select * from business_table", con=engine)



lat_lng = {
    "state":df["state"].tolist(),
    "name": df["name"].tolist(), 
    "lat":df["latitude"].tolist(),
    "lng":df["longitude"].tolist()

}

print(df.duplicated().sum())

print(df.state.value_counts())

time.sleep(20)


app = Flask(__name__)

run_with_ngrok(app)

@app.route('/', methods=["GET","POST"])
def first_page():
    return render_template("homepage.html", latLng=lat_lng)




if __name__ == "__main__":
    app.run()