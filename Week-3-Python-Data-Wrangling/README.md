# Week 3 – Python & Data Wrangling

This folder contains the Week 3 practical work based on the supplied Data Analyst Course PDF.

## Topics
- Python basics: data structures, functions, and scripting
- Pandas for data manipulation
- Reading CSV files
- Filtering rows
- Creating and manipulating columns
- Introductory Matplotlib and Seaborn visualization

## Assignment
Clean a messy dataset in Pandas by:
- Handling missing values
- Removing duplicates
- Filtering rows
- Creating new columns
- Producing basic visualizations

## Files

```text
Week-3-Python-Data-Wrangling/
├── Python/
│   └── week3_python_data_wrangling.py
├── data/
│   ├── messy_sales_data.csv
│   └── cleaned_sales_data.csv   # generated after running the Python file
├── revenue_by_category.png      # generated after running the Python file
└── ratings_by_category.png      # generated after running the Python file
```

## How to Run

From the Week 3 folder:

```bash
pip install pandas matplotlib seaborn
python Python/week3_python_data_wrangling.py
```

The script cleans the dataset, prints the results, saves the cleaned CSV, and generates two charts.

> Note: The Week 3 PDF specifies a Google Drive dataset link, but the dataset contents were not included in the uploaded PDF. This practical uses the sales dataset already used in the Week 2 work as a consistent practice dataset.
