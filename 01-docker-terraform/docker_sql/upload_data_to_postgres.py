#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pd.__version__


# In[5]:


df = pd.read_csv("yellow_tripdata_2021-01.csv", nrows=1000)


# df

# In[7]:


# We need to generate a schema for the dataset to transfer to Postgres


# In[12]:


#First, we convert the datetime columns to their appropriate value
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime  = pd.to_datetime(df.tpep_dropoff_datetime)


# In[18]:


#We create a conenction to the postgres database. We use sqlalchemy for this

from sqlalchemy import create_engine


# In[19]:


engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")


# In[20]:


engine.connect()


# In[21]:


print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))


# In[40]:


#We not import the whole dataset. We use iterators to chunk the process into several batches

df_iter = pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=100000)


# In[41]:


df = next(df_iter)


# In[42]:


len(df)


# In[33]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime  = pd.to_datetime(df.tpep_dropoff_datetime)


# In[34]:


#importing only  the first header rows to postgres
df.head(n=0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")


# In[35]:


#importing the data not from the first iterator
get_ipython().run_line_magic('time', 'df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")')


# In[43]:


from time import time


# In[46]:


#Finally, we import all chunks from all iterators. We use a While loop

while True:
    try:
        t_start = time()
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime  = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")
        t_end = time()

        print("inserted another chunk..., took %.3f seconds" % (t_end - t_start))
    except StopIteration:
        print("All chunks processed!")
        break



# In[ ]:





# In[ ]:




