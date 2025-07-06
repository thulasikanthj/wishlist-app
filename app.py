from flask import Flask, render_template, redirect, url_for, request, session
from models import db, User, Wishlist, Product

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this for production

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
#logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Create database tables
with app.app_context():
    db.create_all()
# Initialize the database



@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists!"
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password!"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        wishlist_name = request.form['wishlist_name']
        new_wishlist = Wishlist(name=wishlist_name, owner=user)
        db.session.add(new_wishlist)
        db.session.commit()
        
        return redirect(url_for('dashboard'))

    wishlists = Wishlist.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, wishlists=wishlists)
@app.route('/wishlist/<int:wishlist_id>', methods=['GET', 'POST'])
def view_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)

    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        product_link = request.form['product_link']

        product = Product(name=product_name, price=product_price, link=product_link, wishlist=wishlist)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('view_wishlist', wishlist_id=wishlist_id))

    return render_template('wishlist.html', wishlist=wishlist)
@app.route('/delete_wishlist/<int:wishlist_id>', methods=['POST'])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    db.session.delete(wishlist)
    db.session.commit()
    return redirect(url_for('dashboard'))
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    wishlist_id = product.wishlist_id
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('view_wishlist', wishlist_id=wishlist_id))

if __name__ == '__main__':
    app.run(debug=True)




