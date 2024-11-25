# QA Training

Project was ETL Database Transformation, I wanted to make and validate an ETL between two SQLite databases.  

User Story/Test Cases:

This project implements and validates an ETL (Extract, Transform, Load) process using SQLite databases. The script extracts user data from database_1, transforms it based upon specific rules 
(excluding the user Tom, converting names to uppercase, adding 10 years to each age, and adding a new user JOHN with age 44), and loads the transformed data into database_2. To validate the
process, test.py ensures that Tom is excluded, JOHN is included, and the transformation is correctly applied. Run main.py to perform the ETL operation and test.py to confirm success, 
indicated by the output TEST SUCCEEDED!. This demonstrates a simple yet effective pipeline for data migration and transformation using Python and SQLite.

For the portion of the work done with the Selenium IDE and the website(https://weathershopper.pythonanywhere.com/), the tests were run with the Selenium IDE and the log showed that the tests showed all the 
commands worked properly and yielded the result of having the payment go through correctly at the end of it. The qa-training_learn_selenium.side file shows what was saved from the Selenium IDE.  



# Data Analyst Projects

Movie project was created to allow an individual to enter in their username and movies list, select movies to watch, view upcoming movies, and then be able to view the watched movies. This was done using two 
python files movieapp.py and moviedatabase.py with SQLite. 

Power BI project done on space missions data from 1957 to 2022. Rocket launch data, mission success rate, countries with most successful missions, most used rockets, and patterns with launch locations explored.
(can view Power BI project here:   https://app.powerbi.com/view?r=eyJrIjoiNmVmY2FlMzQtOThkNi00NTUzLThkZDAtNzQ4NjljNWY2NzkxIiwidCI6IjM4NzI4YTE3LTk3MDctNGY0OS04YzliLTI3OWMxYTQwMzhjMSIsImMiOjN9)

Other files for jupyter notebook projects for Covid and FIFA were done as EDA(Exploratory Data Analysis) primarily.


  
