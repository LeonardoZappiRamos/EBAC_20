import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  box_diamonds = sns.lineplot(data=df_gasolina, x="dia", y="venda")
  box_diamonds.set(title='Preço da Gasolina')
  box_diamonds.figure.set_size_inches(w=20/2.54 , h= 15/2.54)

plt.savefig('gasolina.png')