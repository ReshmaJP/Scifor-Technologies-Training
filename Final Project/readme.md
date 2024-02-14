In this project, I trained a GRU Neural network to predict the traffic on four junctions. I used 
Normalization and Differencing transform to achieve a stationary Time Series. As the Junctions 
vary in Trends and Seasonality, I took different approach for each junction to make it stationary. 
I applied the Root Mean Squared error as the evaluation metric for the model. In addition to that 
I plotted the Predictions alongside the original test values.

The Number of vehicles in Junction 1 is rising more rapidly compared to Junction 2 and 3. Due 
to the limitation in data of Junction 4 fails to come up with a conclusion on the same.

The Junction 1’s traffic has a stronger weekly seasonality as well as hourly seasonality. Whereas,
other junctions are significantly linear.

Comparing with ARIMA and Prophet model, GRU model gives better output performance and
results.

In conclusion, the development and implementation of the Gated Recurrent Unit (GRU) model 
for traffic forecasting, coupled with the Streamlit-based application, represent a significant stride 
towards enhancing urban mobility and transportation management. Through a comprehensive 
analysis of historical traffic data from four junctions, our model has demonstrated its efficacy in 
capturing temporal patterns, trends, and seasonality inherent in traffic flow.

Dashboard Link: https://traffic-forecasting-jpreshma.streamlit.app/


