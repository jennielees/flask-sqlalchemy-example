from app import db


class Dessert(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)

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


def create_dessert(new_name, new_price, new_calories):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    dessert = Dessert(new_name, new_price, new_calories)

    # Actually add this dessert to the database
    db.session.add(dessert)

    # Save all pending changes to the database
    db.session.commit()

    return dessert


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
