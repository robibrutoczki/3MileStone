
  <ul class="navbar-nav m-2">
        <li class="nav-item">
              <a class="nav-link" href="{{url_for('get_categories')}}">Manage Categories</a>
        </li>
    </ul>

@app.route('/find_recipe')
def find_recipe():
    return render_template("searchrecipe.html",
                           recipes=mongo.db.recipes.find())
"""
Working on the Categories
"""


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/find_rec_cat/<category_name>', methods=['GET', 'POST'])
def search_by_rec(category_name):
    db_query = {'category_name': category_name}
    rec_by_cat = mongo.db.recipes.find(db_query)
    results_total = mongo.db.recipes.count(db_query)
    return render_template("base.html",
                           catrec=rec_by_cat,
                           results_total=results_total)


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

