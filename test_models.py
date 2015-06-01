import traceback

from models import db, create_dessert


def check_test(func):
    """ This is a decorator that simply prints out whether the function
        it calls succeeded or not. You don't need to edit this.
    """
    def func_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print ":) {} passed".format(func.__name__)
        except AssertionError:
            traceback.print_exc()
            print ":( {} failed".format(func.__name__)
    return func_wrapper


# ## Testing validation for the create_dessert method.

@check_test
def test_create_dessert_works():
    test_name = "Test Dessert"
    test_price = 10
    test_calories = 200

    dessert = create_dessert(test_name, test_price, test_calories)

    assert dessert is not None

    # Delete this dessert now we are done
    db.session.delete(dessert)
    db.session.commit()


@check_test
def test_create_dessert_wrong_types():
    # Test we can't create a dessert with the wrong type of input

    test_name = 4
    test_price = "Cake"
    test_calories = "None"

    # Initialize the dessert variable so we can check it later.
    dessert = None

    # "Try" to create the dessert, and do nothing (pass) if we get an error.
    # After this next block of code, dessert should still be None.

    try:
        dessert = create_dessert(test_name, test_price, test_calories)
    except Exception:
        pass

    # Check dessert is still not created.
    assert dessert is None


@check_test
def test_create_dessert_missing_data():
    # Test that if we pass 'None' in, we fail.
    dessert = None

    try:
        dessert = create_dessert(None, None, None)
    except Exception:
        # You could use e.message in here to check that the error message
        # is correct if you like.
        pass

    # Check dessert is still not created.
    assert dessert is None

    # Also try with empty strings
    try:
        dessert = create_dessert('', '', '')
    except Exception:
        pass

    # Check dessert is still not created.
    assert dessert is None

    # Are there other values we should test for? What about a sensible
    # range for each item?


if __name__ == "__main__":

    # Run every method in this file which starts with test_.

    for item in dir():
        # Loop through all the defined items we know about (functions, etc).
        # If the name starts with test_, assume it's a test and run it!
        if item.startswith('test_'):
            globals()[item]()
