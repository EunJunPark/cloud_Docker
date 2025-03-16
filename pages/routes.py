from flask import Flask, render_template, request, redirect, url_for
from db.db import get_cursor

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
        """ DB에서 게시글을 가져와서 contact.html에 전달 """
        cursor, db = get_cursor()
        cursor.execute("SELECT idx, name, context FROM board WHERE currentstatus = 1 ORDER BY idx DESC")
        posts = cursor.fetchall()
        db.close()  # DB 연결 닫기
        
        return render_template('contact.html', posts=posts)

    @app.route('/add_post', methods=['POST'])
    def add_post():
        """게시글 추가"""
        name = request.form.get('name')
        pw = request.form.get('pw')
        context = request.form.get('context')

        if not name or not pw or not context:
            return redirect(url_for('contact'))  # 필수 값이 없으면 등록하지 않음

        cursor, db = get_cursor()
        cursor.execute("INSERT INTO board (name, pw, context) VALUES (%s, %s, %s)", (name, pw, context))
        db.commit()  # 변경 사항 저장
        db.close()   # DB 연결 닫기

        return redirect(url_for('contact'))

    @app.route('/delete_post/<int:idx>', methods=['POST'])
    def delete_post(idx):
        return redirect(url_for('contact'))
