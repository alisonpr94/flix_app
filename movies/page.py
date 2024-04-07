import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

movies = [
    {
        "id": 1,
        "name": "Vingadores"
    },
    {
        "id": 2,
        "name": "Invocação do Mal"
    },
    {
        "id": 3,
        "name": "The Batman"
    }
]


def show_movies():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )
 
    st.title('Cadastrar novo filme')
    name = st.text_input('Nome do filme')

    if st.button('Cadastrar'):
        st.success(f'Filme {name} cadastrado com sucesso!')