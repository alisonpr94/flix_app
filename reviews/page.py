import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

reviews = [
    {
        "id": 1,
        "star": 5
    },
    {
        "id": 2,
        "star": 3
    },
    {
        "id": 3,
        "star": 5
    }
]


def show_reviews():
    st.write('Lista de Avaliações:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )
