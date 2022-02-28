# HW9 -- Milestone project

## Introduction
- the goal of this project is to combine everything we learned so far into a masterpiece.
- You need to build an app that contains these features
  - a flask application
  - at least one endpoint that calls the `predict` method of a trained sklearn model
    - you can use any dataset you want for training, but please limit the trained model pickle file to be <=5MB
  - [optional] a database/datafile that you can retrieve data from during the app
  - [optional] a model training pipeline file
  - [optional] unit tests
  - [optional] file linting
  - [optional] a makefile that simplifies any logic that you think it's helpful
  - [optional] a ready-to-build dockerfile that defines entry-point to be the launching of your flask app

## Submission
- please mimic the folder structure of Homeworks/HW9/Frank_Xia, where
  - `real_app` contains your main logic code for 
    - flask app
    - model definition
    - model training
    - ...
  - `tests` contains your testing functions
  - `data` contains any training/serving data you need **and trained model**
    - please don't upload anything that's bigger than 5mb. 
  - optional makefile
  - optional dockerfile