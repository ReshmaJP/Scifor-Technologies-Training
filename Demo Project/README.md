# Breast Cancer Classification using Deep Learning
**Objective:**<br>
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

For Installation,<br>
Tensor Flow - pip install tensorflow<br>
plotly - pip install plotly<br>

Required Libraries (Web Application):<br>
import streamlit as st<br>
import time<br>
import tensorflow as tf<br>
import pandas as pd<br>
import matplotlib<br>
matplotlib.use('agg')<br>
#import matplotlib.pyplot as plt<br>
#import numpy as np<br>

from sklearn.datasets import load_breast_cancer<br>
from sklearn.model_selection import train_test_split<br>
from sklearn.preprocessing import StandardScaler<br>

For Installation,<br>
Streamlit - pip install streamlit<br>

Description:<br>
Data Source: https://goo.gl/U2Uwz2<br>
This data consist of 30 Features and 569 Instances. Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.<br> 
They describe characteristics of the cell nuclei present in the image.<br>

Model Building and Training:<br>
Built an Artificial Neural Network by means of Tensorflow's Keras API to predict the possibility of Breast Cancer.<br>
Train Score - Loss:0.1067, Accuracy:0.9790<br>
Test Score - Loss:0.0992, Accuracy:0.9734<br>

Model Deployment:<br>
Developed a web application using Streamlit.<br>

Dashboard Link:<br>
https://reshma-jp-bcc-dl.streamlit.app/






