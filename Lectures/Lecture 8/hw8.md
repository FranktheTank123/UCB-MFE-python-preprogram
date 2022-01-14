# HW 8
Please do the following in a jupyter notebook:
- Build a model with a lower average cross-validated RMSE than the best model that we saw in class (-0.008575141851714435) for prediction hourly returns for SOL
    - use 20% of the data set for validation in you cross-validation
    - make sure you're using a time-series dependent cross-validation method
    - you may use any transformation and model you would like
    - you will likely need to feature engineer to beat the class model

Tips:
- model training can sometimes be expensive, depending on the model - use the learning curve to help you understand how long it would take a model to train
- you will likely get the most yield by feature engineering
- hyperparameter tuning is a higher order optimization, it is useful to get the best result of your chosen model, however if your model is not performant it will rarely make it magically performant
