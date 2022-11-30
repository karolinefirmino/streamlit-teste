import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = ['Angela Pommer', 'Gabriel', 'Ana']
    flute_students = ['Vinicius', 'Matheus']

    def student():
        if inst.get() == "Clarinete":
            stu.config(value=clarinet_students)
        else:
            stu.config(value=flute_students)
    a, b = st.columns(2)
    stu = st.text_input(student())
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))
    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
