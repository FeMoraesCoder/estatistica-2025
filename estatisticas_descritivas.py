#%% 
import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df.head()
# %%
print("Estatisticas de Posição para Transações\n")


minimo = df['qtdPontos'].min()
print("Minimo: ", minimo)

media = df['qtdPontos'].mean()
print("Média: ", media)

quartil_1 = df['qtdPontos'].quantile(0.25)
print("1º Quartil: ", quartil_1)

mediana = df["qtdPontos"].median()
print("Mediana: ", mediana)

quartil_3 = df["qtdPontos"].quantile(0.75)
print("3º Quartil: ", quartil_3)

maximo = df["qtdPontos"].max()
print("Máximo: ", maximo)

df["qtdPontos"].describe() # Aqui ele trás de forma direta as estatísticas descritivas
# %%

print("####################################")
print("\n")

usuarios = (df.groupby(["idUsuario"]).agg({
    "idTransacao": "count",
    "qtdPontos": "sum",
})
                                    .reset_index())

usuarios[['idTransacao', 'qtdPontos']].describe()
# %%


 