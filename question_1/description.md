Q1: Design the high-level daily-batch data ingestion pipeline
A1: Here's a simple pipeline for our ETL process:
  - MongoDB as our data source
  - Workflow management system eg, Airflow. The system is used to schedule/monitor/maintain our batch jobs
  - Batch jobs ingest raw data to GCS
  - Transform and ingest data from GCS to BigQuery which we could go with Cloud function or Dataflow depending each use-case (Serving layer 1)
  - Then, we transform, clean, etc. our data in BigQuery and ingest to another BigQuery project/layer (Serving layer 2)

Q2: Share your thought on how should the data on the serving layer look like?
A2: Serving layer 1 is for DE/DS. The layer can still contain semi-structure data for flexibility. Serving layer 2 is for users with basic knowledge of SQL. The data in this layer is already transformed, cleaned, normalized, etc. in order to make it easy and simple for our business users. Additionally, we can group our data by business domains or use-cases to make it more cool...

Q3: On top of 1., 2., please extend your idea by showing us how the ideal Data Platform(in your opinion) should be
A3: On top of this, we have to make sure that everything is going fine and our data supports our friends well. We could add more layers like visualization layer, AI layer, notification layer, data quality layer, etc. It would be good to know that all of our data in our system is always used by someone.