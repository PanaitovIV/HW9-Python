# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

work = pd.read_csv('task_1/california_housing_train.csv')
answer = work.loc[work['population']<=work['population'].min()*1.1, ['households']].max()
print(answer)