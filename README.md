# Scrapy-MongoDB-Web-Scraper

Project Overview

This project demonstrates a basic web-scraping and data-storage pipeline using Python, Scrapy, and MongoDB.

The spider crawls the website's catalogue, extracts book information, follows pagination, converts selected fields into appropriate data types, and stores each book as a MongoDB document.

Technologies Used
Python — programming language
Scrapy — web scraping and crawling framework
PyMongo — Python driver for MongoDB
MongoDB Community Server — document database
MongoDB Compass — graphical database viewer
Architecture
Books to Scrape
      |
      v
Scrapy Spider
      |
      v
Extract book fields
      |
      v
Clean and transform data
      |
      v
BooksItem
      |
      v
Scrapy Item Pipeline
      |
      v
PyMongo
      |
      v
MongoDB
Data Collected

Each book document contains:

Field	Description	Data type
title	Book title	String
price	Book price	Float
rating	Rating from 1 to 5	Integer
availability	Stock availability text	String
url	Full URL of the book	String

MongoDB also automatically generates an _id field for each document.

Features
Extracts book titles, prices, ratings, availability, and URLs.
Crawls multiple catalogue pages using pagination.
Converts prices to numeric values and ratings to integers.
Converts relative book links into absolute URLs.
Stores scraped books in MongoDB.
Uses the book URL to update existing records or insert new ones, preventing duplicate records when the spider is rerun.
Project Results

The scraper was successfully run against the Books to Scrape catalogue.

Check	Result
Documents stored	1,000
Unique book URLs	1,000
Missing titles	0
Missing prices	0
Missing ratings	0
Missing URLs	0

The price aggregation returned:

Minimum price: £10.00
Maximum price: £59.99
Average price: £35.07

These results reflect the data collected during the project run.

Setup and Installation
Prerequisites
Python
MongoDB Community Server
MongoDB Shell (mongosh)
pip
1. Clone the repository
git clone <your-repository-url>
cd "Scrapy + MongoDB Web Scraper"

Replace <your-repository-url> with your repository URL. If you're using your existing local project, skip this step.

2. Create and activate a virtual environment

On Windows PowerShell:

python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
pip install scrapy pymongo
4. Start MongoDB

Ensure the MongoDB Community Server service is running locally.

The project connects to:

mongodb://localhost:27017/
5. Run the spider

Navigate to the Scrapy project directory:

cd book_scraper
scrapy crawl books

The scraped records are stored in the book_scraper database, in the books collection.

Verify the Data

Open MongoDB Shell:

mongosh

Run these MongoDB commands:

use book_scraper

// Count stored books
db.books.countDocuments()

// View one book
db.books.findOne()

// Count unique book URLs
db.books.distinct("url").length

You can also browse the database visually in MongoDB Compass by connecting to mongodb://localhost:27017.
