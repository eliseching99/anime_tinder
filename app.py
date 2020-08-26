from flask import Flask, render_template, request
import csv
import requests
import random
app = Flask(__name__)

@app.route("/")
def home():

    
    with open('anime.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rows = list(readCSV)
        random_row=random.randint(1,12292)
        anime={'name':'',
        'genre':'',
        'type':'',
        'episodes':'',
        'ratings':'',
        'members':'',
        'image':'http://placehold.it/300x200/000000/&text=Header'}
    




        record=rows[random_row]
        name=(record[1])
        genre= record[2]
        anime_type=record[3]
        episodes=record[4]
        ratings=record[5]
        members=record[6]
        anime['name']=name
        anime['genre']=genre
        anime['type']=anime_type
        anime['episodes']=episodes
        anime['ratings']=ratings
        anime['members']=members
        
        print(anime)
        r = requests.get(f'https://api.jikan.moe/v3/search/anime?q={name}')
        if r.status_code==200:
            url_data=(r.json())
            
            anime_image=url_data['results'][0]['image_url']
            anime['image']=anime_image


        # print(rows[random_row])
        
    return render_template("home.html",data=anime)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    r = requests.get(f'https://api.jikan.moe/v3/search/anime?q={text}')
    if r.status_code==200:
        url_data=(r.json())
        print(url_data)
        return render_template("queried.html",data=url_data)

            
    return 
# class Shirt():
#     def __init__(self, size, color):
#         self.size=size
#         self.color=color
#         self.material='cotton'




@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)