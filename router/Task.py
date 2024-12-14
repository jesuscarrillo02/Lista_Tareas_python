import json, os
from io import BytesIO
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_file
from models.TaskModel import Task
from utils.db import db

task =Blueprint('Tareas', __name__)

@task.route('/')
def home():
    taskList = Task.query.all()
    return render_template('index.html', taskList = taskList)

#Añadir nueva tarea
@task.route('/create_task', methods=['POST'])
def NewTask():
    try:
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        estado = request.form['Estado']
        new_task = Task(titulo, descripcion, estado)
        
        db.session.add(new_task)
        db.session.commit()
        
        flash("Se añadió una nueva tarea") # Mensaje de éxito
        
    except KeyError as e:
        flash(f"Error: Faltan datos en el formulario ({e}).", "error")
        
    except Exception as e:
        db.session.rollback()  # Revierte accion en caso de error
        flash(f"Ocurrió un error al crear la tarea: {e}", "error")

    return redirect(url_for('Tareas.home'))

#Actualizar tarea
@task.route('/update_Task/<id>', methods=['POST', 'GET'])
def UpdTask(id):
    
    try:
        if request.method == 'POST':
            task = Task.query.get(id)
            task.titulo = request.form['titulo']
            task.descripcion = request.form['descripcion']
            task.estado = request.form['Estado']
            
            db.session.commit()
            flash("Se Actualiza la tarea correctamente")
            return redirect(url_for('Tareas.home'))
    
        task = Task.query.get(id)
        return render_template('update.html', task = task)#identificador para los datos en  el formualrio

    except KeyError as e:
        # Maneja errores de claves faltantes en el formulario
        flash(f"Error: Faltan datos en el formulario ({e}).", "error")
    except Exception as e:
        # Manejo de errores generales
        db.session.rollback()  # Revertir transacciones en caso de error
        flash(f"Ocurrió un error al actualizar la tarea: {e}", "error")
    return redirect(url_for('Tareas.home'))
    
#Terminar elimianr tarea 
@task.route('/delete_task/<id>')
def DelTask(id):
    task_del = Task.query.get(id)
    db.session.delete(task_del)
    db.session.commit()
    flash("Se elimino la tarea correctamente")
    
    return redirect(url_for('Tareas.home'))

#Finalizar tarea
@task.route('/endtask/<id>')
def EndTask(id):
    task = Task.query.get(id)
    task.estado = 'Finalizado'
    db.session.commit()
    
    flash("Tarea finalizada")
    return redirect(url_for('Tareas.home'))

#Exportar tareas
@task.route('/export_tasks', methods=['GET'])
def export_tasks():
    try:
        tasks = Task.query.all()
        data = [
            {"titulo": task.titulo, "descripcion": task.descripcion, "estado": task.estado}
            for task in tasks
        ]
        json_data = BytesIO(json.dumps(data, indent=4).encode('utf-8'))
        
        return send_file(
            json_data,
            as_attachment=True,
            download_name="tareas.json",
            mimetype="application/json"
        )            
     
    except Exception as e:
        flash(f"Error al exportar tareas: {e}", "error")
        return redirect(url_for('Tareas.home'))
 
#Importar tareas    
@task.route('/import_tasks', methods=['POST'])
def import_tasks():
    try:
        file = request.files['file']

        # Verifica si se ha subido un archivo válido
        if file.filename == '':
            flash("No se seleccionó ningún archivo", "error")
            return redirect(url_for('Tareas.home'))
        
        # Lee el contenido del archivo
        file_content = file.read()
        
        # Decodifica el JSON
        data = json.loads(file_content)

        # Verifica que sea una lista de tareas y procesa los datos
        if isinstance(data, list):
            for task in data:
                # Crear un nuevo objeto Task a partir del JSON
                new_task = Task(
                    titulo=task.get('titulo', 'Sin título'),
                    descripcion=task.get('descripcion', 'Sin descripción'),
                    estado=task.get('estado', 'pendiente')
                )
                # Agrega la tarea a la base de datos
                db.session.add(new_task)

            # Guarda los cambios en la base de datos
            db.session.commit()

            flash("Tareas importadas exitosamente", "success")
        else:
            flash("El archivo JSON no tiene el formato esperado", "error")
            return redirect(url_for('Tareas.home'))
    
    except Exception as e:
        flash(f"Error al exportar tareas: {e}", "error")
        return redirect(url_for('Tareas.home'))

    # Redirige a la página de inicio o a otra vista
    return redirect(url_for('Tareas.home'))