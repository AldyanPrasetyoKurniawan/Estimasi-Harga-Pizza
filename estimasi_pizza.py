import pickle
import streamlit as st

model = pickle.load(open('estimasi_pizza.sav', 'rb'))

st.title('Estimasi Harga Pizza (Rp)')

size = st.number_input('Small, Reguler, Medium, Large, XL, Jumbo (1, 2, 3, 4, 5, 6)')
diameter = st.number_input('Diameter Pizza dalam Inch')
extra_sauce = st.number_input('Tambahan Saus (yes = 1 dan no = 0')
extra_cheesee = st.number_input('Tambahan Keju (yes = 1 dan no = 0')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[size, diameter, extra_sauce, extra_cheesee]]
    )
    st.write ('Estimasi harga Pizza : ', predict)
