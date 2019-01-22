import os
import sys
import flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pymysql
pymysql.install_as_MySQLdb()

