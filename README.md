![image](https://github.com/abtieku/group4-project/blob/main/Resources/Restaurant.jpg)
# Restaurant Ratings Analysis

Our selected topic is restaurants and their star ratings. We want to be able to predict the star rating of the restaurant based on various attributes such as:

- Price
- Noise Level
- Whether it Serves Alcohol or Not
- Restaurant Attire
- Other

## Reason Why We Selected Our Topic

Our reason for this topic is that some restaurants may not have many ratings yet, and we want to be able to help people find the best restaurants.

## Description of the Source of Data

The Dataset came from [Yelp](https://www.yelp.com/dataset). It contains 5 different json data files out of which we are just taking the ```business.json```
- The ```business.json``` file contains business data including location data, attributes, categories and star ratings for the restaurants.

## Questions to be Answered With the Data

- What features make a restaurant successful?
- Can we accurately classify a restaurant by star rating given these features? 
- Can we accurately predict the success of a restaurant given these features?

## Communication Protocols

```Zoom``` and ```Slack``` are the communication platforms used for discussion on the project. Meetings are conducted several times a week to assign project tasks, decide on technologies to be used and solve any challenges encountered during the process.

## Machine Learning Model

We have been entertaining the idea of incorporating a Neural Network to predict the star rating of a restaurant based on features such as food served, noise level, location etc. The second viable option in mind is to create a model predicting the success of a restaurant based on these same features or attributes utilizing a polynomial linear regression. Information for both models as well as a README.md is located in the link provided below.

[Machine Learning Group 4](https://github.com/abtieku/group4-project/tree/main/Machine_Learning)


## Database

Google Cloud and Postgres are being used to house our server.

### Server
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/server.png)

### Tables
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/tables.png)

### Data
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/data.png)

Shema and README.md provided below

[Database Group 4](https://github.com/abtieku/group4-project/tree/main/Database)

## Data Cleaning and Analysis

Python Pandas, sklearn, and tensorflow libraries will be used to clean the data,perform an exploratory analysis, and build our Machine learning models.

## Database Storage

PostgreSQL is where data is stored and is hosted on the Google Cloud Platform. SQL Alchemy is used to connect to the database.

## Requirements.txt
We set up a requirements.txt file in the main folder. This file contains what packages and libraries are needed to successfully run the code.

## Dashboard

Tableau will be used to create interactive dashboards. The interactive elements include being able to select or de-select 10 states in these charts:

- Top locations
- Restaurant categories (American Traditional, Italian, Japanese, etc) 
- Restaurant categories with review ratings
- Attributes contributing to review ratings

[Link to Tableau Visualization](https://public.tableau.com/profile/shanu.joseph#!/vizhome/RestaurantBusinessAnalysis/Story1?publish=yes)

[Tableau Dashboards Group 4](https://github.com/abtieku/group4-project/tree/shanu_segment2/Dashboard/Tableau)


## Google Slides
Google Slides will be used for the presentation..

[Link to Google Slides](https://docs.google.com/presentation/d/1nr6JvIkOD3UAjcMgdsePUiV51nl8bSs3Si4AMYdGYho/edit#slide=id.gc14ac822ce_1_40)