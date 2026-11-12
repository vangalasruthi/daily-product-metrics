\# Data Dictionary



\## Input: Transaction Events



Each event contains a complete transaction snapshot.

All fields below are required and cannot be null.



| Field | Type | Meaning / Validation |

|---|---|---|

| event\_id | string | Non-empty unique source event identifier |

| transaction\_id | string | Non-empty business transaction identifier |

| version | integer | Positive transaction version; higher version wins |

| product\_id | string | Must exist in the products reference data |

| business\_date | string | Valid date in YYYY-MM-DD format |

| quantity | integer | Greater than zero |

| amount\_minor | integer | Total transaction amount in paise; zero or greater |

| currency | string | INR only |

| status | string | Either active or reversed |

| source\_updated\_at | string | ISO-8601 timestamp with timezone |

| schema\_version | integer | Must be 1 |



\## Business Rules



\- One transaction represents one product purchase line.

\- amount\_minor is the total line amount, not the unit price.

\- Each event is a full replacement snapshot, not a partial update.

\- Higher versions replace the current transaction snapshot.

\- Lower versions are preserved in history without changing current state.

\- Identical event replays do not change business output.

\- Conflicting content for the same event\_id is rejected.

\- Conflicting content for the same transaction\_id and version is rejected.

\- Reversed transactions contribute zero to all sales metrics.

\- Reversals remove sales from the original business date.

\- A higher-version active snapshot can reinstate a reversed transaction.



\## Products Reference



| Field | Type | Rule |

|---|---|---|

| product\_id | string | Primary key; non-empty |

| product\_name | string | Non-empty |



\## Output: Daily Product Metrics



One row per business\_date and product\_id.



| Field | Type | Meaning |

|---|---|---|

| business\_date | string | Sales date in YYYY-MM-DD format |

| product\_id | string | Valid product identifier |

| active\_transaction\_count | integer | Number of active transactions |

| units\_sold | integer | Sum of active transaction quantities |

| sales\_amount\_minor | integer | Sum of active transaction amounts in paise |



Primary key: (business\_date, product\_id)



Groups with no active transactions are omitted.



\## Ingestion Lineage



These fields are added by the pipeline, not supplied in input events:



\- run\_id: Identifier for an execution attempt.

\- source\_file: Input file name.

\- source\_line\_number: Original line number in the input file.



Rejected records retain their raw input, lineage, and rejection reason.

