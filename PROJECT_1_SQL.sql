--What is the mean visibility of the dataset
SELECT AVG(Visibility_km) AS [Mean visibility] FROM [1. Weather Data] 

--Find the number of records where the wind speed is greater than 24km/hr and visibility is equal to 25km
SELECT * FROM [1. Weather Data]
WHERE Wind_Speed_km_h > 24 AND Visibility_km = 25

--What is the mean value of each column for each weather condition?
SELECT AVG(Weather) FROM [1. Weather Data]
GROUP BY COUNT(Weather)
 
--Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40
SELECT * FROM [1. Weather Data]
WHERE Weather = 'Clear' AND Rel_Hum >= 50 OR  Visibility_km >= 40

--Find the number of weather conditions that include snow.
SELECT COUNT(Weather)
FROM  [1. Weather Data]
WHERE weather = 'Snow'