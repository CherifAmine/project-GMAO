from flask import render_template, request, redirect, url_for , session, g
from FlaskBlog import conn

#Initialisation des variables
from FlaskBlog import app




@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('Test_Compte'))
    


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
