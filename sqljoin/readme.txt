
Problem:

Implement a relational join as a MapReduce query

Consider the following query:

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
Your MapReduce query should produce the same result as this SQL query executed against an appropriate database.

---------------------------------------------------------

Dataset 
 - Json file with two input tables, Order and LineItem, as one big concatenated bag of records.
---------------------------------------------------------

System information:
 - CentOS - 6.5
 - Hadoop - 2.4
---------------------------------------------------------

Run code
 - #sh run.sh 

