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

# Configuração do layout com título e estilo
st.html("""
    <div id="contato" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 1200px; padding: 20px;">
        <h1 style="color: #2C4251; font-size: 48px; text-align: center; margin-bottom: 5px;">Contatos</h1> <!-- Diminuindo o margin-bottom -->
    </div>
    """)

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

st.html("""
    <div style="text-align: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #FF4B6E;">
        <div style="margin-bottom: 20px;">
            <a href="#sobre" style="margin: 0 15px; font-size: 24px; color: #FF4B6E; text-decoration: none;">Sobre</a>
            <a href="#faq" style="margin: 0 15px; font-size: 24px; color: #FF4B6E; text-decoration: none;">FAQ</a>
            <a href="#contato" style="margin: 0 15px; font-size: 24px; color: #FF4B6E; text-decoration: none;">Contato</a>
        </div>

        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
            <a href="https://github.com/" target="_blank" style="text-decoration: none;">
                <div style="width: 50px; height: 50px; background-color: #f1f1f1; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width: 24px; height: 24px;">
                </div>
            </a>
            <a href="https://ptb.ifsp.edu.br/index.php/superiores/ads" target="_blank" style="text-decoration: none;">
                <div style="width: 50px; height: 50px; background-color: #f1f1f1; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                    <img src="https://portais.ifsp.edu.br/scl/images/Logo_Campus/logo_IF.jpg" alt="IFSP" style=" height: 24px;">
                </div>
            </a>
            <a href="https://colab.research.google.com/drive/1wDlBsjQoJJqTyGIdSIl16qUMHE0yQ1jh?usp=sharing" target="_blank" style="text-decoration: none;">
                <div style="width: 50px; height: 50px; background-color: #f1f1f1; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                    <img src="data:image/png;base64,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" alt="Colab" style=" height: 24px;">
                </div>
            </a>
        </div>

        <div style="color: #333333; font-size: 16px;">
            Resultados da IA não substituem uma consulta médica.<br>
            © TumTum IA. Todos os direitos reservados.
        </div>
    </div>
    """)