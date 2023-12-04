# Breast Cancer Classification using Deep Learning
Objective:<br>
Our objective is to diagnose the possibility of Breast Cancer using Deep Learning method, based on the data collected from the Fine Needle Aspiration Test.<br>

Required Libraries (Main Code):<br>
Imported Libraries,<br>
import tensorflow as tf<br>
import pandas as pd<br>
import numpy as np<br>
import matplotlib.pyplot as plt<br>
import seaborn as sns<br>
import plotly.express as px<br>

from sklearn.datasets import load_breast_cancer<br>
from sklearn.model_selection import train_test_split<br>
from sklearn.preprocessing import StandardScaler<br>

For Installation,
Tensor Flow - pip install tensorflow
plotly - pip install plotly

Required Libraries (Web Application):
import streamlit as st
import time
import tensorflow as tf
import pandas as pd
import matplotlib
matplotlib.use('agg')
#import matplotlib.pyplot as plt
#import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

For Installation,
Streamlit - pip install streamlit

Description:
Data Source: https://goo.gl/U2Uwz2
This data consist of 30 Features and 569 Instances. Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. 

Model Building and Training:
Built an Artificial Neural Network by means of Tensorflow's Keras API to predict the possibility of Breast Cancer.
Train Score - Loss:0.1067, Accuracy:0.9790
Test Score - Loss:0.0992, Accuracy:0.9734

Model Deployment:
Developed a web application using Streamlit.

Dashboard Link:
https://reshma-jp-bcc-dl.streamlit.app/






