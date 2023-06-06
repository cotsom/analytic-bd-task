from time import sleep
from flask import Flask, render_template, render_template_string, request
import mysql.connector
import random

app = Flask(__name__)


def dbConnect():
    mydb = mysql.connector.connect(
        host="mariadb",
        user="root",
        password="password",
        database="TechnicalStore"
    )

    return mydb


def products_filling(product_file, category_file):
    mydb = dbConnect()
    cursor = mydb.cursor()

    items_number = 5
    products = []
    category = []

    product_lines = open(product_file).read().splitlines()
    category_lines = open(category_file).read().splitlines()


    for _ in range(items_number):
        products.append(random.choice(product_lines))
        category.append(random.choice(category_lines))

    
    id = 1
    for _ in range(items_number):
        sql = "INSERT INTO Products(ProductID, Name, Category, Price) VALUES (%s, %s, %s, %s)"
        val = (id, products[_], category[_], random.randrange(50000))

        cursor.execute(sql, val)
        id = id+1
    mydb.commit()

def supliers_filling():
    mydb = dbConnect()
    cursor = mydb.cursor()

    items_number = 5
    products = []
    category = []

    product_lines = open(product_file).read().splitlines()
    category_lines = open(category_file).read().splitlines()



@app.route("/", methods=["GET", "POST"])
def index():
    # mydb = dbConnect()
    # cursor = mydb.cursor()

    # sql = "INSERT INTO Products(ProductID, Name, Category, Price) VALUES (%s, %s, %s, %s)"
    # val = (1, "hui", "chqweleni&pezdi", 9999)

    # cursor.execute(sql, val)

    # mydb.commit()
    
    products_filling("datasets/Products/products.txt", 'datasets/Products/product_category.txt')

    return "test"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
