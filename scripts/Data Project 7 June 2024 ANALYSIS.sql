-- 'Studio_Ghibli_CLEANED' table contains information about Studio Ghibli films
-- 'Studio_Ghibli_CLEANED2' table contains information about the genres of each film

-- Query to select relevant fields from the 'Movies' table
SELECT Name, Year, Budget, Revenue, Duration
FROM Studio_Ghibli_CLEANED;

-- Joining the 'Movies' table with the 'Genres' table to get genre information for each film
SELECT m.Name, m.Year, m.Budget, m.Revenue, m.Duration, g.Genre
FROM Studio_Ghibli_CLEANED m
JOIN Studio_Ghibli_CLEANED2 g ON m.Name = g.Name;

-- Filtering data using WHERE clause to focus on Studio Ghibli films
SELECT m.Name, m.Year, m.Budget, m.Revenue, m.Duration, g.Genre
FROM Studio_Ghibli_CLEANED m
JOIN Studio_Ghibli_CLEANED2 g ON m.Name = g.Name
WHERE m.Director = 'Hayao Miyazaki';

-- Grouping data by year and calculating average revenue for each year
SELECT Year, AVG(Revenue) AS AvgRevenue
FROM Studio_Ghibli_CLEANED
WHERE Director = 'Hayao Miyazaki'
GROUP BY Year
ORDER BY Year;

-- Grouping data by genre and calculating average revenue for each genre
SELECT g.Genre, AVG(m.Revenue) AS AvgRevenue
FROM Studio_Ghibli_CLEANED m
JOIN Studio_Ghibli_CLEANED2 g ON m.Name = g.Name
WHERE m.Director = 'Hayao Miyazaki'
GROUP BY g.Genre
ORDER BY AvgRevenue DESC;
