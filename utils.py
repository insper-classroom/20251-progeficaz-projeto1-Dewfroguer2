import sqlite3 as sql
from flask import request,redirect,url_for,flash


def pega_notas():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return data

def adiciona_nota():
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("insert into users(TITULO,DETALHES) values (?,?)",(titulo,detalhes))
        con.commit()
        flash('Note Added','success')
        


def editar_nota(uid):
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("update users set TITULO=?,DETALHES=? where UID=?",(titulo,detalhes,uid))
        con.commit()
        flash('Note Updated','success')
       

def deletar_nota(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from users where UID=?",(uid,))
    con.commit()
    flash('Note Deleted','warning')