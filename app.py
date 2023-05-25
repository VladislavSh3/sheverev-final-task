from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/user/add', methods=['POST'])
def add_user():
    name = request.form['name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # Обернуть код в контекст приложения
        db.create_all()
    app.run(host='0.0.0.0')