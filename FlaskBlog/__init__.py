from flask import Flask

import pymysql
import os

conn = pymysql.connect(host="localhost",user="root",passwd="",db="gmao")

app = Flask(__name__)
app.secret_key = os.urandom(24)
 

from FlaskBlog import Compte
from FlaskBlog import intervention
from FlaskBlog import machine
from FlaskBlog import maintenance
from FlaskBlog import Personne
from FlaskBlog import session


