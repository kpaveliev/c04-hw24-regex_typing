# SkyPro.Python course
## Homework 23. Functional programming

**Description**

Flask web-server available at http://127.0.0.1:5000/perform_query/
which could perform queries on the file kept in 'data' folder

To perform a query you should pass filename, command name and command value in a request

Only two commands at a time could be passed (no more, no less)

**Commands available**

1. filter - get lines which contain string passed
2. map - get data from the passed column only
3. unique - get unique data only
4. sort - sort data in ascending or descending order
5. limit - limit lines to the passed number

**Request examples**

Commands could be passed as a json in POST-request or as request parameters

Option 1 Example:
{
    "file_name": "apache_logs.txt",
    "cmd1": "filter",
    "value1": "get",
    "cmd2": "limit",
    "value2": 5
}

Option 2 Example:
http://127.0.0.1:5000/perform_query/?cmd1=filter&value1=GET&cmd2=limit&value2=2


Kirill Paveliev\
July 2022