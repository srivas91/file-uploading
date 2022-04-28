from app import app
from flask_mysqldb import MySQL

mysql = MySQL()

# MySQL configurations
def configuration():
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'company'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql = MySQL(app)
    return mysql