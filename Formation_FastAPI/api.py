
"""--------------------------------------------------------------
 Creation d'un environement de developpement de mon api
--------------------------------------------------------------

 les commandes de la creation 
-----------------------
- python venv nom_venv
  Ue code with caution.
(Cette commande dit à Windows : "Autorise l'exécution des scripts juste pour cette fenêtre de terminal").
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
 ./nom_venv/Scripts/activate
---------------------------------------------------------------------------------------------------------------------
"""

from fastapi import FastAPI
import uvicorn #POUR L'execution de fastapi
import numpy as np
import pandas as pd
import pickle
import json 
from pydantic import BaseModel  #Creation d'un type pour l'utilisation
 

app =FastAPI()  #Creation de l'API

class type_var(BaseModel) :
    age : float 
    bmi : float 
    bp  : float 
    s2  : float 
    s3  : float 
    s4  : float
    s5  : float
    s6  : float

#Chargement du model 
regmodel = pickle.load(open("regmodel.pkl", "rb"))
# scaler =   pickle.load(open("scaling_model.pkl", "rb"))  # Les tranformation sur le modele

#creationdu premier endpoint 
@app.get("/")

def accueil():
    return {"Message": "Bonjour le monde !!"}

## Deuxième point d'accès (Endpoint) : Récupération des données utilisateur pour effectuer des prédictions
@app.post("/predire")   #post permet de recuperer des info en entrer afin de faire les predictions(Fonction de prediction)

def prediction(Data : type_var):
    data  = pd.json_normalize(Data.dump())
    # data  = scaler.transform(data)
    prediction = regmodel.predict(data)
    return f"La prediction du diabete est : {prediction}"

# Vérifie si le script Python est exécuté directement par l'utilisateur.
# (La variable système __name__ prend la valeur "__main__" lors d'un lancement direct)
if __name__ == "__main__":
    
    # Lance le serveur Web Uvicorn en lui passant directement l'objet de l'application (app).
    # ATTENTION : Passer l'objet 'app' directement (au lieu de la chaîne "api:app") 
    # empêche l'utilisation de l'option 'reload=True' (rechargement automatique).
    uvicorn.run(app)
