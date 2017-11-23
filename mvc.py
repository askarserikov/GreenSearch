from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():  
    return render_template("index.html")

@app.route("/add/<int:first>/<int:second>")
@app.route("/add")
def add(first='',second=''):  
    if first == '':
        first = int(request.get("first"))
    if second == '':
        second = int(request.get("second"))
    result = first + second
    return render_template("index.html",result=result)

"""
@app.route("/send_data", methods=["GET","POST"])
def send_data():  
    data={"Eric Schles":"eric.schles@syncano.com",
          "job":"developer evangelist",
          "mission":"end slavery",
          "training for":"the olympics",
          "hobbies":["guitar","rock climbing"],
          "friends":"everyone"
          }
    return jsonify(data)

@app.route("/database")
def showdb():
    con = sql.connect('dataset.db')
    cur = con.cursor()
    result = cur.execute("SELECT * FROM dataset WHERE first_name = 'Alix'")
    fresult = result.fetchall()
    return jsonify(fresult)
"""

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        db = sql.connect('dataset.db')
        c = db.cursor()
        i = 0
        query = "SELECT * FROM dataset WHERE "
        if request.form['name']:
            query += "(first_name LIKE '%" + request.form['name'] + "%' OR last_name LIKE '%" + request.form['name'] +"%' )"
            i += 1
        if request.form['address']:
            if i > 0:
                query += "AND address LIKE '%" + request.form['address'] + "%' "
            else:
                query += "address LIKE '%" + request.form['address'] + "%' "
                i += 1
        if request.form['city']:
            if i > 0:
                query += "AND city LIKE '%" + request.form['city'] + "%' "
            else:
                query += "city LIKE '%" + request.form['city'] + "%' "
                i += 1
        if request.form['specialty']:
            if i > 0:
                query += "AND specialty LIKE '%" + request.form['specialty'] + "%' "
            else:
                query += "specialty LIKE '%" + request.form['specialty'] + "%' "
        print(query)
        c.execute(query)
        return render_template('results.html', records=c.fetchall())
    return render_template('search.html')
'''
@app.route('/results')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   user = request.form['email']
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>Welcome back, '+name+'</h1>'
'''

app.run(debug=True)  