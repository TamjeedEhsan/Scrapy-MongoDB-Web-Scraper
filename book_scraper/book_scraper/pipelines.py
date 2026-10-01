from pymongo import MongoClient


class BookScraperPipeline:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")  #connects to local mongodb server
        self.db = self.client["book_scraper"]  #uses a database named book_scraper
        self.collection = self.db["books"]  #uess a collection named books

    def process_item(self, item, spider):
        book = vars(item)

        self.collection.update_one(
        {"url": book["url"]},
        {"$set": book},
        upsert=True,
        ) 
        #if the book URL already exists, update its data and if it doesnt exist, insert a new document
        
        # self.collection.insert_one(vars(item))  #inserts every scraped book as a document
        return item

    def close_spider(self, spider):
        self.client.close()   #closes the connection when scraping finishes