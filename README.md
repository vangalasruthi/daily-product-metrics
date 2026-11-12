!\[CI](https://github.com/vangalasruthi/daily-product-metrics/actions/workflows/ci.yml/badge.svg)



\# Daily Product Metrics Pipeline



Python-based ETL pipeline that processes retail sales transactions and generates daily product-level metrics with automated tests.



\## Overview



This project reads raw sales transaction data, calculates product-level metrics, and outputs a clean CSV file for reporting.



\## Business Impact



This pipeline helps retail teams track daily sales performance at the product level. By automating metric calculation and validation, it reduces manual reporting effort and provides reliable daily insights for inventory and sales decisions.



\## Features



\- Reads JSONL transaction files

\- Calculates active transaction count, units sold, and sales amount

\- Generates daily product metrics CSV

\- Automated tests with pytest

\- CI workflow with GitHub Actions



\## Project Structure



\- `src/` - source code

\- `tests/` - test files

\- `data/` - input and output files

\- `docs/` - documentation

\- `.github/workflows/` - CI workflow



\## How to Run



1\. Install dependencies:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



2\. Run the pipeline:

&#x20;  ```bash

&#x20;  python src/daily\_metrics.py

&#x20;  ```



3\. Run tests:

&#x20;  ```bash

&#x20;  python -m pytest -q

&#x20;  ```



\## Tech Stack



\- Python

\- pandas

\- pytest

\- GitHub Actions

