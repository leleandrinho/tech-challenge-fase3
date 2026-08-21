
import pandas as pd
import os
print(os.getcwd())

caminho_dados = r"../data/"
alunos = pd.read_parquet(caminho_dados + 'alunos.parquet')

