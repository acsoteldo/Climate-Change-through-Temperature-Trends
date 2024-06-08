-- Query to analyze temperature trends over time
SELECT 
    Country,
    Year,
    AVG(Temperature) AS Avg_Temperature
FROM 
    long_format_annual_surface_temp_CLEANED
GROUP BY 
    Country,
    Year
ORDER BY 
    Country,
    Year;
