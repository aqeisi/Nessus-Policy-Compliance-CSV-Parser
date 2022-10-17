# Nessus Policy Compliance Parser

This simple python script is here to make your life a thousand times easier when it comes to reporting Nessus policy compliance results to your clients!

## Features

 1. Convert Nessus CSV file to a word document which holds each misconfiguration or compliance check in a table of its own.
 2. Filters the data such that only 'Failed' checks will be included in the report (can be modified easily).
 3. Filters data that you do not usually need to include in your reports, such as the "Notes" in the misconfig 'Description' column.
 4. Most importantly, this will **sort the data by misconfig** and not by host, this means that each misconfig will only be included in a single table (multiple IPs), which will make your reports much shorter.

## Usage

1. Sort the CSV file by Description and save it
2. Run the script

```python3 parse-nessus.py -f <full path to CSV-file>```

This will create a word document called "demo.docx" which will hold all the information you need.
