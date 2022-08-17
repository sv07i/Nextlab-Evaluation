# Nextlab-Evaluation

Question : Train a machine learning model that predicts the customer who is going to be checked in. 

I train the model for the machine learning and Deep learning approach.

1) Deep learning -

we have about 83000 row data sets with 30 features in it.

First all this is very Missy data and with the spares arrey which is zero values.

Calculate the spares arrey is very computational expensive so Decided to drop the features who has spares arrey.

Booking check in feature have very up down values so I decided to create function called as checke in which is basically customer check in and not check in values .

This feature completely based on booking check in feature.

Second feature is there are 188 country values so I created function that take only top 10 country in new features who has highest Number of check in.

This new country feature is base on Nationality and booking cancelled feature.

Right now, I have 7 to 8 feature to train model. And after the one hot encoding on country, distribution channels and market segment I have about 23 columns in training phase.

I use Artificial Neural network to train datasets with 23 input dimensions and 1 hidden layer with 8 nodes 

I use "relu" activation function for first two layer and in output layer I use "sigmoid " because I want binary classification .

Age has 3000 null value so I fill it with the median value of the age because it handled outliers using simple imputer class from sklearn.

After creating a ANN model I use early stopping concept to avoid overfitting on prediction.

And compile the model and fit the input data .

I get about 97 % Val_accuracy. With ANN.

And import with the name of  model.h5 .



2) Machine learning -

In this approach I use pipeline with the same 7 feature .

In pipeline I add simple imputer , standard scale, logistics regression with the help of column transformer.

Store the column transformer values in pipe function and make to fit train the data sets.

And Lastly check cross Val score and I get about 77% .

And import pipe with the name of nop.pkl.


(.) Backpropagation -

This is algo. for the adjust the weight for particular layer with the back track.

Backpropagation uses a methodology called chain rule to improve outputs. Basically, after each forward pass through a network, the algorithm performs a backward pass to adjust the model’s weights with the gradient desent algo.

formula : Wnew = Wold - n*dl/dWold

(.) App-

With the help of streamlit I built app which is take a function from the user and predict the check in prediction.

wensite link : https://hotel-customer-check-in.herokuapp.com/

