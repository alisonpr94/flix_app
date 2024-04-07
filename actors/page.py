import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

actors = [
    {
        "id": 1,
        "age": 76,
        "name": "Arnold Schwarzenegger",
        "birthday": "1947-07-30",
        "nationality": "USA"
    },
    {
        "id": 2,
        "age": 47,
        "name": "Wagner Moura",
        "birthday": "1976-06-27",
        "nationality": "BRAZIL"
    },
    {
        "id": 3,
        "age": 48,
        "name": "Angelina Jolie",
        "birthday": "1975-06-04",
        "nationality": "USA"
    }
]

def show_actors():
    st.write('Lista de Atores:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid'
    )
 
    st.title('Cadastrar novo ator/atriz')
    name = st.text_input('Nome do(a) ator/atriz')

    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz {name} cadastrado com sucesso!')