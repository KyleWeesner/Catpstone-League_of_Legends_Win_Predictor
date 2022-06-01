# League of Legends Win Predictor
 
 
**Author: Kyle Weesner**
 
![img](https://wallpaperaccess.com/full/217097.jpg)

## Overview

This project outlines the process of data collection using riots api to train algorithms to predict winnability of a game at 15 mins.  This win predicting model and its application is meant to be used alongside with games as a helper tool for more time efficient rank grinding for serious gamers.  I am here to pitch this model to Swift gaming company to be used in the Blitz app for gamers use that will be ran side by side as a win predictor tool.  

## Business Problem

Playing ranked games of League of Legends take a consumable amount of time to play, so being able to know if moving on to the next game and surrendering sometimes can be a wise choice.  By being able to predict winnability at certain moments of the game one can attempt to save time by moving on to the next game or will know if its worth staying in the game continuing to attempt to win.
 
## Data
Data was acquired through [riots developer portal](https://developer.riotgames.com/).  An account with riot is required along with agreeing with their general policies, terms, and agreements to have access to an api key.  Functions for data collection are located in `data_gathering_functions.py` and the process for collecting my dataset is located at [Web_scraping_for_Final_Dataset.ipynb](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Web_scraping_for_Final_Dataset.ipynb). 

Features that went into the model that were gathered for both blue and red team per game:
- Kills
- VisionScore 
- Assists
- CS 
- Levels
- Number Dragons Slained
- Types of Dragons Slained
- Number of Rift Heralds Slained
- Number of Turrets Destroyed
- Number of Inhibitors Destroyed

 
## Tools
The predictive models were made with a combination between the data and tools used in this project. 
- Pandas for datafram manipulation and data analysis.  
- Sklearn for statistical modeling and machine learning.
- Streamlit for app building  

## Navigation

Follow through these notebooks in order to follow workflow.  They can be found in the workspace folder in this repository.

1. [Webscraping/ Data Collection](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Web_scraping_for_Final_Dataset.ipynb)

2. [Model Building](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Modeling.ipynb)



## Results

Many different types of algorithms were used for modeling.  All of the models here had relatively the same cross val scores so deciding on the final model for the app was based on how fast the model is is able to predict on data.  Because League of Legends is a constantly changing game models will need to be re-trained depending on the season/ patch.  In this project LogisticRegression had the fastest training speed. This data was collect for games in Season 12.  It appears that there may be a "ceiling" for how well our models can predict.  Most models were around the same accuracy, so more features may be needed for improving model performance.

![img](./images/model_improvement.jpg)

Looking at the models developed prediction speed on the training data LogisticRegression is the fastest prediction model.  It is important to have more computationally faster models, so with this information the final model decided on is LogisticRegression.  The model is well fitted with the training data, performs well on unseen data, and is the fastest at predicting. 

![img](./images/models_prediction_speed.jpg)

&nbsp;


The final model's accuracy on the test set is 0.77.  The data is split about 50/50 between blue team and red team wining.  This is good because playing on left side or right side does not influence the game in higher ranks.

![img](./images/confusion_matrix.png)




## App Deployment

Due to legal agreements this app will not be publically avaiable on a website until product get registered and approved by riot.


## Conclusions
My model can be a useful application in the blitz app for league of legend gamers who are wanting to play rank being time efficient.  The final model was a LogististicRegression algorithm with a 77% accuracy on unseen data.


 # Note:Clean up Repo and make structure
## Repository Structure
```
├── data
├── images
├── workspace
│       ├── Data Cleaning and Exploratory Data Analysis.ipynb
│       ├── Feature Importance Analysis.ipynb
│       └── Model Building.ipynb
├── .gitignore
├── README.md
└── presentation.pdf
```
 
### Next Steps

- Get more features for dataframe

- Look into predicting games in every rank

- Develope functions for the app to gather live game data so the user will not need to input every feature.

- Develope a prediction tool that will run alongside during any point in a game that will have a constantly changing win rate.




Citation:
https://wallpaperaccess.com/full/217097.jpg

League of Legends Win Predictor isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.