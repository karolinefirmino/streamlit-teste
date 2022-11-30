import streamlit as st


def inputs():
    d = {}

    with st.form(key="include_note"):
        instruments_list = ['Clarinete', 'Flauta Transversal', 'Oboé']
        input_instrument = st.text_selectbox(
            "Instrumento", instruments_list)
        if input_instrument == 'Clarinete':
            list_clarinet_students = ['Angela Pommer', 'Fernando Grande', 'Ana Carolina',
                                      'Ellen', 'Karoline Rodrigues Firmino', 'Ana Luísa Dias', 'Gabriel Abner', 'Paloma']
        elif input_instrument == 'Flauta Tranversal':
            list_flute_students = ['Adão', 'Carlos',
                                   'Matheus', 'Paloma', 'Vinicius']
        else:
            list_ob_students = ['Lucas', 'Luís', 'Victória']
        pieces_for_evalutation = st.text_input(
            'Peças executadas pelas/pelos estudantes')
        nota_postura = st.number_input('Postura')
        nota_ritmo = st.number_input('Ritmo')
        nota_sonoridade = st.number_input('Sonoridade')
        nota_interpretacao = st.number_input('Interpretação')
        soma = nota_postura + nota_ritmo + nota_sonoridade + nota_interpretacao
        media = soma / range(soma)
        salvar = st.form_submit_button('Salvar Avaliação')

    if d:
        st.json(d)
