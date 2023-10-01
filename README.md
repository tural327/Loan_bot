# Loan_bot
The Weight of Evidence (WoE) and the Information Value (IV) are two of the most widely used tools in Finance and credit risk analysis. Not only these tools are extremely relevant for the measurement of predictive power in  
I
n
d
e
p
e
n
d
e
n
t
   
V
a
r
i
a
b
l
e
s
 , but also extremely effective in handling outliers, missing values, and categorical data transformation.

In this notebook, we will explore the practical applications of both WoE and IV by utilizing the Loan-Approval-Prediction-Dataset. Our aim is to demonstrate how these techniques can be used to enhance the predictive accuracy in many binary classification tasks, such as loan approval prediction.

 # Visualization
 Before training I made quich explore and made simple visualization

 ![](https://github.com/tural327/Loan_bot/blob/main/1.png)
  ![](https://github.com/tural327/Loan_bot/blob/main/2.png)
   ![](https://github.com/tural327/Loan_bot/blob/main/3.png)
    ![](https://github.com/tural327/Loan_bot/blob/main/4.png)
 # Training
 I just build simple tf model and result was  :
```python
 Classification Report: 
               precision    recall  f1-score   support

         0.0       0.96      0.92      0.94       532
         1.0       0.93      0.96      0.94       531

    accuracy                           0.94      1063
   macro avg       0.94      0.94      0.94      1063
weighted avg       0.94      0.94      0.94      1063

 ```

I decided use supervised learning with hyperparameter tuning and result was better than tf model 
```python
model	best_score	best_params
0	svm	0.942583	{'C': 10, 'kernel': 'rbf'}
1	random_forest	0.979293	{'n_estimators': 10}
2	logistic_regression	0.929783	{'C': 10}
 ```
Random forest model was much more better so i will use this model
