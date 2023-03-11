from os import getenv
from typing import Optional, Dict

import pandas as pd
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(getenv("MONGO_URL"), tlsCAFILE=where())["Database"]

    def __init__(self, collection: str):
        self.collection = self.database[collection]

    def seed(self, amount=1000):
        """Randomly Generate a list of 1000 monsters and insert them into MongoDB"""
        data = [Monster().to_dict() for _ in range(amount)]
        return self.collection.insert_many(data).acknowledged

    def reset(self):
        """Remove all documents from the collection"""
        return self.collection.drop()

    def count(self) -> int:
        """Return the number of documents present in the collection"""
        return self.collection.count_documents({})

    def dataframe(self, query: Optional[Dict] = None):
        """Return all documents present in the collection as a DataFrame"""
        return DataFrame(list(self.collection.find(query, {"_id": False})))

    def html_table(self) -> str:
        """Convert DataFrame to HTML table or return None if the collection is empty"""
        if self.count() == 0:
            return 'None'
        else:
            return self.dataframe().to_html()


if __name__ == '__main__':
    test = Database('Database')
    test.reset()
    test.seed()
    print(test.count())
