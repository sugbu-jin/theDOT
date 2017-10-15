# -*- coding: cp1252 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'Welcome to Home'

@app.route('/admin/')
def admin():
   return 'Admin Page'

@app.route('/guest/<guest>')
def guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/category/')
def category():
   return 'Category Page'

@app.route('/category/tech/')
def tech():
   return 'Category: Technology Page'
@app.route('/category/tech/<subject>')
def tech_specific(subject):
   return 'Technology: the DOT of %s' % subject

@app.route('/category/people/')
def people():
   return 'Category: People Page'
@app.route('/category/people/<subject>')
def people_specific(subject):
   return 'People: The DOT of %s' % subject


@app.route('/category/<category>/<subject>')
def category_mapper(category):
   if category =='tech':
      return redirect(url_for('tech', tech = subject))
   else:
      return redirect(url_for('people',guest = subject))


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('admin'))
   else:
      return redirect(url_for('guest',guest = name))

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
