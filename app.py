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


def products_filling():
    with open('products.txt', 'r') as file:
        lines = file.readlines()
        random_lines = random.sample(lines, 5)
        return str(random_lines)


@app.route("/", methods=["GET", "POST"])
def index():
    mydb = dbConnect()
    cursor = mydb.cursor()

    # sql = "INSERT INTO Products(ProductID, Name, Category, Price) VALUES (%s, %s, %s, %s)"
    # val = (1, "hui", "chqweleni&pezdi", 9999)

    # cursor.execute(sql, val)

    # mydb.commit()
    random_lines = products_filling()
    for line in random_lines:
        line.replace('\n', '')
        print(len(random_lines))

    return random_lines


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
