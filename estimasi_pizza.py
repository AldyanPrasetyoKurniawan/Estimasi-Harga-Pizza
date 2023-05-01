import pickle
import streamlit as st

model = pickle.load(open('estimasi_pizza.sav', 'rb'))

st.title('Estimasi Harga Pizza (Rp)')

size = st.number_input('Small, Reguler, Medium, Large, XL, Jumbo (1, 2, 3, 4, 5, 6)')
diameter = st.number_input('Diameter Pizza dalam Inch')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[size, diameter]]
    )
    st.write ('Estimasi harga Pizza : ', predict)