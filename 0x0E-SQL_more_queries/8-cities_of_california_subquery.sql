-- lists all cities of California
-- (mn task 8 lfoo9 we working in 2 tables)
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT states.id FROM states
	WHERE states.name = 'California'
);
