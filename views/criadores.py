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

st.markdown(
    '''
    <div style="text-align: center; font-size: 30PX; color: #1A1A1A; font-weight: bold; padding: 20px 0; max-width: 1200px; margin: 0 auto;">
        CRIADORES DO PROJETO
    </div>
    ''',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("imagens/imagem_eduardo.jpg", "Eduardo Brandão Ferrari")
    st.link_button(label="LinkedIn", url ="https://www.linkedin.com/in/eduardobrand%C3%A3oferrari/", use_container_width=True)

with col2:
    st.image("imagens/imagem_felipe.enc", "Felipe Romani")
    st.link_button(label="LinkedIn", url ="https://www.linkedin.com/in/feliperomani/", use_container_width=True)

with col3:
    st.image("imagens/imagem_pedro.enc", "Pedro Barauna")
    st.link_button(label="LinkedIn", url ="https://www.linkedin.com/in/pedrobarauna/", use_container_width=True)

with col4:
    st.image("imagens/imagem_fabio.jpg", "Fabio Teixeira")
    st.link_button(label="LinkedIn", url ="https://www.linkedin.com/in/fabioteixeira/", use_container_width=True)



