from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

db = mysql.connector.connect(
    host="db",  # MySQL 서비스 이름 (docker-compose에서 db 서비스)
    user="root",  # 기본 root 사용자 사용
    password="rootpassword",  # 기본 root 비밀번호
    database="mydatabase"  # 기본 데이터베이스
)

cursor = db.cursor()

def setup_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/stacks')
    def stacks():
        return render_template('stacks.html')

    @app.route('/project')
    def project():
        return render_template('project.html')

    @app.route('/contact')
    def contact():
        cursor.execute("SELECT idx, name, context FROM board WHERE currentstatus = 1 ORDER BY idx DESC")
        posts = cursor.fetchall()
        return render_template('contact.html', posts=posts)

    @app.route('/add_post', methods=['POST'])
    def add_post():
        name = request.form['name']
        pw = request.form['pw']
        context = request.form['context']
        
        cursor.execute("INSERT INTO board (name, pw, context) VALUES (%s, %s, %s)", (name, pw, context))
        db.commit()
        
        return redirect(url_for('contact'))

    @app.route('/delete_post/<int:idx>', methods=['POST'])
    def delete_post(idx):
        pw = request.form['pw']

        cursor.execute("SELECT pw FROM board WHERE idx = %s", (idx,))
        stored_pw = cursor.fetchone()  
        if stored_pw is None:
            return "게시글을 찾을 수 없습니다.", 404

        stored_pw_value = stored_pw["pw"] if isinstance(stored_pw, dict) else stored_pw[0]

        if stored_pw_value == pw:
            cursor.execute("UPDATE board SET currentstatus = 0 WHERE idx = %s", (idx,))
            db.commit()

        return redirect(url_for('contact'))
