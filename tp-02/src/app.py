#importamos el modulo de flask para que funcione el proyecto
from flask import Flask, render_template, request, redirect, url_for

#importamos el modulo os para acceder mas facil a los directorios
import os

# importamos para la base de datos
import database as db

#definimos la ruta absoluta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unimos las rutas de las carpetas src y templates a la ruta del proyecto de la línea anterior
template_dir = os.path.join(template_dir, 'src', 'templates')

#indicamos que se busque el archivo index.html (en carpeta templates) al lanzar la aplicación
app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
# @app.route('/') es un decorador que vincula una función con una URL específica del sitio web. En este caso, '/' representa la ruta raíz o homepage del sitio web.

# La función home() que sigue al decorador es la que se ejecutará cuando un usuario visite la página principal (homepage) del sitio. La declaración return render_template('index.html') dentro de esta función indica que Flask debe buscar y renderizar el archivo HTML llamado index.html, que generalmente contiene el contenido que se mostrará en la página principal del sitio web.

# IMPORTANTE: importar en la linea 2 del codigo el modulo render_template para lanzar la pagina index.html. Debe quedar asi:
# from flask import Flask, render_template


# cursor es un objeto que apunta a la base de datos y nos permitira interactuar con el. database es el nombre de la variable que se encuentra en el archivo database.py y que contiene toda la informacion de conexion a la base de datos.

#  cursor.execute("SELECT * FROM users") ejecuta la consulta sql a la base de datos

# el metodo fetchall toma todos los registros devueltos en la ejecucion de la consulta anterior y guarda el resultado en la variable miResultado.

# insertarObjectos = [] crea una lista vacia

# nombreDeColumnas = [columna[0] for columna in cursor.description]
# Los nombres de las columnas se obtienen de cursor.description y los guarda en la variable nombreDeColumnas.

# for unRegistro in miResultado:
#     insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
# Recorre cada registro del resultado de ejecutar la consulta y lo convierten en un diccionario. Esto se hace mediante el uso de zip() para emparejar los nombres de las columnas con los valores de cada registro. 

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas,unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('index.html', data=insertarObjectos)



#Ruta para guardar usuarios en la bd
@app.route('/usuario', methods=['POST'])
def usuario():
    destino = request.form['destino']
    excursion = request.form['excursion']
    precio = request.form['precio']

    if destino and excursion and precio:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios(destino, excursion, precio) VALUES (%s, %s, %s)"
        data = (destino, excursion, precio)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


@app.route('/eliminar/<string:id>')
def eliminar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/editar/<string:id>', methods=['POST'])
def editar(id):
    destino = request.form['destino']
    excursion = request.form['excursion']
    precio = request.form['precio']

    if destino and excursion and precio:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET destino = %s, excursion = %s, precio = %s WHERE id = %s"
        data = (destino, excursion, precio, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


#ejecucion directa de este archivo en modo de desarrollador en el puerto 4000 del localhost o servidor local creado por flask.
if __name__ == '__main__':
    app.run(debug=True, port=4000)


