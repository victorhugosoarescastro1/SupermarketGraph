import streamlit as st
import pandas as pd

st.set_page_config(page_title='modelo', layout='wide')

st.header('Gráfico de Vendas')

dados = pd.read_csv('dados/vendas.csv')
df = pd.DataFrame(dados)

combo_box = st.sidebar.multiselect('Escolha o mês desejado', df.columns, placeholder='Selecione')

if combo_box:
    st.write(df[combo_box])

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    col1.bar_chart(df[combo_box])



#EXPLICAÇÃO PASSO A PASSO DE COMO FUNCIONA

# NAS DUAS PRIMEIRAS LINHAS IREMOS IMPORTAR CÓDIGOS DE FORA PARA DENTRO DO CÓDIGO 
# O APELIDO DO STREAMLIT É  ""ST"" E O DO PANDAS É APELIDADO COMO ""PD""

#ELES PRÓPRIOS VEM JÁ COM BLOCO DE CÓDIGOS QUE JÁ SALVA A PELE DO PROGRAMADOR

# LINHA 4 = CRIA UMA ARQUITETURA DA PÁGINA, PODENDO FAZER VÁRIAS CONFIGURAÇÕES LÁ

# LINHA 6 = O HEADER É DESCRITO COMO FOSSE O TÍTULO DA PÁGINA QUE A GENTE QUER QUE APAREÇA 

# LINHA 8 = O PANDAS FAZ UMA LEITURA DO ARQUIVO DO CSV QUE ESTÁ DENTRO DA PASTA "dados" 

# LINHA 9 = A PARTIR DESSA LEITURA ANTERIOR, O PANDAS "pd" ORGANIZA OS DADOS DO CSV EM LINHAS EM COLUNAS PARA CRIAÇÃO DA TABELA / pd.DATAFRAME = BIDIMENSIONAL (LINHAS E COLUNAS)
#                                                     (TODA ESSA CONFIGURAÇÃO É GUARDADA EM ""df"")

# LINHA 11 = OUTRO RECURSO QUE UTILIZOU FOI O RECURSO "SIDEBAR.MULTISELECT" CRIANDO UM BLOCO INTERATIVO EM FORMATO DE COLUNAS "df.columns"
# DENTRO DA CAIXA DO "df.columns" COLOCA-SE O TEXTO A PARTIR DO "placeholder"





