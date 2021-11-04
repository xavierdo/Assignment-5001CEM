from flask import Flask
from flask import render_template
import sqlite3 

con = sqlite3.connect('products.db')

con.execute('CREATE TABLE products(id INT unsigned, name VARCHAR(255), code VARCHAR(255), image TEXT, price DOUBLE)')
con.close()  


con = sqlite3.connect('products.db')
con.execute('INSERT INTO products(id, name, code, image, price) VALUES (1, "American Tourist", "AMTR01", "product-images/bag.jpg", 12000.00),(2, "EXP Portable Hard Drive", "USB02", "product-images/external-hard-drive.jpg", 5000.00),(3, "Shoes", "SH03", "product-images/shoes.jpg", 1000.00),(4, "XP 1155 Intel Core Laptop", "LPN4", "product-images/laptop.jpg", 80000.00),(5, "FinePix Pro2 3D Camera", "3DCAM01", "product-images/camera.jpg", 150000.00),(6, "Simple Mobile", "MB06", "product-images/mobile.jpg", 3000.00),(7, "Luxury Ultra thin Wrist Watch", "WristWear03", "product-images/watch.jpg", 3000.00),(8, "Headphones", "HD08", "product-images/headphone.jpg", 400.00);')
con.commit()

con.close()  







