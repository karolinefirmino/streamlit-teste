import streamlit as st


d = {}

with st.form('Formulário de conta'):
    st.columns(2)
    d['nome'] = st.text_input('Nome do Aluno:')
    d['instrumento'] = st.text_selectbox(
        'Instrumento', ('Flauta Transversal', 'Clarinete'))
    d['nota_postura'] = st.number_input('Postura:')
    d['nota_ritmo'] = st.number_input('Ritmo:')
    d['nota_sonoridade'] = st.number_input('Sonoridade:')
    d['nota_interpretacao'] = st.number_input('Interpretação:')

    d['comentário'] = st.text_area('Um comentário:')

    st.form_submit_button('Enviar')

if d:
    st.json(d)
