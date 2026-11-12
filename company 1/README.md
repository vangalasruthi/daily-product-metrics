\# Daily Product Metrics Pipeline



\## Objective

Maintain daily product sales metrics from incremental transaction events.



\## Technology

\- Python

\- SQLite

\- pytest



\## Planned Business Rules

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

