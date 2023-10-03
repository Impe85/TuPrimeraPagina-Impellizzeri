# TuPrimeraPagina-Impellizzeri:

La pagina es un sitio de Arqueria:

Contenido:

Se creo una 'ArcheryEquipmentApp':
-Tiene tres campos name, manufacturer y description
-Los dos primeros son CharField y el ultimo TextField

Se Creo una carpeta Template que tiene dentro de ella dos carpetas una con el nombre inicio y la otra con el nombre Shared
-inicio: Contiene el inicio.html (Herencia html)
-Shared: Contiene el index.html (Base)

En models.py se creo la clase 'ArcheryEquipment'

Se creo en la carpeta inicio/forms.py
-Este incluye la creacion de la clase 'ArcheryEquipmentForm' y los campos que creamos en 'ArcheryEquipment'

En la carpeta inicio/views.py se definio nuestra funcion add_equipment

Se creo la carpeta static para usar el contenido descargado de Bootstrap
- Se cambio en la carpeta assets/img la imagen con el nombre bg-masthead con una imagen del contexto de la pagina.

- Se Creo el archivo requirements.txt con la version de entorno virtual que estamos usando para emular el sitio.


Nota: Se creo el archivo ignore para la hora de la subida de los archivos y el enlace para compartir con el gente en GitHub.

Author: Martin Impellizzeri