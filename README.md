# ML-Model-deployment-using-Flask
A project that focuses on ML model deployment and data visualization, with python-based web framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Plotly-express](https://plotly.com/python/plotly-express/). 

## Repo Objective
An ML model trained on a large dataset, with a accuracy greater than 90 percent, isn't fully complete until it's deployed for the world to experience. Hence, in this project rather than making a great model, the focus has been shifted to deploying a basic ML model as a user friendly web project using Flask.

Also, I had seen a [post](https://www.linkedin.com/posts/chayankathuria_python-machinelearning-datascience-activity-6715193481385578496-lGth/) showing a beautiful visualization of data in a sunburst chart using plotly. So created one of my own charts and added it in the project as a jewel in the crown! 
<br> Feedback is appreciated!

## Prerequisites
- Install dependencies using [requirements.txt] (/requirements.txt)
<br> ```pip install requirements.txt```
- Imported 2 datasets:
  - [PUBG Finish Placement Prediction Data](https://www.kaggle.com/c/pubg-finish-placement-prediction/data)
  - [Iris Data](https://archive.ics.uci.edu/ml/datasets/iris)

## Features

The website consists of 3 tabs: *Home, Predict, Visualize*
<br> __Home__: Gives a clear description of the website and its working.


![Home page](/images/pagehome.PNG)

<br> __Predict__: With its earier-to-use interface lets end user to input prediction attributes for the pretrained-model to predict, in this case, a [KNN Logistic Regression Model claassifying flower species accurately](/deploy/model.py).   
<br>
![Predict page](/images/pagePredict.PNG)

<br> __Visualization__: Shows data visulizations and an interactive interface.    

![Predict page](/images/pageViz.gif)
