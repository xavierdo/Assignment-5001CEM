from flask import Flask, abort
import sqlite3, os
from flask import flash, session, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_bcrypt import Bcrypt

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def homepage():
    return render_template("homepage.html") #homepage

@app.route('/', methods=['POST'])
def login():
    username = request.form['Username'] #request username and password
    generate_password_hash = request.form['Password'] 
    
    sqlconnection = sqlite3.connect('store.db')
    cursor = sqlconnection.cursor()
    #check username and password if match with in the useers table then redirect to products
    query1 = "SELECT Username, Password From users WHERE Username ='{un}' AND Password = '{ps}'".format(un=username, ps=generate_password_hash)
    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows)==1:
        return redirect(url_for('products'))
    else: 
        return redirect(url_for('register')) #redirect to register page if user is not registered 
    return render_template('homepage.html')
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method =="POST":
        dUn = request.form['Dusername'] #request username and password 
        dPw = request.form['Dpassword']
        sqlconnection = sqlite3.connect('store.db') #connect to the database 
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO users VALUES('{u}','{p}')".format(u=dUn, p=dPw) #store password into users table 
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect(url_for('homepage')) #redirect to the homepage for login users
    return render_template('register.html')

@app.route('/add_books', methods=['GET','POST'])
def add_books(): #function use to store the books attributes into books table 
    if request.method =="POST":
        id = request.form['ID']
        title = request.form['Title']
        author = request.form['Author']
        description = request.form['Description']
        image = request.form['Image']
        price = request.form['Price']
        sqlconnection = sqlite3.connect('store.db')
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO books VALUES('{a}','{b}','{c}','{d}','{e}',{f})".format(a=id, b=title, c=author, d=description, e=image, f=price)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect(url_for('products')) #redirect to the products page to display new items that has been added.
    return render_template('add_books.html')

@app.route('/products')
def products(): #showing all the books produtcs in the database to be displayed in product page.
    try:
        con = sqlite3.connect('store.db')
        cur = con.cursor();
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        return render_template('products.html', products=rows)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()

        
sid = 'SJo_c3Nob3BwaW5nUGF5'
pid = 'payment1'
secret = 'kvza9mEtztYV7i-WTtu-REwfilcA'
		
@app.route('/add', methods=['POST'])
def add_product_to_cart():
    cursor = None
    try:
        _quantity = int(request.form['quantity']) #based on ID or EAN number, quantity will be added depend on users clicked
        _code = request.form['id']
        
        if _quantity and _code and request.method == 'POST': 
            con = sqlite3.connect('store.db')
            cur = con.cursor();
            cur.execute("SELECT * FROM books WHERE id=?;", [_code])
            row = cur.fetchone() #everytime user clicked the quantity will be added one into cart. 
            itemArray = { row[0] : {'id' : row[0], 'title' : row[1], 'author' : row[2], 'description' : row[3],'quantity' : _quantity, 'image' : row[4], 'price' : row[5],  'total_price': _quantity * row[5]}}
            print('itemArray is', itemArray)
            
            all_total_price = 0
            all_total_quantity = 0
            
            session.modified = True
            
            if 'cart_item' in session: #if new item in cart_item 
                print('in session')
                if row[0] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row[0] == key: #if ID equal to the key values of current item 
                            old_quantity = session['cart_item'][key]['quantity']#old quantity will be added into quantity
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row[5] #total quantity * price of the products 
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)
                    
                for key, value in session['cart_item'].items(): #when item presented in cart quantity and total_price will be added 
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row[5] # if no new item added then it will show only current total price + quantity *price. 
                
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            
            checksumstr = f"pid={pid:s}&sid={sid:s}&amount={all_total_price:.1f}&token={secret:s}"
            #print('checksumstr is', checksumstr)
            checksum = md5(checksumstr.encode('utf-8')).hexdigest()
            session['checksum'] = checksum
            #print('checksum is', checksum)
            session['sid'] = sid
            session['pid'] = pid
            
            return redirect(url_for('.products'))
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()


@app.route('/empty')
def empty_cart(): #clear all the item in products using session and then redirect to products
	try:
		session.clear()
		return redirect(url_for('.products'))
	except Exception as e:
		print(e)

@app.route('/delete/<string:id>')
def delete_product(id): #delete item in the product based upon checking the id 
	try:
		all_total_price = 0
		all_total_quantity = 0
		session.modified = True
		
		for item in session['cart_item'].items():
			if item[0] == id:				
				session['cart_item'].pop(item[0], None)
				if 'cart_item' in session:
					for key, value in session['cart_item'].items():
						individual_quantity = int(session['cart_item'][key]['quantity'])
						individual_price = float(session['cart_item'][key]['total_price'])
						all_total_quantity = all_total_quantity + individual_quantity
						all_total_price = all_total_price + individual_price
				break
		
		if all_total_quantity == 0:
			session.clear()
		else:
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price
		return redirect(url_for('.products'))
	except Exception as e:
		print(e)
		
def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False		
		
if __name__ == "__main__":
    app.run()