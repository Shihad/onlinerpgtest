from flask import Flask, render_template, request, redirect
from models import db, Personage

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.drop_all()
    db.create_all()
    hero1=Personage('Вирджил')
    hero2 = Personage('Джахейра')
    hero3 = Personage('Рейстлин Маджере')
    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(hero3)
    db.session.commit()

@app.route("/index")
@app.route("/")
def index():
    hero=Personage.query.filter_by(id=1).first()
    return render_template("index.html", hero=hero)

@app.route("/personages")
def personages_list():
    personages=Personage.query.all()
    return render_template("personages_list.html",personages=personages)

@app.route("/personages/<p_id>")
def personage_page(p_id):
    personage=Personage.query.filter_by(id=p_id).first()
    return render_template("personage_page.html",personage=personage)

@app.route("/personages/create", methods=["POST","GET"])
def personage_create():
    if request.method=="GET":
        return render_template("personages_create.html")
    if request.method=="POST":
        name=request.form['name']
        hero = Personage(name)
        db.session.add(hero)
        db.session.commit()
        return redirect("/personages")




app.run()