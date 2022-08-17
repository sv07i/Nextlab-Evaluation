import streamlit as st
import pandas as pd
import numpy as np

import pickle




Country = ["FRA", "PRT", "DEU", "GBR", "ESP","USA","ITA","BEL","BRA","NLD","CHE","IRL","Other"]


dist = ["Travel Agent/Operator", "Direct", "Corporate", "Electronic Distribution"]

market = ["Other","Travel Agent/Operator","Direct","Groups", "Corporat", "Complementary", "Aviation"]





pipe = pickle.load(open('nop.pkl','rb'))
st.title('Hotel Check In ')




selectedcity = st.selectbox('Select Country',sorted(Country))

DistributionChannel = st.selectbox(' Distribution Channel',sorted(dist))

MarketChannel = st.selectbox('Select Market Segment',sorted(market))

Age = st.number_input('Age')

AverageLeadTime = st.number_input('Lead Time')

Revenue = st.number_input('Revenue of the Hotel')







if st.button('Generate Prediction'):
    #query = np.array([])

    data = np.array(["AverageLeadTime","DistributionChannel","MarketChannel","selectedcity","Revenue","Age"], dtype=object).reshape(1, 6)
    prediction = pipe.predict(data)
    #query = query.reshape(1,6)


    #prediction = pipe.predict(query).argmax()
    #st.title("Prediction is ".format([prediction]))

    #st.title("Prediction is " + str(int(np.exp(pipe.predict(test_input)))))
    st.title("Prediction is " + format(prediction[0]))

    st.text("1 Means Yes and 0 Means No")





