import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = ['Angela Pommer', 'Gabriel', 'Ana']
    flute_students = ['Vinicius', 'Matheus']
    a, b = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))
    CHOICES = {1: clarinet_students, 2: flute_students}

    def format_func(option):
        return CHOICES[option]
    option = st.selectbox("Select option", options=list(
        CHOICES.keys()), format_func=format_func)
    st.write(f"You selected option {option} called {format_func(option)}")
    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
