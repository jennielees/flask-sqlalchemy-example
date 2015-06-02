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
