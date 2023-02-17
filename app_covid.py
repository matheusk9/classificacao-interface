import streamlit as st
import pickle
import pandas as pd


# Carrega o modelo treinado
with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

def prever_morte(sexo, pneumonia, age, diabetes, copd, asma, hipertensao, outra, cardio, obeso, renal, fuma, classific):
    entrada = pd.DataFrame({'SEX': [sexo],'PNEUMONIA': [pneumonia],'AGE': [age], 'DIABETES': [diabetes], 'COPD': [copd], 'ASTHMA': [asma], 'HIPERTENSION': [hipertensao], 'OTHER_DISEASE': [outra], 'CARDIOVASCULAR': [cardio], 'OBESITY': [obeso], 'RENAL_CHRONIC': [renal], 'TOBACCO': [fuma], 'CLASIFFICATION_FINAL': [classific]})
    morte = model.predict(entrada)[0]
    return morte

# Elementos visuais do site
st.set_page_config(
    page_title="Detecção COVID-19",
    layout="wide",
)
# Titulo
titulo = "Predição de risco de morte por COVID diante informações"
st.markdown(f"""<h1 style='text-align: center;'>{titulo}</h1>""", unsafe_allow_html=True)

st.warning("Preencha os dados corretamente")

colunas = st.columns(3)

dict_options = {
    'sex':{'Masculino':2, 'Feminino':1},
    's/n':{'Sim':1,'Não':2}
}

with colunas[0]:
    sexo = dict_options['sex'][st.radio("Sexo", options=dict_options['sex'].keys())]
    idade = st.slider("Idade", min_value=1, max_value=100)
    classificacao = dict_options['s/n'][st.radio("Ja teve COVID-19", options=dict_options['s/n'].keys())]
    pneumonia = dict_options['s/n'][st.radio("Indica se o paciente já tem inflamação dos sacos aéreos ou não.",options=dict_options['s/n'].keys())]
    diabetes = dict_options['s/n'][st.radio("Indica se o paciente tem diabetes ou não.",options=dict_options['s/n'].keys())]

with colunas[1]:
    copd= dict_options['s/n'][st.radio('Indica se o paciente tem doença pulmonar obstrutiva crônica ou não.',options=dict_options['s/n'].keys())]
    asma= dict_options['s/n'][st.radio('Indica se o paciente tem asma ou não.',options=dict_options['s/n'].keys())]
    hipertensao= dict_options['s/n'][st.radio('Indica se o paciente tem hipertensão ou não.',options=dict_options['s/n'].keys())]
    cardiovascular= dict_options['s/n'][st.radio('Indica se o paciente tem doença relacionada ao coração ou aos vasos sanguíneos.',options=dict_options['s/n'].keys())]

with colunas[2]:
    crônica_renal= dict_options['s/n'][st.radio('Indica se o paciente tem doença renal crônica ou não.',options=dict_options['s/n'].keys())]
    outra_doença= dict_options['s/n'][st.radio('Indica se o paciente tem outra doença ou não.',options=dict_options['s/n'].keys())]
    obesidade= dict_options['s/n'][st.radio('Indica se o paciente é obeso ou não.',options=dict_options['s/n'].keys())]
    tabaco= dict_options['s/n'][st.radio('Indica se o paciente é usuário de tabaco.',options=dict_options['s/n'].keys())]

cols = st.columns([2,1,2])
with cols[1]:
    if st.button('Estimar'):
        morte = prever_morte(sexo, pneumonia ,idade, diabetes, copd, asma, hipertensao, outra_doença, cardiovascular,obesidade,crônica_renal,tabaco,classificacao)
        if morte == 1:
            st.write('Procure um atendimento médico.\n Risco de morte!', morte)
        else:
            st.write('Seguro! \n não há riscos!', morte)