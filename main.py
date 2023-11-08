import pymysql

from app import app
from config import mysql
from flask import jsonify
from flask import request

# flask 2.2.4
# Flask-Cors 3.0.10
# flask -MySQL 1.52

@app.route('/pais/create', methods=['POST'])
def create_pais():
    try:
        _json = request.json
        _name = _json['name']
        _capital = _json['capital']


        if _name and _capital  == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO pais(name, capital) VALUES(%s, %s)"
            bindData = (_name, _capital)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close()
            respone = jsonify('pais created successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:

        conn.close()


@app.route('/pais')
def employee():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, capital FROM pais")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


@app.route('/pais/<int:pais_id>')
def employee_details(pais_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, capital FROM pais WHERE id =%s", pais_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


@app.route('/pais/update', methods=['PUT'])
def update_employee():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _capital = _json['capital']

        if _name and _capital == 'PUT':
            sqlQuery = "UPDATE pais SET name=%s, capital=%s WHERE id=%s"
            bindData = (_name, _capital, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Pais updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


@app.route('/pais/delete/<int:pais_id>', methods=['DELETE'])
def delete_employee(pais_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pais WHERE id =%s", (pais_id,))
        conn.commit()
        respone = jsonify('Pais deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()