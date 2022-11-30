import streamlit as st


with st.form('Formulário de conta'):
    clarinet_students = ['Angela Pommer', 'Gabriel', 'Ana']
    flute_students = ['Vinicius', 'Matheus']
    student = ""

    def student():
        if inst.get() == "Clarinete":
            student.config(value=clarinet_students)
        else:
            student.config(value=flute_students)
    stu = st.text_input(student)
    a, b = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))
    a.number_input('Postura:')
    b.number_input('Ritmo:')
    a.number_input('Sonoridade:')
    b.number_input('Interpretação:')

    st.text_area('Um comentário:')

    submitted = st.form_submit_button()
