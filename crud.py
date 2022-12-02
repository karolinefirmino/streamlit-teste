import streamlit as st


d = {}

with st.form('Formulário de conta'):
    a, b = st.columns(2)
    d['nome'] = a.text_input('Nome do Aluno:')
    d['instrumento'] = b.text_selectbox(
        'Instrumento', ('Flauta Transversal', 'Clarinete'))
    d['nota_postura'] = st.text_input('Seu e-mail:')

    d['comentário'] = st.text_area('Um comentário:')

    st.form_submit_button('Enviar')

if d:
    st.json(d)
