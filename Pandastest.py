import pandas as pd
# create two dataframes
customers = pd.DataFrame(
    {"customer_id": ["1","2","3","4","5"],
     "name":["John","Alice","Gordon","Matthew","Sarah"],
     "lastname":["Smith","Roberts","Hamilton","Woods","Carey"],
     "city": ["Kyoto", "Rookwood", "Wasgington", "Missauga", "Dubai", 'Chester'],
     "country": ["Japan", "United Kingdom", "USA", "Canada", "UAE", 'UK']
     }
)

occupation = pd.DataFrame(
    {"customer_id": ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32"],
     "Area_of_occupation": ["Astrogeologist","Biogeochemist","Climatologist","Dendroarchaeologist","Dendrologist","Edaphologist","Gemologist","Geoarchaeologist","Geobiologist","Geographer","Geologist","Geomicrobiologist","Geomorphologist","Geophysicist","Glaciologist","Hydrogeologist","Hydrologist","Hydrometeorologist","Limnologist","Meteorologist","Mineralogist","Oceanographer","Paleoclimatologist","Paleoecologist","Paleogeologist","Paleoseismologist","Palynologist","Petrologist","Sedimentologist","Seismologist","Speleologist","Volcanologist"]
     }
)

#merged_df = pd.merge(customers,info)
#merged_df.head()
#print(merged_df)


#inner join example
merged_df = customers.merge(occupation,
                            how='outer',
                            indicator=True,
                            on=['customer_id'])

merged_df.head()
print(merged_df)

merged_df.pivot(index='Area_of_occupation',
                columns='country',
                values='id')