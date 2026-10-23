import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Augusto Gois | Portfólio", page_icon="💻", layout="wide"
)

# Título principal do site
st.title("🚀 Augusto Gois | Portfólio & Projetos")
st.markdown(
    "Bem-vindo ao meu espaço na web! Aqui você encontra ferramentas, scripts e"
    " aplicações desenvolvidas por mim em Python. Sinta-se à vontade para"
    " testar, baixar e conferir o código no GitHub."
)

st.divider()

# --- CRIANDO AS ABAS PRINCIPAIS ---
aba_portfolio, aba_servicos, aba_loja, aba_contato = st.tabs([
    "📂 Portfólio & Downloads",
    "🛠️ Serviços de TI",
    "🛒 Produtos & Acessórios",
    "📬 Contato",
])

# --- ABA 1: PORTFÓLIO & DOWNLOADS ---
with aba_portfolio:
  st.header("Meus Softwares e Ferramentas")
  st.write(
      "Aqui estão as aplicações desktop e scripts desenvolvidos por mim em Python:"
  )

  col1, col2, col3, col4 = st.columns(4)

  with col1:
    st.subheader("⏱️ Aplicativo Cronômetro")
    st.write("Aplicação desktop em Python convertida em executável.")
    st.markdown(
        "[🔗 Ver Código no GitHub]"
        "(https://github.com/Augustogois/cronometro)"
    )
    with open("cronometro.exe", "rb") as arquivo:
      st.download_button(
          "📥 Baixar Executável",
          data=arquivo,
          file_name="cronometro.exe",
          key="btn1",
      )

  with col2:
    st.subheader("💰 Calculadora de CDB")
    st.write("Calculadora financeira integrada com dados do Banco Central.")
    st.markdown(
        "[🔗 Ver Código no GitHub]"
        "(https://github.com/Augustogois/calculadora-de-cdb)"
    )
    with open("main.exe", "rb") as arquivo:
      st.download_button(
          "📥 Baixar Executável",
          data=arquivo,
          file_name="main.exe",
          key="btn2",
      )

  with col3:
    st.subheader("App de Transcrição")
    st.write("Aplicação para transcrever vídeos em texto.")
    st.markdown(
        "[🔗 Ver Código no GitHub]"
        "(https://github.com/Augustogois/videotranscripter)"
    )
    with open("videotranscript.exe", "rb") as arquivo:
      st.download_button(
          "📥 Baixar Executável",
          data=arquivo,
          file_name="videotranscript.exe",
          key="btn3",
      )

  with col4:
    st.subheader("Jogo Sudoku")
    st.write("Jogo de lógica Sudoku em Python.")
    st.markdown(
        "[🔗 Ver Código no GitHub](https://github.com/Augustogois/sudoku)"
    )
    with open("sudoku.exe", "rb") as arquivo:
      st.download_button(
          "📥 Baixar Executável",
          data=arquivo,
          file_name="sudoku.exe",
          key="btn4",
      )

# --- ABA 2: PRESTAÇÃO DE SERVIÇOS ---
with aba_servicos:
  st.header("Serviços Profissionais")
  st.write(
      "Precisa de automação, planilhas inteligentes ou scripts personalizados"
      " para o seu negócio? Eu posso ajudar!"
  )

  s1, s2, s3 = st.columns(3)
  with s1:
    st.markdown("### 🤖 Automação de Processos")
    st.write(
        "Criação de scripts em Python para automatizar tarefas repetitivas e"
        " extração de dados."
    )
  with s2:
    st.markdown("### 📊 Painéis e Dashboards")
    st.write(
        "Desenvolvimento de interfaces interativas e painéis dinâmicos para"
        " dados."
    )
  with s3:
    st.markdown("### 💻 Desenvolvimento Sob Medida")
    st.write("Criação de pequenas ferramentas desktop e utilitários.")
  st.info("💡 Interessado? Entre em contato pela aba de Contato!")

# --- ABA 3: LOJA DE PRODUTOS FÍSICOS ---
with aba_loja:
  st.header("Vitrine de Produtos")
  st.write("Conheça alguns dos produtos físicos e acessórios disponíveis.")
  p1, p2 = st.columns(2)
  with p1:
    st.subheader("🎒 Acessório / Gadget Tech")
    st.write("Descrição do produto físico.")
    st.markdown("**Preço:** R$ 99,90")
    st.link_button("🛒 Comprar Agora", "https://www.mercadopago.com.br")
  with p2:
    st.subheader("⌨️ Periférico Exclusivo")
    st.write("Descrição de outro item à venda.")
    st.markdown("**Preço:** R$ 149,90")
    st.link_button("🛒 Comprar Agora", "https://www.mercadopago.com.br")

# --- ABA 4: CONTATO DIRETO ---
with aba_contato:
  st.header("Fale Comigo")
  with st.form("form_contato"):
    nome = st.text_input("Seu Nome")
    email = st.text_input("Seu E-mail")
    mensagem = st.text_area("Sua Mensagem")
    enviar = st.form_submit_button("Enviar Mensagem")
    if enviar:
      if nome and email and mensagem:
        st.success(f"Obrigado, {nome}! Mensagem enviada com sucesso.")
      else:
        st.warning("Preencha todos os campos.")

# --- BARRA LATERAL (FIXA) ---
st.sidebar.title("Contato & Links")
st.sidebar.markdown("[Meu Perfil no GitHub](https://github.com/Augustogois/)")
st.sidebar.markdown(
    "[Conecte-se no LinkedIn](https://www.linkedin.com/in/augusto-gois/)"
)