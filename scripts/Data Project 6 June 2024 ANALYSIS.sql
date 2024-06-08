-- Query to analyze temperature trends over time
SELECT 
    Country,
    Year,
    AVG(Temperature) AS Avg_Temperature
FROM 
    Temperature_Data
GROUP BY 
    Country,
    Year
ORDER BY 
    Country,
    Year;
