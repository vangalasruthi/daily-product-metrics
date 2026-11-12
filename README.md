\# Daily Product Metrics Pipeline



\## Objective

Maintain daily product sales metrics from incremental transaction events.

Handle updates, reversals, late events, and safe reruns.



\## Technology

\- Python

\- SQLite

\- pytest



\## Business Rules

\- Each event contains a complete transaction snapshot.

\- Higher transaction versions replace older versions.

\- Duplicate events must not change sales totals.

\- Reversed transactions contribute zero sales.

\- Late events update the affected historical dates.

\- Currency is INR; amounts are stored in paise.



\## Output

Daily metrics for each product:

\- Active transaction count

\- Units sold

\- Sales amount



\## Sample Data

\- data/input/products.csv

\- data/input/batch\_001.jsonl

\- data/input/batch\_002.jsonl



\## Expected Results

After batch 1: 2 active transactions, 2 units, INR 150.

After batch 1 followed by batch 2: 1 active transaction, 1 unit, INR 120.



\## Project Status

Initial documentation and sample files have been created.

Pipeline implementation and automated tests are not yet complete.

Setup and run instructions will be added after verification.

