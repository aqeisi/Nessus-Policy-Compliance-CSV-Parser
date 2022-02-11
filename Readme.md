# Nessus Policy Compliance Parser

This simple python script is here to make your life a thousand times easier when it comes to reporting Nessus policy compliance results to your clients!

## Features

 1. Convert Nessus CSV file to a word document which holds each misconfiguration or compliance check in a table of its own.
 2. Filters the data such that only 'Failed' checks will be included in the report (can be modified easily).
 3. Filters data that you do not usually need to include in your reports, such as the "Notes" in the misconfig 'Description' column.

## Usage

```python3 parse-nessus.py -f <full path to CSV file>```

This will create a word document called "demo.docx" which will hold all the information you need.
