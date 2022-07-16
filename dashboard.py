# Import des librairies utiles

import requests
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import json


def main():

    API_URL = "http://127.0.0.1:5000/"  # "https://flask-api-p7.herokuapp.com/" 
    
    st.subheader("Prédiction sur le joueur choisis")

    st.markdown("Renseignez les statistiques sportives du joueur")

    # Statistiques à choisir par l'utilisateur (toutes les variables)
    
    GP = st.number_input("Games played ", min_value=0.0,max_value=100.0)
    MIN = st.number_input("Minutes played ", min_value=0.0,max_value=100.0)
    PTS = st.number_input("Points per Game ", min_value=0.0,max_value=100.0)
    FGM = st.number_input("Field Goals Made", min_value=0.0,max_value=100.0)
    FGA = st.number_input("Field Goals Attempts", min_value=0.0,max_value=100.0)
    FGper = st.number_input("Field Goals Percent", min_value=0.0,max_value=100.0)
    _3P_Made = st.number_input("3 Points Made", min_value=0.0,max_value=100.0)
    _3PA = st.number_input("3 Points Attempts", min_value=0.0,max_value=100.0)
    _3Pper = st.number_input("3 Points Percent", min_value=0.0,max_value=100.0)
    FTM = st.number_input("Free Throw Made", min_value=0.0,max_value=100.0)    
    FTA = st.number_input("Free Throw Attempt", min_value=0.0,max_value=100.0)
    FTper = st.number_input("Free Throw Percent", min_value=0.0,max_value=100.0)
    OREB = st.number_input("Offensive Rebounds", min_value=0.0,max_value=100.0)
    DREB = st.number_input("Defensive Rebounds", min_value=0.0,max_value=100.0)
    REB = st.number_input("Rebounds", min_value=0.0,max_value=100.0)
    AST = st.number_input("Assists", min_value=0.0,max_value=100.0)
    STL = st.number_input("Steals", min_value=0.0,max_value=100.0)
    BLK = st.number_input("Blocks", min_value=0.0,max_value=100.0)
    TOV = st.number_input("Turnovers", min_value=0.0,max_value=100.0)
    
    st.write('Les statistiques entrées : ', (GP,MIN,PTS,FGM,FGA,FGper,_3P_Made,_3PA,_3Pper,FTM,FTA,FTper,OREB,DREB,REB,AST,STL,BLK,TOV))
    
    
    
    # On charge la prédiction faite par requête sur l'API
    
    def chargement_prediction():

        prediction = requests.get(API_URL + "predict", params={"GP":GP, "MIN":MIN, "PTS":PTS, "FGM":FGM, "FGA":FGA, "FGper":FGper, "_3P_Made":_3P_Made, "_3PA":_3PA, "_3Pper":_3Pper, "FTM":FTM, "FTA":FTA, "FTper":FTper, "OREB":OREB, "DREB":DREB, "REB":REB, "AST":AST, "STL":STL, "BLK":BLK, "TOV":TOV})
        
        prediction = prediction.json()

        return prediction
    
    
    
    # Affichage de la prédiction
    
    prediction = chargement_prediction()
    
    if prediction == 1:
        st.subheader("--- > Prédiction : "+ "Le joueur aura une longue carrière en NBA")
    else:
        st.subheader("--- > Prédiction : "+ "Le joueur n'aura pas une longue carrière en NBA")

    

if __name__== '__main__':
    main()