import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
import time

st.set_page_config(
    page_title="Painel de Monitoramento de PCs",
    page_icon="📊",
    layout="wide"
)

def carregar_dados(limite=100):
    conn = sqlite3.connect('pcs.db', timeout=10)
    query = f'''
        SELECT timestamp, pc_id, uso_cpu, uso_ram, temp_cpu
        FROM leituras_pcs
        ORDER BY id DESC
        LIMIT {limite}
    '''
    df = pd.read_sql_query(query,conn)
    conn.close()
    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
    return df

st.title("Monitoramento de PCs em Tempo Real")

#Barra lateral de controle
st.sidebar.header("Filtros de controle")
intervalo_atualizacao = st.sidebar.slider("Frequência de atualização (segundos):",1,10,2)
quantidade_registros = st.sidebar.slider("Histórico de leituras:", 30, 300, 120)
df = carregar_dados(limite=quantidade_registros)

if df.empty:
    st.info("Aguardando dados... Certifique-se de que o 'simulador.py' está rodando")
else:
    pcs_disponiveis = df['pc_id'].unique().tolist()
    pc_selecionado = st.sidebar.selectbox("Filtrar por Pc:", ["Todos"] + pcs_disponiveis)
    
    if pc_selecionado != "Todos":
        df_filtrado = df[df['pc_id'] == pc_selecionado]
    else:
        df_filtrado = df
        
    #Indicadores dos últimos valores
    st.subheader("Últimas leituras registradas")
    ultimos = df_filtrado.groupby('pc_id').last().reset_index()
    cols = st.columns(len(ultimos))
    
    for idx, row in ultimos.iterrows():
        with cols[idx]:
            st.markdown(f"### {row['pc_id']}")
            st.metric("Uso CPU", f"{row['uso_cpu']} %")
            st.metric("Uso RAM", f"{row['uso_ram']} %")
            st.metric("Temperatura CPU", f"{row['temp_cpu']} ºC")
    
    st.markdown("---")
    
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        fig_temp = px.line(
            df_filtrado,
            x='timestamp',
            y='temp_cpu',
            color='pc_id',
            title="Temperatura (°C) ao longo do tempo",
            markers=True
        )
        fig_temp.update_xaxes(title="Horário")
        fig_temp.update_yaxes(title="C")
        st.plotly_chart(fig_temp, use_container_width=True)
        
    with col_g2:
        fig_umid = px.line(
            df_filtrado,
            x='timestamp',
            y='uso_cpu',
            color='pc_id',
            title="Uso da CPU relativo (%) ao longo do tempo",
            markers=True
        )
        fig_umid.update_xaxes(title="Horário")
        fig_umid.update_yaxes(title="%")
        st.plotly_chart(fig_umid, use_container_width=True)
        
    with st.expander("Visualizar tabela de registros"):
        st.dataframe(df_filtrado.sort_values('timestamp', ascending=False), use_container_width=True)
        
#Loop de atualização automática em tempo real
time.sleep(intervalo_atualizacao)
st.rerun()