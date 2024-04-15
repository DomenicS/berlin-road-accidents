# project_berlin-road-accident

## Final Tableau Dashboard / Vizualization

- https://public.tableau.com/app/profile/domenic4547/viz/BerlinRoadAccidents-Draft/VIZ 

## Project Structure

- **01_accident_data.ipynb**: Contains the workflow for loading, cleaning, preparing data for further usage on tableau and SQL.

- **01_population_data.ipynb**: Details the procedures for processing the population data, including data transformation and export for further analysis.

## Key Procedures

- **Data Cleaning**: Involves handling missing values and formatting data to ensure consistency across the datasets.
- **Pre-processing of Geospatial Data in Python**: To enhance performance in Tableau, geospatial data joins and transformations were performed in Python. This step ensures that the data is already geographically structured and optimized for fast loading and analysis in Tableau
- **Data Export**: Includes storing the cleaned and transformed data into a SQL database and exporting to CSV files for use in applications such as Tableau.


## Datasets Used

- Berlin road accident data - https://unfallatlas.statistikportal.de/?BL=BE
    - statistische Ämter des Bundes und der Länder

- Berlin population data - https://www.statistik-berlin-brandenburg.de/a-i-16-hj
    - Amt für Statistik Berlin Brandenburg / [A | 16 - hj 2/22]

- Berlin geographical data - https://daten.odis-berlin.de/ 
    - "Geoportal Berlin / [lor_bezirksregionen_2021]
    - "Geoportal Berlin / [lor_ortsteile]
    - "Geoportal Berlin / [lor_planungsraeume_2021]
    - "Geoportal Berlin / [lor_prognoseraume_2021]
    - "Geoportal Berlin / [Detailnetz-Strassenabschnitte]
    - "Geoportal Berlin / [Strassenflaechen]

## License
This project is licensed under the Creative Commons Attribution 3.0 Germany (CC BY 3.0 DE) License. For more details, please visit [Creative Commons CC BY 3.0 DE License](https://creativecommons.org/licenses/by/3.0/de/).
