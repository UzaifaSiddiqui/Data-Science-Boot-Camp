# Data-Science-bootCamp


#ABOUT GRAND PROJECT


NOTE : It is better to run this file on COLAB as it already contain all the libraries used and no download have to be made in PC .


This Directory Contain 5 files.

1- Two DATASET files (credit_loan and Main)

2- EDA File have all the preprocessing , EDA , feature engineering and Model fitting (RandomForrestClassifier and DecisionTreeClassifier) which were tested on the Credit_loan DATASET.

3- Model File have the best performing Model and it was Fitted on Main.csv DATASET (which is typically same credit_loan dataset but is preprocessed).

4- Futher Model.pynb aslo generates a pickle for fitted model and then it gets passed to Gradio.

5- Gradio is a python library for deployment of ML models .

6- When the last cell is run on Model.pynb it prints two things FIRST A LINK and SECOND the UI of MODEL .

7- Model can be accessed there as it is 

  8- But a better OPTION is to click on the link which will open a live hosting of that FITTED MODEL.
  
  
  This is a 1 set of value to make prediction on the model and AFTER entering these values model should return 'You Are Not Eligible For Loan' 
  [[24.0,
    82000.0,
    1.0,
    7500.0,
    8.32,
    0.09,
    3.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0]]
