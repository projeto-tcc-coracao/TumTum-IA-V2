import streamlit as st

# configurando a página
st.set_page_config(page_title="TumTum IA",
                   page_icon="tumtum-icone.png",
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   menu_items=None,
                  )

with st.sidebar:
    st.write("Instituto Federal de São Paulo - Pirituba")

def justificar_texto(texto):

    # substituir as quebras de linha por <br> antes de usar a f-string
    texto_corrigido = texto.replace('\n', '<br>')

    # envolvendo todo o texto em uma tag <div> com estilo de justificação
    texto_formatado = f"<div style='text-align: justify; font-size: 16px'>{texto_corrigido}</div>"

    return texto_formatado

st.markdown(
    '''
    <div style="text-align: center; font-size: 30px; color: #1A1A1A; font-weight: bold; padding: 20px 0; max-width: 1200px; margin: 0 auto;">
        DOCUMENTAÇÃO DO PROJETO
    </div>
    ''',
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2, gap="medium")


with col1:
    contexto_projeto ="As doenças cardíacas estão entre as principais causas de mortalidade em todo o mundo, representando uma significativa ameaça à saúde. Diante desse cenário, a prevenção e o diagnóstico precoce tornam-se essenciais para reduzir a ocorrência dessas doenças e melhorar a qualidade de vida das pessoas."
    contexto_projeto = justificar_texto(contexto_projeto)
    
    st.markdown("<div style='text-align: center; font-size: 19px; background-color: #C4ECFF; padding: 10px; border-radius: 5px;'><b>CONTEXTO DO PROJETO</b></div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: left; font-size: 19px;'><b>1 - CONTEXTO DO PROJETO</b></div>", unsafe_allow_html=True)
    st.write("")

    st.markdown(contexto_projeto, unsafe_allow_html=True)
    st.write("---")

    objetivo_projeto = "Desenvolvimento de uma ferramenta baseada em técnicas de machine learning capaz de fornecer um pré-diagnóstico de doenças cardíacas, auxiliando médicos e pacientes na detecção precoce de possíveis problemas cardíacos."
    objetivo_projeto = justificar_texto(objetivo_projeto)

    st.markdown("<div style='text-align: center; font-size: 19px; background-color: #C4ECFF; padding: 10px; border-radius: 5px;'><b>OBJETIVO</b></div>",unsafe_allow_html=True)
    #st.markdown("<div style='text-align: left; font-size: 19px;'><b>2 - OBJETIVO</b></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown(objetivo_projeto, unsafe_allow_html=True)
    st.write("")

with col2:
    metodo_projeto = "Análise exploratória em uma base de dados pública contendo informações clínicas de 918 pacientes. Processamento de dados, utilização de técnicas de aprendizado de máquina e interface gráfica."
    metodo_projeto = justificar_texto(metodo_projeto)

    st.markdown("<div style='text-align: center; font-size: 19px; background-color: #C4ECFF ; padding: 10px; border-radius: 5px;'><b>MÉTODO</b></div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: left; font-size: 19px;'><b>3 - MÉTODO</b></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown(metodo_projeto, unsafe_allow_html=True)
    st.write("---")

    resultados_projeto = "O modelo de Regressão Logística foi o que teve melhor desempenho atingindo 86.36% de precisão, 89.06% para revocação e 87.68% no F1-Score, o qual está sendo utilizado nessa aplicação."
    resultados_projeto = justificar_texto(resultados_projeto)

    st.markdown("<div style='text-align: center; font-size: 19px; background-color: #C4ECFF; padding: 10px; border-radius: 5px;'><b>RESULTADO</b></div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: left; font-size: 19px;'><b> 4 - RESULTADO</b></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown(resultados_projeto, unsafe_allow_html=True)

st.write("---")
conclusao_projeto = "A aplicação das técnicas de inteligência artificial em conjunto com a plataforma web podem se tornar uma ferramenta valiosa para a detecção precoce de doenças cardíacas, beneficiando o sistema de saúde e melhorando o prognóstico dos pacientes."
conclusao_projeto = justificar_texto(conclusao_projeto)

st.markdown("<div style='text-align: center; font-size: 19px; background-color: #C4ECFF; padding: 10px; border-radius: 5px;'><b>CONCLUSÃO</b></div>", unsafe_allow_html=True)
#st.markdown("<div style='text-align: left; font-size: 19px;'><b> 5 - CONCLUSÃO</b></div>", unsafe_allow_html=True)
st.write("")
st.markdown(conclusao_projeto, unsafe_allow_html=True)





