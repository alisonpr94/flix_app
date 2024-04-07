import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

genres = [
    {
        "id": 1,
        "name": "Ação"
    },
    {
        "id": 2,
        "name": "Aventura"
    },
    {
        "id": 3,
        "name": "Cinema de arte"
    }
]

def show_genres():
    st.write('Lista de Gêneros:')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
    )
 
    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')

    if st.button('Cadastrar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')