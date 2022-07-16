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

@API.route("/predict", methods=["GET"])
def predict():
    
    # Variables choisises par l'utilisateur
    GP = request.args.get("GP")
    MIN = request.args.get("MIN")
    PTS = request.args.get("PTS")
    FGM = request.args.get("FGM")
    FGA = request.args.get("FGA")
    FGper = request.args.get("FGper")
    _3P_Made = request.args.get("_3P_Made")
    _3PA = request.args.get("_3PA")
    _3Pper = request.args.get("_3Pper")
    FTM = request.args.get("FTM")
    FTA = request.args.get("FTA")
    FTper = request.args.get("FTper")
    OREB = request.args.get("OREB")
    DREB = request.args.get("DREB")
    REB = request.args.get("REB")
    AST = request.args.get("AST")
    STL = request.args.get("STL")
    BLK = request.args.get("BLK")
    TOV = request.args.get("TOV")
    
    # Mise en forme et transformations des statistiques pour la prédiction
    stat_joueur = np.array([GP,MIN,PTS,FGM,FGA,FGper,_3P_Made,_3PA,_3Pper,FTM,FTA,FTper,OREB,DREB,REB,AST,STL,BLK,TOV])  
    stat_joueur = stat_joueur.reshape(1,19)
    stat_joueur_scaled = scaler.transform(stat_joueur)
    
    # Prédiction
    return jsonify(modele_optimal_loaded.predict(stat_joueur_scaled).tolist()[0])




if __name__ == "__main__":
    API.run()