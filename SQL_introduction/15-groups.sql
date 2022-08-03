-- list the number of the records
SELECT score, COUNT(score) AS NUMBER FROM second_table GROUP BY score ORDER BY score DESC;
