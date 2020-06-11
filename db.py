import os
import pandas as pd
import pymongo
import json
from config import databaseusername, databasepassword

def import_content(filepath):
    mng_client = pymongo.MongoClient(f'mongodb+srv://{databaseusername}:{databasepassword}@george-ilsoc.gcp.mongodb.net/test?retryWrites=true&w=majority')
    mng_db = mng_client['housing'] # Replace mongo db name
    collection_name = 'texas' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.delete_many({})
    db_cm.insert_many(data_json)

if __name__ == "__main__":
  filepath = 'data/complete_df.csv'  # pass csv file path
  import_content(filepath)