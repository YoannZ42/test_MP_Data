# -*- coding: utf-8 -*-

# Import des librairies utiles

from flask import Flask, jsonify, request
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import joblib
import warnings
import pickle
warnings.filterwarnings("ignore", category=UserWarning)


# On charge le modèle optimal et le transformateur nécessaire

modele_optimal_loaded = joblib.load('modele_optimal.joblib')
scaler = pickle.load(open('scaler.sav', 'rb'))

# Prédiction en fonction des statistiques sportives choisies par l'utilisateur

API = Flask(__name__)

@API.route("/")
def initialisation():
    return "Test"

@API.route("/predict", methods=["GET"])
def predict():
    
    # Variables choisies par l'utilisateur
    GP = request.args.get("GP")
    FGM = request.args.get("FGM")
    FGper = request.args.get("FGper")
    _3P_Made = request.args.get("_3P_Made")
    _3Pper = request.args.get("_3Pper")
    FTper = request.args.get("FTper")
    REB = request.args.get("REB")
    AST = request.args.get("AST")
    STL = request.args.get("STL")
    BLK = request.args.get("BLK")

    
    # Mise en forme et transformations des statistiques pour la prédiction
    stat_joueur = np.array([GP,FGM,FGper,_3P_Made,_3Pper,FTper,REB,AST,STL,BLK])  
    stat_joueur = stat_joueur.reshape(1,10)
    stat_joueur_scaled = scaler.transform(stat_joueur)
    
    # Prédiction
    return jsonify(modele_optimal_loaded.predict(stat_joueur_scaled).tolist()[0])




if __name__ == "__main__":
    API.run()