import os
import sys

# Tell PySpark to use the current active Python executable
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("FirstSparkApplication") \
    .master("local[*]") \
    .getOrCreate()

# Sample dataset
data = [(1, "Tejas"), (2, "Rahul"), (3, "Amit")]

# Create and display DataFrame
df = spark.createDataFrame(data, ["id", "name"])
df.show()

# Stop Spark Session
spark.stop()