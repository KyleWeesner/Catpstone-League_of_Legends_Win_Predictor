# League of Legends Win Predictor
 
 
**Author: Kyle Weesner**
 
![img](https://wallpaperaccess.com/full/217097.jpg)

## Overview

This project outlines the process of data collection using riots api for data to train algorithms to predict winnability of a game at 15 mins.  This project is a starting model and application to run alongside with a game as a helper tool for more time efficient rank grinding for serious gamers.  I am here to pitch this model to Swift gaming company to be used in the Blitz app for gamers use that will eventually run side by side as a win predictor tool.  

## Business Problem

Ranked games in League of Legends is 
When playing League of Legends games take a consumable amount of time to play, so being able to know if moving on to the next game and surrendering sometimes can be a wise choice.  By being able to predict winnability at certain moments of the game one can attempt to save time by moving on to the next game or will know if its worth staying in the game to continuing to attempt to win.
 
## Data
Data was acquired through [riots developer portal](https://developer.riotgames.com/).  An account with riot is required along with agreeing with their general policies, terms, and agreements to have access to an api key.  Functions for data collection are located in `data_gathering_functions.py` and the process for collecting my dataset is located at `Web_scraping_for_Final_Dataset.ipynb`. 

 
## Tools
The predictive models were made with a combination between the data and tools used in this project. 
- Pandas for datafram manipulation and data analysis.  
- Sklearn for statistical modeling and machine learning.
- Streamlit for app building  

## Navigation

Follow through these notebooks in order to follow workflow.  They can be found in the workspace folder in this repository.

1. [Webscraping/ Data Collection]()

2. [Model Building]()

3. [Feature Importance Analysis]()



## Results
Model Proformance Metrics

The final model had decent proformance metrics.  Final model's accuracy on the test set is 0.95. Final model's precision on the test set is 0.81. Final model's recall on the test set is 0.8. Final model's f1-score on the test is 0.81.  

![img](./images/confusion_matrix.png)


Model Improvements

The predictive models took in 15 features that contributes accuracy scores.  As we can see the model was slightly being improved throughout the iterative process.  Our final model was our best model which was GradientBoostingClassifier after being tuned.   

![img](./images/model_improvement.jpg)

## App Deployment

Due to legal agreements this app will not be publically avaiable.


## Conclusions

Model Recommendation
- Syriatel can use this model to predict which clients may churn in advance so we can provide intermediation strategies/ allocating resources to hopefully reduce the number of churning.

Business Recommendation
- I would focus on improving customer service with priotizing keeping customer service calls under 4.

- Implement new payment plans per amount of data usage that are better cost efficient for the customer or have monthly plans. 

- The current international plan needs to be evaluated and changed due to a large proportion having it end up churning.

 
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

- Improving model predictive ability.  I would like to reduce my false positives and false negatives.

- Look into how well the model works with other time period datasets that you may have.  

- Explore analysis on other features outside of these 3 provided.
