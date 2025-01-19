import streamlit as st
import pandas as pd

# configurando a página
st.set_page_config(page_title="TumTum IA",
                   page_icon="tumtum-icone.png",
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   menu_items=None,
                  )

# st.image("tumtum-logo.png", use_container_width=True)


st.html(f'''
<div style="text-align: center; padding: 20px 0; max-width: 1200px; margin: 0 auto;"> 
    <!-- Heading Section -->
    <h1 style="font-size: 48px; color: #1A1A1A; margin-bottom: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: bold;">
        Descubra seus riscos cardíacos<br>em minutos
    </h1>

    <!-- Subheading -->
    <p style="font-size: 24px; color: #4A4A4A; margin-bottom: 40px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        Análise personalizada usando Inteligência Artificial
    </p>

    <!-- CTA Button with Hover Effect -->
    <style>
        .cta-button {{
            display: inline-block; 
            background-color: #FF4B6E; 
            color: white !important; 
            padding: 16px 48px; 
            border-radius: 50px; 
            text-decoration: none; 
            font-size: 24px; 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            font-weight: bold; 
            transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
        }}
        .cta-button:hover {{
            background-color: #E0435F;
            color: white !important;
            transform: translateY(-4px);
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        }}
    </style>

    <a href="/formulario_analise" class="cta-button">Faça sua Análise</a>
</div>
''')


st.html('''
<body>
<div style="display:flex; justify-content:space-between; align-items:center; padding:20px; max-width:1200px; margin:0 auto; gap:20px; font-family:sans-serif;">

    <div style="flex:1; text-align:center;">
        <div style="background-color:#b6ece3; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 10px;">
            <span style="color:#2C4251; font-size:24px;">👆</span>
        </div>
        <h3 style="color:#2C4251; font-size:18px; margin:0 0 8px;">Rápido e Fácil</h3>
        <p style="color:#4A5568; font-size:14px; margin:0; line-height:1.4;">Em poucos cliques você obtém as recomendações da nossa IA.</p>
    </div>

    <div style="flex:1; text-align:center;">
        <div style="background-color:#b6ece3; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 10px;">
            <span style="color:#2C4251; font-size:24px;">🚀</span>
        </div>
        <h3 style="color:#2C4251; font-size:18px; margin:0 0 8px;">Tecnologia Avançada</h3>
        <p style="color:#4A5568; font-size:14px; margin:0; line-height:1.4;">Uso de Inteligência Artificial para gerar recomendações com base nos seus exames.</p>
    </div>

    <div style="flex:1; text-align:center;">
        <div style="background-color:#b6ece3; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 10px;">
            <span style="color:#2C4251; font-size:24px;">💰</span>
        </div>
        <h3 style="color:#2C4251; font-size:18px; margin:0 0 8px;">Totalmente Gratuito</h3>
        <p style="color:#4A5568; font-size:14px; margin:0; line-height:1.4;">Buscamos trazer saúde e bem-estar para a população sem custo.</p>
    </div>

</div>
</body>

''')

st.html("""
    <div id="sobre" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; width: 100%; padding: 20px; color: #2C4251;">
        <h1 style="color: #40E0D0; font-size: 32px; margin-bottom: 8px; font-weight: 600;">Sobre o TumTum</h1>

        <p style="font-size: 16px; line-height: 1.6; margin-bottom: 24px; text-align: justify; white-space: normal;">
            Este projeto é resultado do Trabalho de Conclusão de Curso (TCC) dos estudantes de Análise e Desenvolvimento de Sistemas (ADS) 
            <span style="color: #1A365D;">Felipe Romani, Eduardo Brandão e Pedro Barauna</span>, 
            do Instituto Federal de São Paulo (IFSP) – campus Pirituba. Desenvolvido em 2024, o projeto tem como objetivo aplicar o conhecimento 
            adquirido ao longo do curso para criar uma solução tecnológica inovadora voltada para a área de saúde.
        </p>

        <p style="font-size: 16px; line-height: 1.6; text-align: justify; white-space: normal;">
            O produto, um sistema de checkup cardíaco, utiliza técnicas de aprendizado de máquina para analisar dados médicos 
            e oferecer uma avaliação rápida do risco de doenças cardíacas. A ideia surgiu a partir da necessidade crescente 
            de ferramentas acessíveis e intuitivas para ajudar no monitoramento de saúde, especialmente em tempos de alta 
            demanda por soluções digitais no setor médico.
        </p>
    </div>
""")

st.html("""
<div style="
    display: flex; 
    justify-content: center; 
    align-items: flex-start; /* Alinha o conteúdo no topo */
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    margin: 0; /* Remove margens externas */
    padding: 0; /* Remove espaçamento interno */">

    <div id="faq" style="max-width: 800px; padding: 0 20px; text-align: left;">
        <h1 style="color: #FF4B6E; font-size: 48px; text-align: center; margin: 5px 0;">Perguntas Frequentes</h1> <!-- Margens ajustadas -->

        <details style="margin-bottom: 10px; background: #F8F9FA; border-radius: 8px; padding: 15px; cursor: pointer;"> <!-- Margem e padding reduzidos -->
            <summary style="font-size: 24px; color: #2C4251; font-weight: 500; list-style: none; display: flex; justify-content: space-between; align-items: center;">
                Como o TumTum IA funciona?
                <span style="font-size: 24px; transition: transform 0.3s;">▼</span>
            </summary>
            <p style="margin-top: 10px; color: #4A5568; line-height: 1.6; font-size: 16px;"> <!-- Margem reduzida -->
                O usuário insere informações como resultados de exames de sangue e dados relacionados ao coração, e o sistema 
                processa esses dados para fornecer uma recomendação sobre o risco de doenças cardíacas.
            </p>
        </details>

        <details style="margin-bottom: 10px; background: #F8F9FA; border-radius: 8px; padding: 15px; cursor: pointer;">
            <summary style="font-size: 24px; color: #2C4251; font-weight: 500; list-style: none; display: flex; justify-content: space-between; align-items: center;">
                Quem pode usar este serviço?
                <span style="font-size: 24px; transition: transform 0.3s;">▼</span>
            </summary>
            <p style="margin-top: 10px; color: #4A5568; line-height: 1.6; font-size: 16px;">
                Qualquer pessoa que tenha resultados de exames recentes e deseje uma análise preliminar do seu risco cardíaco.
                O serviço é especialmente útil para aqueles que querem um acompanhamento preventivo da saúde do coração.
            </p>
        </details>

        <details style="margin-bottom: 10px; background: #F8F9FA; border-radius: 8px; padding: 15px; cursor: pointer;">
            <summary style="font-size: 24px; color: #2C4251; font-weight: 500; list-style: none; display: flex; justify-content: space-between; align-items: center;">
                Os resultados são confiáveis?
                <span style="font-size: 24px; transition: transform 0.3s;">▼</span>
            </summary>
            <p style="margin-top: 10px; color: #4A5568; line-height: 1.6; font-size: 16px;">
                O TumTum IA utiliza algoritmos avançados de aprendizado de máquina treinados com dados médicos reais. 
                No entanto, os resultados são indicativos e não substituem uma avaliação médica profissional.
            </p>
        </details>

        <details style="margin-bottom: 10px; background: #F8F9FA; border-radius: 8px; padding: 15px; cursor: pointer;">
            <summary style="font-size: 24px; color: #2C4251; font-weight: 500; list-style: none; display: flex; justify-content: space-between; align-items: center;">
                Meus dados estão seguros?
                <span style="font-size: 24px; transition: transform 0.3s;">▼</span>
            </summary>
            <p style="margin-top: 10px; color: #4A5568; line-height: 1.6; font-size: 16px;">
                Sim, todos os dados são processados de forma segura e não são armazenados permanentemente. 
                Seguimos rigorosos protocolos de privacidade e proteção de dados em conformidade com a LGPD.
            </p>
        </details>
    </div>
</div>
""")

st.write("")
st.markdown(
    '''
    <div style="text-align: center; font-size: 50PX; color: #2C3E50; font-weight: bold; max-width: 1200px; margin: 0 auto;">
        Contatos
    </div>
    ''',
    unsafe_allow_html=True
)
st.write("")

# Definindo colunas lado a lado
col1, col2 = st.columns([1, 1.2], gap="small")

# Coluna da esquerda - Card de informações
with col1:
    st.html("""    
    <div style="display: flex; gap: 40px; flex-wrap: wrap; justify-content: right;">
        <!-- Card de informações -->
        <div style="flex: 1; max-width: 500px; background: #F8F9FA; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: #2C4251; font-size: 32px; margin-bottom: 20px;">Entre em contato</h2> <!-- Reduzindo a margem do título -->

            <div style="margin-bottom: 20px;">
                <h3 style="color: #2C4251; font-size: 20px; margin-bottom: 12px; display: flex; align-items: center;">
                    <span style="margin-right: 10px;">✉️</span>
                    Email:
                </h3>
                <a href="mailto:projeto.dados.ifsp@gmail.com" 
                   style="color: #FF4B6E; text-decoration: none; font-size: 18px; display: block; margin-left: 30px;">
                   projeto.dados.ifsp@gmail.com
                </a>
            </div>

            <div>
                <h3 style="color: #2C4251; font-size: 20px; margin-bottom: 12px; display: flex; align-items: center;">
                    <span style="margin-right: 10px;">📍</span>
                    Endereço:
                </h3>
                <p style="color: #4A5568; font-size: 18px; line-height: 1.6; margin-left: 30px;">
                    Av. Mutinga, 951 - Jardim Santo Elias,<br>
                    São Paulo - SP, 05110-000
                </p>
            </div>

            <div style="margin-top: 20px;">
                <a href="https://www.google.com/maps?q=IFSP+Campus+Pirituba" 
                   target="_blank"
                   style="display: inline-block; background-color: #40E0D0; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-size: 16px; margin-left: 30px;">
                   Ver no Google Maps
                </a>
            </div>
        </div>
    </div>
</div>
    """)

with col2:

    location_data = pd.DataFrame({
    'latitude': [-23.487939],
    'longitude': [-46.735926]
    })
    
    st.map(location_data, zoom=14)

st.markdown(
    """
    <div style="text-align: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #FF4B6E;">
        <div style="margin-bottom: 0px;">
            <a href="#sobre" style="margin: 0 15px; font-size: 24px; color: #FF4B6E; text-decoration: none;">Sobre</a>
            <a href="#faq" style="margin: 0 5px; font-size: 24px; color: #FF4B6E; text-decoration: none;">FAQ</a>
            <a href="#contato" style="margin: 0 5px; font-size: 24px; color: #FF4B6E; text-decoration: none;">Contato</a>
        </div>
    </div>

    <div style="display: flex; gap: 20px; align-items: center; justify-content: center;">
        <a href="https://github.com/projeto-tcc-coracao/TumTum-IA-V2" target="_blank" style="text-decoration: none;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                 alt="GitHub" style="width: 50px; height: 50px;">
        </a>
        <a href="https://colab.research.google.com/drive/1wDlBsjQoJJqTyGIdSIl16qUMHE0yQ1jh?usp=sharing" 
           target="_blank" style="text-decoration: none;">
            <img src="https://colab.research.google.com/img/colab_favicon_256px.png" 
                 alt="Colab" style="width: 50px; height: 50px;">
        </a>
        <a href="https://ptb.ifsp.edu.br/index.php/superiores/ads" 
           target="_blank" style="text-decoration: none;">
            <img src="https://portais.ifsp.edu.br/scl/images/Logo_Campus/logo_IF.jpg" 
                 alt="Instituto Federal" style="width: 50px; height: 50px;">
        </a>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center; color: #333333; font-size: 16px; gap: 5px;">
        <span>Resultados da IA não substituem uma consulta médica.</span>
        <span>© TumTum IA. Todos os direitos reservados.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

