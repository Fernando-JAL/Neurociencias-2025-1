import pandas as pd
import numpy as np

array = np.random.uniform(-10, 10, size=[4,4])

# Representación en jupyter
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])

print(df)