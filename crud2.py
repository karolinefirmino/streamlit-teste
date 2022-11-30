import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = {1: 'Angela Pommer', 2: 'Gabriel', 3: 'Ana'}
    flute_students = {1: 'Vinicius', 2: 'Matheus'}
    a, b = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))

    def format_func(option):
        if inst == 'Clarinete':
            return clarinet_students[option]
            option = st.selectbox("Select option", options=list(
                clarinet_students.keys()), format_func=format_func)
            #display = (clarinet_students.values())
            #options = list(range(len(display)))
            #value = st.selectbox("aluna/o", options, format_func=format_func)
            # return value
        else:
            return flute_students[option]
            option = st.selectbox("Select option", options=list(
                flute_students.keys()), format_func=format_func)
            #display = (flute_students.values())
            #options = list(range(len(display)))
            # value = st.selectbox(
            # "aluna/o", option, format_func=format_func)
            # return value
        st.write(f"You selected option {option} called {format_func(option)}")
        print(type(option))
    # format_func(option)

    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
