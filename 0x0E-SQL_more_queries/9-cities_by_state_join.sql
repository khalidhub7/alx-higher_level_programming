-- lists all cities with some requiremetns
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = cities.state_id;
