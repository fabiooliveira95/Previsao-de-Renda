import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
    page_title="analise_de_dados",
    page_icon=":bar_chart:",
    layout="wide"
)

st.write('# Análise exploratória da previsão de renda')

# Load dataset
renda = pd.read_csv('previsao_de_renda.csv')

# Convert relevant columns to datetime where applicable
renda['data_ref'] = pd.to_datetime(renda['data_ref'], errors='coerce')

# Sidebar filters
st.sidebar.title('Filtros')

min_data = renda['data_ref'].min()
max_data = renda['data_ref'].max()

st.write("Data mínima:", min_data)
st.write("Data máxima:", max_data)

data_inicial = st.sidebar.date_input('Data inicial',
                                     value=min_data,
                                     min_value=min_data,
                                     max_value=max_data)

data_final = st.sidebar.date_input('Data final',
                                   value=max_data,
                                   min_value=min_data,
                                   max_value=max_data)

st.sidebar.write('Data inicial escolhida:', data_inicial)
st.sidebar.write('Data final escolhida:', data_final)

# Filter data based on sidebar inputs
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)

renda = renda[(renda['data_ref'] >= data_inicial) & (renda['data_ref'] <= data_final)]

# Plotting
fig, ax = plt.subplots(8, 1, figsize=(10, 70))

sns.histplot(data=renda, x='renda', hue='posse_de_imovel', ax=ax[0], kde=True)
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)

sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7, 1, figsize=(10, 50))

sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2])
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3])
sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4])
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6])

sns.despine()
st.pyplot(plt)
