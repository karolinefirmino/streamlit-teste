import streamlit as st

st.markdown(
    '''
# Bem-vindo/a, Professor(a) 
### (Teste) Sistema de Gestão Informacional da Escola Livre de Música.

Abaixo registre as notas das/dos alunas/alunos avaliadas/os

'''
)
with st.form('Formulário de conta'):
    clarinet_students = ['Angela Pommer',  'Gabriel', 'Ana']
    flute_students = ['Vinicius', 'Matheus']
    c, d = st.columns(2)
    inst = st.selectbox('Instrumento', ('Clarinete', 'Flauta Transversal'))
    options = []
    student = st.selectbox('Aluna/o', options)

    def aluno(inst):
        if inst == 'Clarinete':
            for i in range(len(clarinet_students)):
                options.append(i)
            return options
        else:
            for i in range(len(flute_students)):
                options.append(i)
            return options

    nota_p = st.number_input('Postura:')
    nota_r = st.number_input('Ritmo:')
    nota_s = st.number_input('Sonoridade:')
    nota_i = st.number_input('Interpretação:')
    #notas = [nota_p, nota_r, nota_s, nota_i]
    #nota_t_media = sum(notas) / len(notas)
    soma = nota_p + nota_r + nota_s + nota_i
    media_p = int(soma) / 4

    st.text_input('Comentário/Observação:')
    st.write(f'Média Parcial: {media_p}')

    submitted = st.form_submit_button()
    st.balloons()
