from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'development'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'Virtual'
app.config['MYSQL_DATABASE_HOST'] = '192.168.0.21'
mysql.init_app(app)
