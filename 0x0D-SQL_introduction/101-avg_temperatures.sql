-- AVG in hot database
USE hbtn_0c_0;
SELECT city, AVG(value) AS avgg FROM temperatures ORDER BY avgg DESC;
