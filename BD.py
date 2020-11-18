import pandas as pd

df = pd.read_csv('C:/Users/baikalvel/Desktop/PROJECT/DATASET.csv', error_bad_lines=False, sep=';')
kaloris = ['Наименование', 'Калорийность', 'Жиров', 'Белков', 'Углеводов']
k_df = df[kaloris]
name = []
kal = []
bel = []
ugl = []
zir = []
for i in k_df['Наименование']:
    name.append(i)
for i in k_df['Калорийность']:
    kal.append(i)
for i in k_df['Белков']:
    bel.append(i)
for i in k_df['Углеводов']:
    ugl.append(i)
for i in k_df['Жиров']:
    zir.append(i)
