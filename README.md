Book Store Data Analysis Project

Hey! This is a project I built to practice the tools used in data analyst roles.
The idea was to scrape some real product data, clean it up, store it in a database,
run SQL queries on it, and then visualize everything in Tableau.

I used a practice website called [books.toscrape.com](http://books.toscrape.com) —
it's made for scraping projects so there are no issues using it.

---

Tools Used

- **Python + Selenium** — to scrape book listings across multiple pages
- **pandas** — to clean and transform the raw data
- **MySQL** — to store the data and run SQL queries
- **SQLAlchemy** — to connect pandas to MySQL without warnings
- **Tableau** — to build an interactive dashboard

---

Questions I Wanted to Answer

- Do expensive books actually get better ratings?
- Which books are the best value for money (5 stars + cheapest price)?
- How many books are in stock vs out of stock?
- Which expensive books have bad ratings and might need a discount?

---

Project Structure

```
book-analysis/
├── book_analysis.ipynb   ← everything in one Jupyter notebook
├── scraper.py            ← scrapes the data using Selenium
├── clean_data.py         ← cleans and transforms with pandas
├── analyze.py            ← quick analysis and summary tables
├── load_to_mysql.py      ← sets up MySQL and loads data
├── queries.sql           ← all the SQL queries I used
├── tableau_export.py     ← exports CSVs for Tableau
├── requirements.txt
└── data/                 ← generated files (not tracked by git)
    ├── raw_books.csv
    ├── clean_books.csv
    ├── summary.csv
    ├── tableau_all_books.csv
    ├── tableau_summary.csv
    └── tableau_by_rating.csv
```

---

## 🚀 How to Run It

**1. Install the libraries**

```bash
pip install -r requirements.txt
```

**2. Update your MySQL password**

Open `load_to_mysql.py` (or the notebook) and change this line:

```python
DB_PASSWORD = "Password"   # change this to your actual password
```

**3. Make sure MySQL is running on your computer**

**4. Run the scripts in order**

```bash
python scraper.py
python clean_data.py
python analyze.py
python load_to_mysql.py
python tableau_export.py
```

Or just open `book_analysis.ipynb` and run all cells from top to bottom — it does everything in one place!

---

## 🗄️ Database Schema

```sql
CREATE TABLE books (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    title          VARCHAR(500),
    price          DECIMAL(6, 2),
    rating         INT,
    in_stock       VARCHAR(5),
    price_category VARCHAR(20)
);
```

---

## 🔍 SQL Queries

| Query | Question |
|-------|----------|
| Q1 | How many books are in each price category? |
| Q2 | What is the average price per star rating? |
| Q3 | Which 5-star books are the cheapest? |
| Q4 | Do expensive books get better ratings? |
| Q5 | How many books are in stock vs out of stock? |
| Q6 | Which expensive books have bad ratings? |
| Q7 | Full summary by price category |

---

## 📊 Tableau Dashboard

After running `tableau_export.py`, import the CSV files from the `data/` folder into Tableau.

You can also connect Tableau directly to MySQL:
- Go to **Connect → To a Server → MySQL**
- Server: `localhost`
- Database: `bookstore`
- Table: `books`

Charts I made for the dashboard:
- Bar chart — number of books per price category
- Scatter plot — price vs rating (does price predict quality?)
- KPI cards — total books, average price, average rating, % in stock
- Table — top 10 best value books

> 

---

## ⚠️ Note on the SQLAlchemy Warning

If you see this warning when running SQL queries:

```
UserWarning: pandas only supports SQLAlchemy connectable...
```

Make sure you're using the SQLAlchemy engine to connect, not the raw `mysql-connector` object.
The notebook and scripts already handle this — just make sure you run the engine setup cell first.

---

## 📝 What I Learned

- Selenium needs `time.sleep()` otherwise it tries to scrape before the page loads
- Data cleaning takes way longer than expected — just the price column needed 3 fixes
- `GROUP BY` in SQL is super useful for summarizing data quickly
- pandas needs SQLAlchemy to connect to MySQL cleanly (not the raw connector)
- Connecting Tableau directly to MySQL is easier than exporting CSVs every time

---

## ⚙️ Requirements

```
selenium
pandas
mysql-connector-python
sqlalchemy
pymysql
```

Install everything with:

```bash
pip install -r requirements.txt
```

---

*Built as a portfolio project while learning data analytics. Open to any feedback!* 😊
