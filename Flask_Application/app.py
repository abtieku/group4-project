import pandas
from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from connect_sql_db import build_engine
import os

app = Flask(__name__)

run_with_ngrok(app)

@app.route('/', methods=["GET","POST"])
def first_page():
    return render_template("homepage.html")