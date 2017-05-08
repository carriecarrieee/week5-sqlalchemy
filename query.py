"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

""" The datatype of the returned value of this query is that of an object
    at the location in memory:
    <flask_sqlalchemy.BaseQuery object at 0x7f78d4a63c10>

    If I add ".all()" at the end of the query, it will return a list of
    objects, but the repr method would kick in and show the format that
    I had specified in the repr method.
    """
    

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

""" An association table functions as the middle table between two or more
    tables that have a many-to-many relationship. Association tables do not
    typically contain any meaningful fields, but in SQLAlchemy the table would
    contain at least two foreign keys that point to each respective table it is
    connecting.
    """


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.get('ram').name

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(brand_id='che', name='Corvette').all()
# Returns list of objects containing all models that fit these filters.

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1928).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded=='1903', Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded<1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id !='for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    pass

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    pass


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass

