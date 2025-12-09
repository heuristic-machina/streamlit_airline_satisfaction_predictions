
# Airline Satisfaction Predictions using Machine Learning: 

This experiment employs 4 Machine Learning models evaluating model metrics and computing performance for predicting airline satisfaction rates.  Fly over to the interactive app for this project and try for yourself: https://airline-satisfaction-predictions.streamlit.app/


## Introduction:

The Kaggle dataset of shape (103594, 25) tracked satisfaction rates amongst business and personal travelers.  `satisfaction` binary attributes made a great candidate for Random Forest models in particular.  Three other models: Radial Basis Function (RBF) Support Vector Classification (SVC), Linear SVC, and Logistic Regression provided baseline and computationally complex comparisons.  Outliers existed in flight time and delays and were compressed using numpy.log1p() method to help in the model's processing analysis.  One-hot encoding using pandas.get_dummies converted catergorical labels for the `class` feature into numerical formats machine learning models can understand.  Missing values in `arrival_delay_in_minutes` and non-pertinent columns `id` and `unnamed:_0` were dropped in the preprocessing stage.  The cleaned dataset was saved as new csv file after completing exploration of the dataset implementing seaborn visualations.  

The second portion of the experiment split the cleaned dataset into training and test sets for model inputs.  The 4 models were evaluated against a baseline using model metrics: accuracy, recall, and precision and then visualized using a confusion matrix.  Hyperparameter tuning was employed on half of the models: Logistic Regression which showed no remarkable change and Random Forest that benefited by better fitting and classification.



## Technologies

**Client-Server-Architecture:** JupyterLab 4.2.5

**Programming Language:** Python 3.12.1

**Libraries:** Numpy 1.26.4, Matplotlib 3.9.2, Pandas 2.2.2, Seaborn 0.13.2, Scikit-learn 1.5.1

## Visualization Methods

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/heatmap.png)

Heatmap: `satisfaction` 

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/log_feat.png)

Boxplots: Log Transformed Features `dep_delay_log`, `arr_delay_log`, `flight_dist_log`

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/log_r.png)

Confusion Matrix: Logistic Regression Model

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/lin_svc.png)

Confusion Matrix: Linear SVC Model

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/rbf_svc.png)

Confusion Matrix: Radial Basis Function SVC Model

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/rf.png)

Confusion Matrix: Random Forest Classifier Model

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/rf_hyper.png)

Confusion Matrix: Random Forest Classifier Model Hyperparameter Tuning

![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/features.png)

Bar Plot: Most Important Features
![App Screenshot](https://github.com/heuristic-machina/streamlit_airline_satisfaction_predictions/blob/master/imgs/demographics.png)

Heatmap: Median Survey Feature Scores by Demographic


## Conclusion:

🌳 The Random Forest model performed the best because the data contains complex, non-linear patterns that linear models miss (Linear SVC & Logistic Regression), and the algorithm is computationally efficient enough to train effectively on a dataset of this size, which challenges the kernel classifier RBF.

The kernel classifier obtained high scores but was extremely slow and computationally expensive since it compares every data point to every other data point taking space of Big O notation of N squared.

From a business standpoint airlines can help their customers become more satisified by arming them with knowledgeable blogs to get new and young business travelers up to speeds like their loyal veterans. Airline implementation of email marketing for onboard offerings could be beneficial for optimal planning resulting in increased traveler satisfaction.

Now that you have all that reading out of the way go on and check out the interactive app: https://airline-satisfaction-predictions.streamlit.app/ for this project!

## References and Credits

 - Burkov, Andriy, *The Hundred-Page Machine Learning Book*, Coppell, 2019
 - Images from Vecteezy, https://www.vecteezy.com/
 - Image from ChatGPT, https://chatgpt.com/
 - https://www.businessinsider.com/difference-between-amenities-in-business-and-economy-class-2023-8#both-seats-offered-snacks-but-in-business-class-i-could-order-an-unlimited-amount-23
 - https://www.reddit.com/r/BritishAirways/comments/1dr9xa7/corporate_travel_policies_frequent_flying/
 - https://www.getnomad.app/blog/do-planes-have-wifi
 - https://thepointsguy.com/news/business-travel-points-and-miles/
 - https://onemileatatime.com/tall-passengers-more-legroom/
 - https://travelnoire.com/too-tall-to-fly-learn-how-main-us-airlines-deal-with-passengers-that-need-more-leg-room
 - https://www.nerdwallet.com/travel/learn/in-flight-entertainment-the-complete-guide
 - https://www.reddit.com/r/unitedairlines/comments/14qo2u1/economy_plus_on_full_flight/
 - https://www.united.com/en/us/fly/travel/inflight/economy-plus.html
 - https://entertainment.aa.com/en
 - https://www.united.com/en/us/fly/mileageplus/young-adult-discount.html
 - https://simpleflying.com/united-airlines-economy-plus-facts/

