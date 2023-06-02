from flask import *
from DBFile import get_db
from DBRequest import DataBase

app = Flask(__name__)

def GiveBase():
    db = get_db()
    return DataBase(db)

# главная страница
@app.route('/')
def index():
    menu = GiveBase().getHeader()
    content = GiveBase().getContent()
    return render_template('index.html', menu = menu , title = "Главная страница", content=content)

# Страница О нас
@app.route('/skills')
def about_us():
    menu = GiveBase().getHeader()
    return render_template('about_us.html',menu = menu , title = "О нас")



@app.route('/kabinet')
def kabinet():
    menu = GiveBase().getHeader()

    return render_template('login.html',menu=menu)




if __name__ == "__main__":
    app.run(debug=True)
