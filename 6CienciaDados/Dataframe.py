import pandas as pd
import numpy as np



cliente = { "Nome": ['Marcelo', 'Ana', 'Maria'],
            "Idade": [33, 26, 45]
}

print(cliente)
print("\n\n")

dataframe = pd.DataFrame(cliente)

print(dataframe)


vetor = np.array([5, 6, 7, 8])

v = pd.Series(vetor)

print(vetor)
print("\n\n")
print(v)