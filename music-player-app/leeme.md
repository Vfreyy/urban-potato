# Aplicación Reproductor de Música

Esta es una aplicación sencilla de reproductor de música diseñada para funcionar en computadoras y PC. Permite reproducir, pausar, detener música y gestionar una lista de reproducción mediante una interfaz gráfica intuitiva y fácil de usar.

## Estructura del Proyecto

```
music-player-app
├── src
│   ├── main.py                # Archivo principal, punto de entrada de la aplicación
│   ├── player
│   │   └── __init__.py        # Contiene la clase Player para controlar la reproducción de música
│   ├── ui
│   │   └── __init__.py        # Contiene la clase UserInterface para la interfaz gráfica de usuario
│   ├── utils
│   │   └── __init__.py        # Funciones auxiliares y utilitarias para la aplicación
│   └── types
│       └── index.py           # Definiciones de tipos y estructuras de datos utilizadas
├── requirements.txt           # Lista de dependencias necesarias para ejecutar el proyecto
└── README.md                  # Documentación del proyecto
```

### Explicación de la estructura

- **src/main.py**: Es el archivo principal que inicia la aplicación y conecta todos los módulos.
- **player/**: Aquí se encuentra la lógica para reproducir, pausar, detener y gestionar las canciones.
- **ui/**: Contiene el código de la interfaz pipgráfica, permitiendo al usuario interactuar fácilmente con el reproductor.
- **utils/**: Incluye funciones adicionales que ayudan en el funcionamiento general de la aplicación.
- **types/**: Define las estructuras de datos y tipos personalizados que se utilizan en el proyecto.
- **requirements.txt**: Archivo donde se especifican las librerías externas necesarias (por ejemplo, `pygame`, `tkinter`).
- **README.md**: Este archivo, donde se explica cómo usar y contribuir al proyecto.

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/Vfreyy/urban-potato.git
   cd music-player-app
   ```

2. Instala las dependencias necesarias:
   ```
   pip install -r requirements.txt
   ```

   > **Nota:** Asegúrate de tener Python instalado en tu computadora. Las dependencias incluyen librerías para la interfaz gráfica y la reproducción de audio.

## Uso

Para ejecutar la aplicación del reproductor de música, utiliza el siguiente comando en la terminal:

```
python src/main.py
```

Al iniciar, se abrirá una ventana donde podrás cargar archivos de música desde tu computadora, reproducirlos, pausarlos y detenerlos. La interfaz está diseñada para ser sencilla y accesible.

## Características

- **Reproducir, pausar y detener pistas de música:** Controla la reproducción de tus canciones favoritas.
- **Cargar archivos de música desde un directorio:** Selecciona y gestiona tus archivos MP3 locales.
- **Interfaz gráfica amigable:** Navega y controla la música fácilmente gracias a una ventana intuitiva.
- **Gestión de lista de reproducción:** Puedes agregar varias canciones y reproducirlas en el orden que prefieras.

