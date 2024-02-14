In this project, I trained a GRU Neural network to predict the traffic on four junctions. I used a Normalization and Differencing transform to achieve a stationary Time Series. As the Junctions vary in Trends and Seasonality, I took different approach for each junction to make it stationary. I applied the Root Mean Squared error as the evaluation metric for the model. In addition to that I plotted the Predictions alongside the original test values.

The Number of vehicles in Junction 1 is rising more rapidly compared to Junction 2 and 3. Due to the limitation in data of Junction 4 fails to come up with a conclusion on the same.

The Junction 1’s traffic has a stronger weekly seasonality as well as hourly seasonality. Whereas other junctions are significantly linear.

Comparing with ARIMA and Prophet model, GRU model gives a better output performance and results.

Dashboard Link: https://traffic-forecasting-jpreshma.streamlit.app/


