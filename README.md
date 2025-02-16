
<h1> Taximeter</h1>

# Index

+ [Description](#description)
+ [Project Configuration](#project-Configuration)
+ [Logging System](#Logging-System)
+ [Test](#test)
+ [Project Structure ](#project-structure)
+ [Technologies](#technologies)
+ [Authors](#authors)
+ [Contributions](#contributions)

# Descripcción

<p>Taximeter is a command-line application that allows users to record taxi trips, including pauses, and calculate the total cost based on the time spent moving and paused.</p>

## Project Configuration

1. **Clone the Repository:**

`bash`
* Copy code in your terminal: `git clone https://github.com/Nho89/Taximetro.git`
* Copy code in your terminal: `cd Taximetro` <br>
To enter the repository folder.


2. **(Optional) Create a virtual environment:**
   
`bash`   
* Copy code: `python -m venv venv`
* Copy code: `source .venv/Scripts/activate`


3. **Install Dependencies:** 

`bash`
* Copy code: `pip install -r requirements.txt`

4. **Running the Application**

`bash`
* Copy code: `python app.py`

## Logging System

* Each trip is logged in the .taximeter.log file with the following format:

- --- Resumen del viaje 🧳---
- 📆 Fecha: 2025-02-16 22:31:09
- ⌛ Duración total del viaje: 0.53 minutos
- 🚕 Tiempo en movimiento: 0.53 minutos
- ⏸️ Tiempo parado: 0.0 minutos
- 💰 El costo total del viaje es: 5,10 €


## Test

`bash`
* Copy code: `python -m unittest`
This will run the tests.


## Project Structure 

* __app.py:__  Application entry point.
* __test_app.py:__ file with unit tests of the application.
* __.taximeter.log:__ system log file.
* __requirements.txt:__ Project dependencies.
* __.gitignore:__ Files ignored by Git.
* __README.md:__ Project documentation.


# Technologies

<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/visual_studio_code.png" >&nbsp;
<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png" >&nbsp;
<img width="50" src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg">&nbsp;



# Authors

 - Web Developer: [Nhoeli Salazar](https://github.com/Nho89)


# Contributions
Contributions are welcome! If you find any problems or have suggestions for improvement, please create an issue or make a pull request.
   
**[⬆️ Back to Index](#index)**
