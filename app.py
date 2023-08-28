from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from mongo_data import set_user , get_user
from mongo_conection import MongoAccess
app = Flask(__name__)


"""
client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/")

db = client.users
users_collection = db.user"""


@app.route('/')
def accueil():
    
    return render_template('index.html')


@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        user =MongoAccess.get_element(user,pw)
        if user is not None:
            return render_template('connexion.html',user=user)
        else:
            return render_template('index.html')
    return render_template('connexion.html')


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        # Insérer l'utilisateur dans la base de données
        #set_user(user,pw)
        MongoAccess.set_element(user,pw)
        return "Inscription réussie !"

    return render_template('inscription.html')




if __name__ == '__main__':
    app.run(debug=True)



































# @app.route("/")
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template("index.html",
#         online_users=online_users)


# @app.route('/')
# def index():
#     posts = data.lire_posts()
#     return render_template('index.html', post=posts)
#
#
# @app.route('/<int:post_id>')
# def post(post_id):
#     posts = data.get_post(post_id)
#     return render_template('post.html', post = posts)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)