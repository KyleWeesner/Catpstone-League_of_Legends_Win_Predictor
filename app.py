import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

st.title("League of Legends Win Predictor")

st.write("## This app will predict the chance of your team winning at 15 mins.")

team = st.selectbox("Which team are you on?",
    options=['Blue', 'Red'])
col1, col2 = st.columns(2)

with col1:
    blue_team_kills = st.number_input("Number of Blue Team Kills?", min_value=0, max_value=100)
    blue_team_visionScore = st.number_input("Sum of Blue Team VisionScore?", min_value=0, max_value=100)
    blue_team_assists = st.number_input("Number of Blue Team Assists?", min_value=0, max_value=100)
    blue_team_cs = st.number_input("Sum of Blue Team Creep Score?", min_value=0, max_value=600)
    blue_team_level = st.number_input("Sum of Blue Team Levels?", min_value=5, max_value=80)
    blue_dragons_slained = st.number_input("Number of Blue Team Dragons Slained?", min_value=0, max_value=2)
    blue_rift_heralds_slained = st.number_input("Number of Blue Team Rift Heralds Slained?", min_value=0, max_value=2)
    blue_AIR_DRAGON = st.number_input("Number of Blue Team air drags?", min_value=0, max_value=1)
    blue_EARTH_DRAGON = st.number_input("Number of Blue Team earth drags?", min_value=0, max_value=1)
    blue_FIRE_DRAGON = st.number_input("Number of Blue Team fire drags?", min_value=0, max_value=1)
    blue_HEXTECH_DRAGON = st.number_input("Number of Blue Team hextech drags?", min_value=0, max_value=1)
    blue_WATER_DRAGON = st.number_input("Number of Blue Team water drags?", min_value=0, max_value=1)
    blue_inhibitors_destroyed = st.number_input("Number of Blue Team Inhibitors Destroyed?", min_value=0, max_value=3)
    blue_towers_destroyed = st.number_input("Number of Blue Team Towers Destroyed?", min_value=0, max_value=11)



with col2:
    red_team_kills = st.number_input("Number of Red Team Kills?", min_value=0, max_value=100)
    red_team_visionScore = st.number_input("Sum of Red Team VisionScore?", min_value=0, max_value=100)
    red_team_assists = st.number_input("Number of Red Team Assists?", min_value=0, max_value=100)
    red_team_cs = st.number_input("Sum of Red Team Creep Score?", min_value=0, max_value=600)
    red_team_level = st.number_input("Sum of Red Team Levels?", min_value=5, max_value=80)
    red_dragons_slained = st.number_input("Number of Red Team Dragons Slained?", min_value=0, max_value=2)
    red_rifts_heralds_slained = st.number_input("Number of Red Team Rift Heralds Slained?", min_value=0, max_value=2)
    red_AIR_DRAGON = st.number_input("Number of Red Team air drags?", min_value=0, max_value=1)
    red_EARTH_DRAGON = st.number_input("Number of Red Team earth drags?", min_value=0, max_value=1)
    red_FIRE_DRAGON = st.number_input("Number of Red Team fire drags?", min_value=0, max_value=1)
    red_HEXTECH_DRAGON = st.number_input("Number of Red Team hextech drags?", min_value=0, max_value=1)
    red_WATER_DRAGON = st.number_input("Number of Red Team water drags?", min_value=0, max_value=1)
    red_inhibitors_destroyed = st.number_input("Number of Red Inhibitors Destroyed?", min_value=0, max_value=3)
    red_towers_destroyed = st.number_input("Number of Red Towers Destroyed?", min_value=0, max_value=11)


f=open('./Untitled_Folder/best_model_logreg_T', 'rb')
loaded_model=pickle.load(f)
f.close()


def win_proba(team,blue_team_kills,red_team_kills,blue_team_visionScore,red_team_visionScore,blue_team_assists,red_team_assists,blue_team_cs,red_team_cs,blue_team_level,red_team_level,blue_dragons_slained,red_dragons_slained,blue_rift_heralds_slained,red_rifts_heralds_slained,blue_AIR_DRAGON,red_AIR_DRAGON,blue_EARTH_DRAGON,red_EARTH_DRAGON,blue_FIRE_DRAGON,red_FIRE_DRAGON,blue_HEXTECH_DRAGON,red_HEXTECH_DRAGON,blue_WATER_DRAGON,red_WATER_DRAGON,blue_inhibitors_destroyed,red_inhibitors_destroyed,blue_towers_destroyed,red_towers_destroyed):
    data = {'blue_team_kills':[blue_team_kills],'red_team_kills':[red_team_kills],'blue_team_visionScore':[blue_team_visionScore],
            'red_team_visionScore':[red_team_visionScore],'blue_team_assists':[blue_team_assists],
            'red_team_assists':[red_team_assists],'blue_team_cs':[blue_team_cs],'red_team_cs':[red_team_cs],
            'blue_team_level':[blue_team_level],'red_team_level':[red_team_level],'blue_dragons_slained':[blue_dragons_slained],
            'red_dragons_slained':[red_dragons_slained],'blue_rift_heralds_slained':[blue_rift_heralds_slained],
            'red_rifts_heralds_slained':[red_rifts_heralds_slained],'blue_AIR_DRAGON':[blue_AIR_DRAGON],
            'red_AIR_DRAGON':[red_AIR_DRAGON],'blue_EARTH_DRAGON':[blue_EARTH_DRAGON],'red_EARTH_DRAGON':[red_EARTH_DRAGON],
            'blue_FIRE_DRAGON':[blue_FIRE_DRAGON],'red_FIRE_DRAGON':[red_FIRE_DRAGON],'blue_HEXTECH_DRAGON':[blue_HEXTECH_DRAGON],
            'red_HEXTECH_DRAGON':[red_HEXTECH_DRAGON],'blue_WATER_DRAGON':[blue_WATER_DRAGON],'red_WATER_DRAGON':[red_WATER_DRAGON],
            'blue_inhibitors_destroyed':[blue_inhibitors_destroyed],'red_inhibitors_destroyed':[red_inhibitors_destroyed],
            'blue_towers_destroyed':[blue_towers_destroyed],'red_towers_destroyed':[red_towers_destroyed]}

    probability_model_df = pd.DataFrame(data,columns=['blue_team_kills','red_team_kills','blue_team_visionScore','red_team_visionScore','blue_team_assists','red_team_assists','blue_team_cs','red_team_cs','blue_team_level','red_team_level','blue_dragons_slained','red_dragons_slained','blue_rift_heralds_slained','red_rifts_heralds_slained','blue_AIR_DRAGON','red_AIR_DRAGON','blue_EARTH_DRAGON','red_EARTH_DRAGON','blue_FIRE_DRAGON','red_FIRE_DRAGON','blue_HEXTECH_DRAGON','red_HEXTECH_DRAGON','blue_WATER_DRAGON','red_WATER_DRAGON','blue_inhibitors_destroyed','red_inhibitors_destroyed','blue_towers_destroyed','red_towers_destroyed'])

    team_predictions = loaded_model.predict_proba(probability_model_df)

    if team == 'Blue': 
        return (f'You have a {round(team_predictions[0][0]*100,1)}% chance of winning') 
    elif team == 'Red':
        return (f'You have a {round(team_predictions[0][1]*100,1)}% chance of winning')

run = st.button("Prediction")

if run:
    results = win_proba(team,blue_team_kills,red_team_kills,blue_team_visionScore,red_team_visionScore,blue_team_assists,red_team_assists,blue_team_cs,red_team_cs,blue_team_level,red_team_level,blue_dragons_slained,red_dragons_slained,blue_rift_heralds_slained,red_rifts_heralds_slained,blue_AIR_DRAGON,red_AIR_DRAGON,blue_EARTH_DRAGON,red_EARTH_DRAGON,blue_FIRE_DRAGON,red_FIRE_DRAGON,blue_HEXTECH_DRAGON,red_HEXTECH_DRAGON,blue_WATER_DRAGON,red_WATER_DRAGON,blue_inhibitors_destroyed,red_inhibitors_destroyed,blue_towers_destroyed,red_towers_destroyed)
    st.write(f'{results}')