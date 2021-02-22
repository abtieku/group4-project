# Restaurant Business Analysis

The purpose of this project is to find the most popular restaurants across cities with regards to the review ratings provided by customers and also use different machine learning models to predict accuracy of customer review ratings.

## Data Source

[Link](https://www.yelp.com/dataset)

## Communication Protocols

```Zoom``` and ```Slack``` are the communication platforms used for discussion on the project. Weekly meetings are conducted to assign project tasks, decide on technologies to be used and solve any challenges encountered during the process.

## Technologies Used

## Data Cleaning and Analysis

Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using PySpark.

## Database Storage

PostgreSQL is where data is stored and is hosted on th Google Cloud Platform.

## Machine Learning

Python Libraries, PySpark and Google Colab will be used for NLP machine learning

## Dashboard

Tableau is used to create interactive dashboards.

## Reason why we selected our topic

With this project we can help people search the best restaurants in a particular category in a particular city.

## Description of the source of data.

The Datset contains 5 different json data files out of which we are just taking ```business.json``` and ```review.json``` files for our analysis. Rest of the data is out of scope for our analysis.

- The ```business.json``` file contains business data including location data, attributes, categories and star ratings for the restaurants.
- The ```review.json``` file contains review data including the user_id who wrote the reviews, the business_id  for which the review is written and the star reviews for each of the restaurant.

## Questions to be answered with the data

- Average review per city per category
- What is the percentage for positive and negative reviews per city per category
- Top 5 restaurants in a City.
- Train and evaluate various machine learning models to predict the machine learning model with the highest accuracy


