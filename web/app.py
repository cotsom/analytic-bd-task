from time import sleep
from flask import Flask, render_template, render_template_string, request
import psycopg2
import random
import os
import json

app = Flask(__name__)


def dbConnect():
    mydb = psycopg2.connect(
        host="db",
        user="student",
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    return mydb

def parse_tasks(file):
    with open(file, 'r') as task_file:
        tasks = json.load(task_file)
        return tasks

tasks = parse_tasks('tasks.json')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        mydb = dbConnect()
        cursor = mydb.cursor()

        task_id = int(request.form.get('task_id'))
        user_query = request.form.get('query')
        right_query = tasks['tasks'][task_id]['answerQuery']

        try:
            cursor.execute(user_query)
            user_answer = cursor.fetchall()

            cursor.execute(right_query)
            right_answer = cursor.fetchall()
        except Exception as e:
            return render_template('index.html', tasks=tasks, answer='Not correct')
        

        if user_answer == right_answer:
            tasks['tasks'][task_id]['taskState'] = f'Ебать мой лысый череп, ты чертовски прав, ответ {right_answer[0][0]}'
            return render_template('index.html', tasks=tasks)
        else:
            return render_template('index.html', tasks=tasks, answer='Not correct')

    return render_template('index.html', tasks=tasks)

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
