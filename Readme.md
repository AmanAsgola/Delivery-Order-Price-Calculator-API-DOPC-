#Python Version 3.12

1.Installation (Windows):


Create and activate a virtual environment: # you can skip this and directly install dependencies on PC or Laptop as it is already in zip file
    
	python -m venv dopc_env

	
	.\dopc_env\Scripts\activate.ps1  # for vs Code

Install Dependencies:
	pip install -r requirements.txt 


2.Running the API

Start Server (in terminal):
	uvicorn main:app --reload

Access the API Documentation (Browser):
	http://127.0.0.1:8000/docs


# Notes


	Ensure the API endpoints used in config.py are live and accessible.

	The API is built assuming specific data structures from the endpoints. Adjust as necessary for your use case.