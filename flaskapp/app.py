from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "mysql"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "mypassword"
app.config["MYSQL_DB"] = "mydb"

mysql = MySQL(app)

@app.route("/persons", methods=["POST"])
def create_person():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO persons (name, age) VALUES (%s, %s)", (name, age))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "success", "message": "Person added"}), 201

@app.route("/persons", methods=["GET"])
def get_persons():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM persons")
    rows = cur.fetchall()
    cur.close()

    persons = []
    for row in rows:
        persons.append({"name": row[1], "age": row[2]})

    return jsonify(persons), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
