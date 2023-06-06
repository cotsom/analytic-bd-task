from time import sleep
from flask import Flask, render_template, render_template_string, request
import psycopg2
import random
import os

app = Flask(__name__)


def dbConnect():
    mydb = psycopg2.connect(
        host="db",
        user="student",
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    return mydb


@app.route("/", methods=["GET", "POST"])
def index():
    # mydb = dbConnect()
    # cursor = mydb.cursor()

    # sql = "INSERT INTO Products(ProductID, Name, Category, Price) VALUES (%s, %s, %s, %s)"
    # val = (1, "hui", "chqweleni&pezdi", 9999)

    # cursor.execute(sql, val)

    # mydb.commit()
    

    return render_template('index.html')

@app.route("/query", methods=["GET", "POST"])
def query():
    if request.method == 'POST':
        mydb = dbConnect()
        cursor = mydb.cursor()

        query = request.form.get('query')
        try:
            cursor.execute(query)
        except Exception as e:
            return render_template('query.html', error=e)

        colnames = [desc[0] for desc in cursor.description]
        answer = cursor.fetchall()

        cursor.close()


        return render_template('query.html', answer=answer, colnames=colnames)
    
    return render_template('query.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
