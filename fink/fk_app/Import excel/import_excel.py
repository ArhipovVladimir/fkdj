import pandas as pd
import numpy as np
data = pd.reade_excel('reestr.xlsx',
                      skiprows=13,
                      usecols='B:M')

# data ['Адрес'] = np.where(data['№опер.']).str.startswith('POS'),
#                           data['№опер.']).str.split(',', n=1).str[1],
#                           np.nan)
#
# data ['POSTID'] = np.where(data['№опер.']).str.startswith('POS'),
#                           data['№опер.']).str.split('(', n=1).str[1].str.split(')', n=1).str=[0],
#                           np.nan)
#
# data ['Адрес'] = data['Адрес'].flild()
# data ['POSTID'] = data['POSTID'].flild()



print(data)