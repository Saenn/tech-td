# Setup
```
pip3 install pipenv
pipenv install
```

# Question 1
Answers are in a folder "question_1" including both basic diagram and description

# Question 2
Executing a program with cli arguments including source filepath and output filename, run:
```
pipenv run python3 -m sanitizer -s input/sample.txt -t result.txt
# -s = source filepath
# -t = target filename, output will be stored in a folder 'output'
```
Alternatively, you can simply execute below command to let the program reads config from './config.yaml':
```
pipenv run python3 -m sanitizer
```
To make the program ready for production, we still have to implement error-handling, logging. Also, If we use Airflow, we will need a Dockerfile and secret for connecting to our source data. Having a unittest would be good in this kind of application so we can assure the trasformation logics.
# Question 3
SQLs for creating tables are in a folder "question_3/bq_sample_data"  
"question_3/find_top_sales.sql" is used to find top 2 sales for each product class
