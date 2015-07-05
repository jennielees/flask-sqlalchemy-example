## Flask / SQLAlchemy Simple App

This is a simple app using [Flask](http://flask.pocoo.org), [SQLAlchemy](http://www.sqlalchemy.org/) and the connecting [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) library.

### Installing Dependencies

```
pip install -r requirements.txt
```

### Running the App

To run the app, first run the `models.py` file directly to create the database tables:

```
$ python models.py
```

You only need to do this once, unless you change your model definitions (see below).

Then run the app itself:

```
$ python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser to see the results.

### Running Tests

```
python test_models.py
```


### Setting up the Database

This branch includes [Flask-Migrate](https://flask-migrate.readthedocs.org/en/latest/) to manage database changes. This compares the code in `models.py` to what is actually in the database.

```
pip install Flask-Migrate
```

First of all, **assuming you already set up the database from previous steps using `db.create_all()`**, you need to tell Flask-Migrate that the database is already up to date:

```
python models.py db init
python models.py db stamp head
```

"Head" refers to the "most current" database version.

If **the database is empty**, you will want to generate an initial migration and run it first.

```
python models.py db init
python models.py db migrate
python models.py db upgrade
```

If you add a change to the models, e.g. adding a new column, you repeat the second two steps.

```
python models.py db migrate
python models.py db upgrade
```

You can optionally add a message to the migration so you know what's going on when you look back.

```
python models.py db migrate -m "adding is_admin column to User"
python models.py db upgrade
```

Flask-Migrate supports plenty of other options, like downgrading if you want to undo some changes. Play with it!
