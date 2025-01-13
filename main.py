import streamlit as st


#st.sidebar.markdown("Instituto Federal de São Paulo - Pirituba")
# --- PAGE SETUP ---
pagina_inicial = st.Page(
    "views/pagina_inicial.py",
    title="Página Inicial",
    icon=":material/home:",
    default=True,
)

pagina_formulario = st.Page(
    "views/formulario_analise.py",
    title="Realizar Análise",
    icon=":material/analytics:",
)

pagina_sobre_nos = st.Page(
    "views/criadores.py",
    title="Criadores",
    icon=":material/contacts:",
)

pagina_documentacao = st.Page(
    "views/documentacao.py",
    title="Documentação",
    icon=":material/info:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation({
    "Projeto": [pagina_inicial, pagina_formulario],
    "Informações": [pagina_sobre_nos, pagina_documentacao],
})


# --- RUN NAVIGATION ---
pg.run()
