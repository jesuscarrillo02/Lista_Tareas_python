Explicacion rapida de la aplicacion:

es una aplicacion wed que al ejecutarse de transmitira en el puerto 5000, esta tiene dos paginas principales, la primera sinedo     donde estara el formualrio para poder registrar nuevas tareas junto con la tabla que muestra la lista de registros de cada una de las tareas, esta funciona con sqlite con un archivo interno que contiene la base de datos ubicado en la carpeta "instance".

Requerimientos:

antes de procedes con el arranque del proyecto primero deveras de construir un entorno virtual, para ello utiliza debera de ir al directorio donde guarde los archivos correspondiente al poryecto y debera de insertar el comando "python -m virtualenv env" en la terminal de tu proyecto, luego deberas de utilizr el comando  "pip install" para instalar las bibliotecas utilizadas, estas estaran en el archivo "requeriments.txt" hay se encunetran las bibliotecas y extenciones utilizadas para el proyecto.

Instrucciones:

1.-Para ejecutar la aplicacion debes de ir a tu visual studio.

2.-Pulsa en "archivo" en visual studio, pincha en "abrir carpeta" y busca la carpeta correspondiente al proyecto
![alt text](/Img_aplicacion/Buscar%20carpeta.png)

3.- abre la terminal de Visual studio y ejecuta el comando "python index.py", es necesario tener activado tu lector de python en la
aplicacion, de no tenerlo es necesario instalarlo. ![alt text](/Img_aplicacion/Comando%20Python.png)

4.-Abre tu navegador y en tu barra superior coloca esto "http://localhost:5000"

5.-Se desplegaran la pagina donde se ejecuta la aplicacion puedes empezar creando un regisyto
![alt text](/Img_aplicacion/image-1.png)

6.-para crear un registro en el formulario de la derecha coloca la informacion solicitada y preciona el boton "guardar"

7.- para editar un registro debes de precionar el primer boton que esta en la tabla y debera rellenar el formualrio para 
editar el registro, ![alt text](/Img_aplicacion/Edicion_registros.png)

8.- para eliminar un registro la tarea debe de estar en estado "Finalizado" para ello preicona el boton que esta al lado de editar
![alt text](/Img_aplicacion/Finalizar_tarea.png)

9.- Al cambiar el estado a "Finalizado" pincha en el ultimo boton de la tabla que tiene un icono de basurero para eliminar el registro.

10.- para importar regsitro solo debes de precionar el boton "Importar datos"

11.- para esportarlos preciones en el seleccionde archivo y escoja el archivo de formato json despues solo presion en "exportar archivo"

Imagen de los resultados de la evaluacion por SonarQube con librerias: ![alt text](/Img_aplicacion/image.png)

Imagen de los resultados de la evaluacion por SonarQube sin librerias: ![alt text](/Img_aplicacion/Captura%20de%20evaluacion%20SonarQube.png)
