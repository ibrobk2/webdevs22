from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/todoapp'

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'
    

db.create_all()

@app.route('/todos/add', methods=['POST'])
def add_todo():
    # description = request.form.get('description', '')
    description = request.get_json()['description']
    
    try:
        
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
    except:
        db.session.rollback()
        error=True
        print(sys.exc_info())
    finally:
        db.session.close()
    # return redirect(url_for('index'))
    return jsonify({
        'description': todo.description
    })


@app.route('/')

def index():
    return render_template('index.html', data = Todo.query.all())
    
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)