from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
import utils

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    data = utils.pega_notas()
    return render_template("index.html",datas=data)


@app.route("/add_user",methods=['POST','GET'])
def add_note():
    if request.method=='POST':
        utils.adiciona_nota()
        return redirect(url_for("index"))
    return render_template("add_note.html")


@app.route("/edit_note/<string:uid>",methods=['POST','GET'])
def edit_note(uid):
    if request.method=='POST':
        utils.editar_nota(uid)
        return redirect(url_for("index"))
    
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where UID=?",(uid,))
    data=cur.fetchone()
    con.close()
    return render_template("edit_note.html",datas=data)
    

@app.route("/delete_note/<string:uid>",methods=['GET'])
def delete_note(uid):
    utils.deletar_nota(uid)
    return redirect(url_for("index"))
    

if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)