import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    if actors:
        st.write('Lista de Atores:')
        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    
    st.title('Cadastrar novo ator/atriz')
    name = st.text_input('Nome do(a) ator/atriz')
    bday = st.date_input(
        'Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        'Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actor = actors_service.create_actor(
            name=name,
            bday=bday,
            nationality=nationality
        )

        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos.')