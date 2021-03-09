# Final Dashboard
# [Group 4 Dashboard](https://groupfour.ngrok.io)



![image](https://github.com/abtieku/group4-project/blob/main/Resources/Restaurant.jpg)
# Restaurant Business Analysis

## Purpose of the Project 

- Find the most popular restaurants across different states in US with regards to the review ratings provided by customers.
- Use different machine learning models to predict the star rating and success of a restaurant based on restaurant attributes such as food served, noise level, delivery, takeout, price range etc. 
- Train and evaluate different machine learning models to predict the model with the highest accuracy score.

## Reason Why We Selected Our Topic

With this project, we want to be able to help people search the best restaurants in a particular category in a particular city.

## Description of the Source of Data

The Dataset came from [Yelp](https://www.yelp.com/dataset). It contains 5 different json data files out of which we are just taking the ```business.json```

- The ```business.json``` file contains business data including location data, attributes, categories and star ratings for the restaurants.

## Questions to be Answered With the Data

- What Features makes a Restaurant successful
- Can we accurately predict the success of a restaurant given these features
- What is the percentage for positive and negative reviews per state per category?
- What are the top 5 restaurants in a state?
- Can we accurately classify a restaurant by star rating given these features

## Communication Protocols

```Zoom``` and ```Slack``` are the communication platforms used for discussion on the project. Meetings are conducted several times a week to assign project tasks, decide on technologies to be used and solve any challenges encountered during the process.

## Machine Learning Model

We have been entertaining the idea of incorporating a Neural Network to predict the star rating of a restaurant based on features such as food served, noise level, location etc. The second viable option in mind is to create a model predicting the success of a restaurant based on these same features or attributes utilizing a Logistic regression. Information for Both Models as well as a README.md is located in the link provided below

[Machine Learning Group 4](https://github.com/abtieku/group4-project/tree/main/Machine_Learning)


## Database

Google Cloud and Postgres is being used to host our server

### server
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/server.png)

### tables
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/tables.png)

### data
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/data.png)

Schema and README.md provided below

[Database Group 4](https://github.com/abtieku/group4-project/tree/main/Database)

## Data Cleaning and Analysis

Python Pandas,sklearn, and tensorflow libraries will be used to clean the data,perform an exploratory analysis, and build our Machine learning models.

## Database Storage

PostgreSQL is where data is stored and is hosted on the Google Cloud Platform.

## Requirements.txt
We set up a requirements.txt file in the root folder. This file contains what packages and libraries are needed to successfully run the code.

## Dashboard

Tableau will be used to create interactive dashboards.

[Link to Tableau Visualization](https://public.tableau.com/profile/shanu.joseph#!/vizhome/RestaurantBusinessAnalysis/Story1?publish=yes)

[Tableau Dashboards Group 4](https://github.com/abtieku/group4-project/tree/shanu_segment2/Dashboard/Tableau)
 

## Google Slides
Google Slides will be used for the presentation..

[Link to Google Slides](https://docs.google.com/presentation/d/1nr6JvIkOD3UAjcMgdsePUiV51nl8bSs3Si4AMYdGYho/edit#slide=id.gc14ac822ce_1_40)
