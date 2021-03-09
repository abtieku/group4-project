# Machine Learning
 
## Data Preprocessing
- Downloaded data set from yelp
 
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/raw_json.png?raw=True)
 
- utilized pandas for ETL process
 
- reduced dataset to only hold businesses marked as Restaurants
 
- Using Pandas, Postgres, and Google Cloud we created two DataFrames, business dataframe and attributes data frame
as well as two corresponding tables in Postgres named business_table and attributes_table
 
### Business Dataframe
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/business_df.png?raw=True)
 
### Attributes Dataframe
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/attributes_df.png?raw=True)
 
- Inspected Data types, value counts, and null values
 
- Business data frame was created from the processed data excluding the two columns attributes and categories
 
## Feature engineering
- Attributes data frame was created using the unique business_id column and new boolean columns populated by a python function which retrieved data from the business dataframe's attributes and categories columns for the corresponding business id
 
- Dropped duplicated and NaN values from both dataframes
 
- Dropped Restaurants that had less than 50 reviews
 
- Dropped Restaurants that were not relevant to our analysis:
  
   - Restaurants in Hotels
   - Delis
   - Venues & Event Spaces
   - etc
 
- Dropped Restaurants that were not located in the US
 
- imported data frames from Pandas to the postgresql server hosted on the google cloud.

## Description of how the data was split into training and testing


- 
-  
# Machine Learning Models
## Model Choice including limitations and benefits
- Neural network is an alternative to all the models as it can handle non linear relationships and can handle messy data
- Accuracy score was lower for neural compared to the two other models we used.
## Logistic Regression regression
 
 Logistic regression classifier is used to predict whether a restaurant is successful or not
- A new temporary column was added to hold data regarding whether the restaurant is successful or not
- Label encoder was used to convert is_succesful column to numbers

 
## Neural network classifier
 
A new table was created in postgres using an inner join between our two tables business_table and attributes_table on the business_id column
 
The data was imported into a jupyter notebook as a dataframe, the data frame was then split into two variables: our X or features variable and our y or target variable.
utilizing the python modules tensorflow and sklearn we split the data into training and testing sets.
 
The data was then scaled using the StandardScaler imported from the sklearn library
 
A Sequential model was instanted from the tensorflow library
and built with four layers. the first 3 using the `relu` activation and the last one with the `soft max` activation.
 
This model was chosen for its ability to classify a target column and improve predictions as more data is presented.
 
## Model Summary
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/model_summary.png?raw=True)
 
## Fitting Model
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/100_epochs.png?raw=True)
 
## Accuracy Plot
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/model_accuracy.png?raw=True)
 
## Loss Plot
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/model_loss.png?raw=True)
 
## Predictions
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/model_predictions.png?raw=True)
 
## Classification Report
![alt-text](https://github.com/abtieku/group4-project/blob/main/Resources/model_classification_report.png?raw=True)
 
Our classification report shows an unfortunately low accuracy to predict the correct star rating for Restaurants. We will attempt to create a logistic model and oversampling to predict the success of the restaurant.
 
 
 

