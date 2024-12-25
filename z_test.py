# Z -test
import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Datsframe
df = pd.DataFrame({
    'landing_page':['new_page', 'old_page'],
    'not_converted':[128045, 127785],
    'converted':[17264, 17489]})

#print(df)

# calculated total
df['total'] = df['not_converted'] + df['converted']

print(df)

convert_old = df.loc[df['landing_page']=='old_page', 'converted'].values[0]
convert_new = df.loc[df['landing_page']=='new_page', 'converted'].values[0]

total_old = df.loc[df['landing_page']=='old_page', 'total'].values[0]
total_new = df.loc[df['landing_page']=='new_page', 'total'].values[0]

count = np.array([convert_old, convert_new])
nobs = np.array([total_old, total_new])

#print(count)

# Perform z test
z_statistics, p_value = proportions_ztest(count, nobs, alternative = 'two-sided')

print("Z-statistics :-", z_statistics)
print("p-value :-", p_value)
