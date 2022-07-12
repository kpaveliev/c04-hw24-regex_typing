# SkyPro.Python course
## Homework 24. Functional programming

**Description**

Flask web-server available at http://127.0.0.1:5000/perform_query/
which could perform queries on the file kept in 'data' folder

To perform a query you should pass filename, command name and command value in a request

Only two commands at a time could be passed (no more, no less)

**Commands available**

1. regex - filter data with regular expression passed
2. map - get data from the passed column only (update: lines are split using regular expressions)
3. filter - get lines which contain string passed
4. unique - get unique data only
5. sort - sort data in ascending or descending order
6. limit - limit lines to the passed number

**Request examples**

Commands could be passed in request parameters

Example:
http://127.0.0.1:5000/perform_query/?cmd1=filter&value1=GET&cmd2=limit&value2=2


Kirill Paveliev\
July 2022