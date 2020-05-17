import os

from os import path
from datetime import datetime
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from flask import Flask, render_template, redirect, request, url_for
"""
Renders a template from the template folder with the given context.
"""
"""
Safe way to use MongoDB
"""
if path.exists("env.py"):
    import env


app = Flask(__name__)


"""
Login to MongoDB
"""
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DB')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)
datetime_now = datetime.now()

"""
Works with Recipes
"""
@app.route('/')
@app.route('/get_recipes')   # Starting point of the website
def get_recipes():
    return render_template("recipe.html",
                           recipes=mongo.db.recipes.find())

# Rendering all the recipes on Index.html
@app.route('/get_index')
def get_index():
    return render_template("index.html",
                           recipes=mongo.db.recipes.find())

# Rendering addrecipe.html
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


# This is inserting a recipe to the DB then goes back to all recipes
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_index'))

# Find a recipe for editing ,using recipe ID
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)

# Updateting a recipe then returning the updeted recipe
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'recipe_ingrediens': request.form.get('recipe_ingrediens'),
        'recipe_diff': request.form.get('recipe_diff'),
        'recipe_met': request.form.get('recipe_met'),
        'recipe_time': request.form.get('recipe_time'),
        'recipe_url': request.form.get('recipe_url'),
        'recipe_serv': request.form.get('recipe_serv'),
        'recipe_rate': request.form.get('recipe_rate')
    })
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("showOne.html", recipe=recipe_id)

# Deleting a recipe then goes back to all recipes
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_index'))

# Finds the recipe and show on one page
@app.route('/show_recipe/<recipe_id>/')
def show_recipe(recipe_id):
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("showOne.html", recipe=recipe_id)

# Searching in recipes then returning it on search.html
@app.route('/search_recipe/<recipe_diff>', methods=['GET', 'POST'])
def search_by_diff(recipe_diff):
    db_query = {'recipe_diff': recipe_diff}
    recipe_by_difficulty = mongo.db.recipes.find(
        db_query).sort([("recipe_name", -1)])
    results_total = mongo.db.recipes.count(db_query)
    return render_template("search.html",
                           recipes=recipe_by_difficulty,
                           results_total=results_total)

# Searching in recipes then returning it on search.html
@app.route('/find_recipe_rate/<recipe_rate>', methods=['GET', 'POST'])
def search_by_rate(recipe_rate):
    db_query = {'recipe_rate': recipe_rate}
    recipe_by_rate = mongo.db.recipes.find(
        db_query).sort([("recipe_name", -1)])
    results_total = mongo.db.recipes.count(db_query)
    return render_template("search.html",
                           recipes=recipe_by_rate,
                           results_total=results_total)

# Searching in recipes then returning it on search.html
@app.route('/find_recipe_serv/<recipe_serv>', methods=['GET', 'POST'])
def search_by_serv(recipe_serv):
    db_query = {'recipe_serv': recipe_serv}
    recipe_by_serv = mongo.db.recipes.find(
        db_query)
    results_total = mongo.db.recipes.count(db_query)
    return render_template("search.html",
                           recipes=recipe_by_serv,
                           results_total=results_total)

# Searching in recipes then returning it on search.html
@app.route('/find_recipe_cat/<category_name>', methods=['GET'])
def search_by_reccat(category_name):
    db_query = {'category_name': category_name}
    recipe_by_cat = mongo.db.recipes.find(
        db_query)
    results_total = mongo.db.recipes.count(db_query)
    return render_template("search.html",
                           recipes=recipe_by_cat,
                           results_total=results_total)


"""
Working on the Categories
"""

# These are not in use till Sign in part not finished,
# working fine,able to add,edit,delete categories
# only need a link in the navbar
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


"""
Working on Shop/Item
"""

# Find a item then returning by category
@app.route('/find_item_cat/<category_name>', methods=['GET', 'POST'])
def search_by_cat(category_name):
    db_query = {'category_name': category_name}
    item_by_cat = mongo.db.shop.find(db_query)
    results_total = mongo.db.shop.count(db_query)
    return render_template("searchitem.html",
                           cat=item_by_cat,
                           results_total=results_total)


"""
Working on Shop/Item
"""

# Rendering all items on shop page
@app.route('/get_shop')
def get_shop():
    return render_template("shop.html",
                           shop=mongo.db.shop.find())

# Getting a item by ID  then returning it on a webpage
@app.route('/show_item/<item_id>/')
def show_item(item_id):
    item_id = mongo.db.shop.find_one({"_id": ObjectId(item_id)})
    return render_template("showItem.html", item=item_id)


"""
Charts part
"""

# Rendering charts from MongoDB on charts.html
@app.route('/see charts')
def see_charts():
    return render_template('chart.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
