import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = {1: 'Angela Pommer', 2: 'Gabriel', 3: 'Ana'}
    flute_students = {1: 'Vinicius', 2: 'Matheus'}
    a, b = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))
    option = ""

    def format_func(option):

        if inst == 'Clarinete':
            return clarinet_students[option]
            option = st.selectbox("Select option", options=list(
                clarinet_students.values()), format_func=lambda x: "option " + str(x))
        else:
            return flute_students[option]
            option = st.selectbox("Select option", options=list(
                flute_students.values()), format_func=lambda x: "option " + str(x))

    st.write(f"You selected option {option} called {format_func(option)}")
    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
