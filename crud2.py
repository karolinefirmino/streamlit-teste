import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = ['Angela Pommer', 'Gabriel', 'Ana']
    flute_students = ['Vinicius', 'Matheus']
    a, b = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))

    def student():
        if inst == 'Clarinete':
            student = st.text_input(clarinet_students.__getitem__)
        else:
            student = st.text_input(flute_students.__str__)
    student()
    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
