# Lukas Elsrode - (19/29/2020) - Completed Project for IT department changin

import pandas as pd
from math import ceil

# Init dictionday {fields: count}  
d_fields = {'Browser': 'Number of Browser Sessions',
            'Exchange ActiveSync': 'Number of Exchange ActiveSync Sessions',
            'Exchange Web Services': 'Number of Exchange Web Services Sessions',
            'MAPI over HTTP': 'Number of MAPI over HTTP Sessions'}


def make_data(filename='data.csv'):
    return pd.read_csv(filename)

def fill_categories_for_rows(df=make_data(),d_fields=d_fields):
    ''' Fills the Category in Dataframe
    '''
    for i,r in df.iterrows():

        row_values = r.dropna()
        cat = []
        max_c = 0

        for num_of in d_fields.values():
            try:
                count = int(row_values[num_of])
                if count > max_c:
                    max_c = count
            except:
                count = None
            if count:
                key = ' '.join(num_of.split(' ')[2:][:-1])
                tup = (key,count)
                cat.append(tup)

        if 'Zero Byte.1' in row_values.index:
            print(row_values)
            df.at[i,'Category'] = None
    
        else:
            if len(cat) == 1:
                df.at[i,'Category'] = cat[0][0]
            
            if len(cat) > 1:
                ans = [i[0] for i in cat if i[1] >= (max_c * 0.20)]
                ans = ' & '.join(ans)
                df.at[i,'Category'] = ans
    return df

def save_as_xlsx(df,date='NEW'):
    '''Saves the updated CSV as an Excel File'''

    file_name = 'Basic-Auth-Users-Service-Desk-Labelled-verbose-Lukas-' + date + '.xlsx'
    writer = pd.ExcelWriter(file_name)
    df.to_excel(writer, index=False)
    writer.save()
    return


if __name__ == "__main__":

    # Fill the rows
    df_cated = fill_categories_for_rows()
    # Save the File 
    save_as_xlsx(df_cated)
