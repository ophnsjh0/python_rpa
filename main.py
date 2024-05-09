from flask import Flask, render_template, request, redirect, flash, send_file

app = Flask("AutoCheck")

@app.route("/")
def home():
    return render_template("home.html")

app.run("0.0.0.0")