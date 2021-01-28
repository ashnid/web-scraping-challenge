from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home(): 
    # Find data
    mars_facts = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", mars=mars_facts)

# Scrape function
@app.route("/scrape")
def scrape():
    # Run
    mars_data = scrape_mars.scrape()
    # Update 
    mongo.db.collection.update({}, mars_data, upsert=True)
    # Redirect to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    