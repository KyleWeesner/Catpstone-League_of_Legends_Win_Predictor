# League of Legends Win Predictor
 
 
**Author: Kyle Weesner**
Note: github/linked/email
 
![img](https://wallpaperaccess.com/full/217097.jpg)


## Overview

This project outlines the process of data collection, using Riots API to train algorithms.  We are doing this to predict the winnability of a game at 15 mins.  This win predicting model and its app is meant to be used as a time efficient rank climbing helper tool to help more serious gamers.  I'm here to pitch this model to Swift Gaming Company, to be used in the Blitz App for gamers.  This model will be used side by side as a win predictor tool.  

## Business Problem

Playing ranked games of League of Legends can take consumable amount of time.  At the fifteen minute mark, you have the option to surrender.  My model will predict whether your team will win or not at the fifteen minute mark.  Being able to know if you're going to win the match or not can save time for the losing team.  The losing team will have the option to surrender instead of playing the remainder of the game.
 
## Data
Data was acquired through [Riots Developer Portal](https://developer.riotgames.com/).  An account with Riot is required along with agreeing with their general policies to have access to their API key.  Functions for data collection are located in `data_gathering_functions.py` and the process for collecting my dataset is located [Web_scraping_for_Final_Dataset](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Web_scraping_for_Final_Dataset.ipynb). 

Features that went into the model were:
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
The predictive models were made with a combination of the data and the tools listed below:
- Pandas for dataframe manipulation and data analysis.  
- Sklearn for statistical modeling and machine learning.
- Streamlit for app building.  

## Navigation

Follow these notebooks in order for the workflow.

1. [Webscraping/ Data Collection](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Web_scraping_for_Final_Dataset.ipynb)

2. [Model Building](https://github.com/KyleWeesner/Catpstone-exploration/blob/main/Untitled_Folder/Modeling.ipynb)



## Results

There were many types of algorithms that were used for modeling.  All of the models had relatively the same cross-val scores.  Deciding on the final model for the app was based on how fast the model was able to predict on the data.  Because League of Legends is a constantly updating their gameplay, some of my models will need to be re-trained depending on the season/ update. This data was collected during Season 12.

If you look below at my plot, it appears that there may be a cap for how well my models can predict.  Most of my models were around the same accuracy, so more features may be needed for improving my model performance.

![img](./images/model_improvement.jpg)

All of my models had the same accuracy.  The second most important factor was the speed of my models.  Having a faster computational speed determined my model for my app.  That model was LogisticRegression. 

![img](./images/models_prediction_speed.jpg)

&nbsp;


The final model's accuracy score on the test set was 0.77.  The data was split about 50/50 on the winning percentage between the blue team and the red team.  This was great because playing on the left side or the right side had no bias to influence the chance of winning the game.  

![img](./images/confusion_matrix.png)


## App Deployment

Due to legal agreements this app will not be publically available on a website until the product gets registered and approved by Riot Games.


## Conclusion
My model can be a useful application in the Blitz App for League of Legend gamers who are wanting to play a ranked match while being efficient with their time.  The final model used was a LogististicRegression Algorithm with a 77% accuracy on unseen data.


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

- Develop functions for the app to gather live game data so the user will not need to input every feature.

- Develop a prediction tool that updates the winning percentage as the game progresses.




Citation:
https://wallpaperaccess.com/full/217097.jpg

League of Legends Win Predictor isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.