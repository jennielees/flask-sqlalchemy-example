from app import app, db

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Dessert(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)
    doilikeit = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="desserts")

    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def calories_per_dollar(self):
        if self.calories:
            return self.calories / self.price


class Menu(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(250))
    name = db.Column(db.String(100))
    avatar = db.Column(db.String(250))

    def __init__(self, username, password, email, name, avatar):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.avatar = avatar


def create_dessert(new_name, new_price, new_calories):
    # Create a dessert with the provided input.

    # We need every piece of input to be provided.

    # Can you think of other ways to write this following check?
    if new_name is None or new_price is None or new_calories is None:
        raise Exception("Need name, price and calories!")

    # They can also be empty strings if submitted from a form
    if new_name == '' or new_price == '' or new_calories == '':
        raise Exception("Need name, price and calories!")

    # This line maps to line 16 above (the Dessert.__init__ method)
    dessert = Dessert(new_name, new_price, new_calories)

    # Actually add this dessert to the database
    db.session.add(dessert)

    # Save all pending changes to the database

    try:
        db.session.commit()
        return dessert
    except:
        # If something went wrong, explicitly roll back the database
        db.session.rollback()


def delete_dessert(id):

    dessert = Dessert.query.get(id)

    if dessert:
        # We store the name before deleting it, because we can't access it
        # afterwards.
        dessert_name = dessert.name
        db.session.delete(dessert)

        try:
            db.session.commit()
            return "Dessert {} deleted".format(dessert_name)
        except:
            # If something went wrong, explicitly roll back the database
            db.session.rollback()
            return "Something went wrong"
    else:
        return "Dessert not found"


if __name__ == "__main__":
    manager.run()
