import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

################################################

# Original dataset
df_filename = '../data/raw/scraped_data.csv'

# Additional dataset
df2_filename = '../data/raw/final_cleaned_data_Racoons_command.csv'

# Joined dataset
df_combined_filename = '../data/raw/combined_data_from_victor.csv'

################################################

df = pd.read_csv(df_filename,delimiter=',',encoding='utf-8')
df_2 = pd.read_csv(df2_filename,delimiter=',',encoding='utf-8')

# Drop the column Url because it needn't for analysis
col = 'Url'  
if col in df.columns:
    df.drop(columns=[col], inplace=True)

# Rename columns
df.columns = ['property_id', 'locality', 'postal_code', 'price', 'property_type','property_subtype', 'sale_type','rooms', 'area','has_equipped_kitchen', 'is_furnished', 'has_open_fire','has_terrace','has_garden','facades_number', 'has_swimming_pool','state']

df_2.columns = (
    df_2.columns
      .str.replace(r"\(.*?\)", "", regex=True)  
      .str.strip()                               
      .str.replace(" ", "_")                     
)

df_2.columns = ['property_id', 
                'locality', 
                'postal_code', 
                'property_type',
                'property_subtype', 
                'price', 
                'rooms', 
                'area',
                'has_equipped_kitchen', 
                'is_furnished', 
                'has_open_fire',
                'has_terrace',
                'terrace_area',
                'has_garden',
                'facades_number', 
                'has_swimming_pool',
                'state']

##################################################################

# Types conversion

for col in set(df.columns) & set(df_2.columns):
    try:
        df_2[col] = df_2[col].astype(df[col].dtype)
    except:
        pass  

##################################################################

# Compare two datasets
df_diff = df_2[~df_2['property_id'].isin(df['property_id'])]
print( 'Difference: ',df_diff.shape )

df_combined = pd.concat([df, df_diff], ignore_index=True, sort=False)

print( 'All data:', df_combined.shape, '\n\n')

print(df_combined.info())

df_combined.to_csv(df_combined_filename, index=False, encoding='utf-8')

##################################################################


#print('Main dataset:\n')
#print(df.info())
#print('Second dataset:\n')
#print(df_2.info())

#print( df.head(4).transpose() )
#print( df_2.head(4).transpose() )


