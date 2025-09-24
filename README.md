# Asistente-virtual-UIEPCH
Este es un proyecto de titulación para la carrera de ingeniería en sistemas computacionales, el cual trata sobre el desarrollo de un asistente virtual. Este ayudara a los estudiantes de nuevo ingreso a consultar información de manera rapida y precisa a cerca de temas relacionados con la universidad. Esto con el uso de unas de las tecnologias mas usadas en estos tiempos la AI. A continuacion, se mostraran un pequeño preview de como luce:
<br />

# Screenshot
<figure>
  <img width="1700" height="923" alt="Image" src="https://github.com/user-attachments/assets/c0b7394e-9551-413a-b035-14746d2c4527" />
</figure>
<br />

# Mobile version 
<p align="center" width="100%">
  <img  width="350" height="700" alt="Image" src ="https://github.com/user-attachments/assets/9e2f5d62-a8df-46ea-82a1-43233553c30e" />
</p>


# Requisitos previos :D
Debes de tener instalado dentro de tu equipo una version de python compatible con las librerias, yo recomiento la 3.11.9 para que no exista conflicto alguno.
Despues en caso de tener mas proyectos que pudieran chocar con algunas dependencias ya instaladas se recomienda crear un entorno virtual para este, por ejemplo:
<br />

```shell
python -m venv nombre del entorno
```

Para poner utilizar este proyecto es necesario instalar las siguientes librerias dentro de la terminal del proyecto, asegurandose que se encuentre dentro del entorno creado.
<br />
<ul style="list-style-type: none;">
  <li>pip install streamlit</li>
  <li>pip install openai</li>
  <li>pip install langchain</li>
  <li>pip install embeddings</li>
</ul>

Una vez configurado el entorno se necesitara la creacion de la API de openAI. Esta se crea directamente desde la pagina oficial en donde debes
dirigirte a la opcion de ajustes. Una vez alli buscar la opcion de **"API keys"** y seleccionar la opcion de **"create new secret key"** y automaticamente se creara una. **No debes compartir esta pues podrian hacer mal uso de ella.**Puedes ingresar a la pagina con el siguiente link [OpenAI](https://platform.openai.com/docs/overview).
<br />
Esto es solo para agregar la api despues deberan de agregar saldo a una cartera digital propia de OpenAI la cual sirve para hacer las llamadas a la API y que el LLM responda.
Esta seccion se encuentra en el lado izquierdo en el apartado de **"Billing"**. Una vez dentro darle clic a la opcion de **"Add to credit balance"** y agregar un metodo de pago y el monto a depositar. Una vez hecho esto la API ya tendra funcionalidad y podra ser usada para contestar las preguntas que le sean puestas.
<br />
<figure>
  <img width="1801" height="849" alt="Image" src="https://github.com/user-attachments/assets/05a686e2-d56e-4216-9755-dcdfb67ccd36" />
</figure>
