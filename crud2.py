import streamlit as st


with st.form('Formulário de conta'):
    st.text_input('Nome do Aluno:')
    st.text_selectbox(
        'Instrumento', ('Flauta Transversal', 'Clarinete'))
    st.number_input('Postura:')
    st.number_input('Ritmo:')
    st.number_input('Sonoridade:')
    st.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button("Submit")
