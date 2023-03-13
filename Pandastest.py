import pandas as pd
# create two dataframes
customers = pd.DataFrame(
    {"customer_id": ["1","2","3","4","5"],
     "name":["John","Alice","Gordon","Matthew","Sarah"],
     "lastname":["Smith","Roberts","Hamilton","Woods","Carey"]}
)

info = pd.DataFrame(
    {"customer_id": ["2","3","5","4","1","6"],
    "city":["Kyoto","Rookwood","Wasgington","Missauga","Dubai",'Chester'],
     "country":["Japan","United Kingdom","USA","Canada","UAE",'UK']
    }

)

#merged_df = pd.merge(customers,info)
#merged_df.head()
#print(merged_df)


#inner join example
merged_df = customers.merge(info,
                            how='left')
merged_df.head()
print(merged_df)