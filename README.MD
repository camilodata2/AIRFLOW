# Apache Airflow 🌬️
## Descripción
Apache Airflow es una plataforma de código abierto para la programación, monitoreo y gestión de flujos de trabajo (workflows). Permite definir, ejecutar y monitorear flujos de trabajo complejos de una manera fácil y flexible.
Conceptos clave
* BashOperator 💻: BashOperator permite ejecutar comandos de shell como parte de un flujo de trabajo en Airflow. Esto es útil para realizar tareas como ejecutar scripts, comandos de sistema o cualquier acción que se pueda realizar desde la línea de comandos.
* PythonOperator 🐍 :PythonOperator ejecuta funciones o scripts de Python como tareas dentro de un flujo de trabajo. Permite aprovechar la flexibilidad y funcionalidades de Python para realizar tareas personalizadas, manipular datos, conectarse a servicios externos, entre otras acciones.
* XComs (Cross-Communication) 🔄: XComs son un mecanismo de comunicación entre tareas en Airflow. Permiten compartir datos entre tareas, lo que facilita el intercambio de información o resultados entre diferentes pasos de un flujo de trabajo. Los valores se almacenan en la base de datos de metadatos de Airflow, lo que permite acceder a ellos entre ejecuciones de flujos de trabajo.
* Taskflow 🛠️: Taskflow es un paradigma de programación en Airflow que ofrece una abstracción más alta y simplificada para la creación de flujos de trabajo. En lugar de definir DAGs con operadores individuales y dependencias explícitas entre ellos, Taskflow permite definir flujos de trabajo utilizando estructuras de control de flujo más comunes y familiarizadas como bucles, condicionales y funciones.

Algunos conceptos importantes en Taskflow son:

* BaseTask: Un BaseTask es una unidad de trabajo en Taskflow. Puede ser un operador Airflow o una función de Python. Cada BaseTask se encarga de una parte del flujo de trabajo y puede tener dependencias con otras tareas.

* Taskflow API: La API de Taskflow permite definir flujos de trabajo usando estructuras de control más familiares como if, for, while y subdags, facilitando la lógica compleja en los flujos de trabajo.

* BranchPythonOperator: Es un operador en Taskflow que permite bifurcar el flujo del DAG basado en la salida de una función Python.

* XComPuller: Un componente que permite a las tareas en un flujo de trabajo acceder a los valores de XCom de tareas anteriores.

* Decorrators: En Taskflow, los decoradores se utilizan para definir cómo se deben ejecutar las tareas y manejar sus resultados.

* Retries y reintentos: Taskflow permite definir reglas personalizadas para reintentar tareas o flujos de trabajo completos cuando se produce un error.

* Taskflow proporciona una abstracción más poderosa y flexible para definir flujos de trabajo complejos en Airflow, simplificando la lógica y facilitando la comprensión y mantenimiento de DAGs más elaborados.
### Custom Operators, Hooks y Sensor 🛠️
Custom Operators: Los Custom Operators son extensiones de Airflow que permiten a los usuarios definir sus propios operadores personalizados para adaptarse a casos de uso específicos. Esto puede ser útil cuando las tareas estándar de Airflow no son suficientes y se requiere funcionalidad adicional.
* Hooks: Los Hooks son interfaces de bajo nivel para interactuar con servicios externos desde Airflow. Permiten a los desarrolladores crear conexiones personalizadas a sistemas externos y realizar operaciones como consultas a bases de datos, llamadas a API, envío de correos electrónicos, entre otros.

* Sensor: Los Sensores son operadores especiales en Airflow que esperan ciertas condiciones antes de continuar con el flujo de trabajo. Por ejemplo, un Sensor de archivo podría esperar a que un archivo aparezca en un directorio antes de que una tarea pueda ejecutarse. Los Sensores son útiles para esperar eventos externos o condiciones específicas antes de ejecutar tareas.