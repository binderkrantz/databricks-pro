# Databricks notebook source
from pyspark.sql import SparkSession
import os

# COMMAND ----------

spark = SparkSession.builder.appName('Practise').getOrCreate()

# COMMAND ----------

cwd=os.getcwd()
print(cwd)
os.listdir('/Workspace/Users/chanbitz@live.dk/')

# COMMAND ----------


dfps = spark.read.csv('file:/Workspace/Repos/chanbitz@live.dk/databricks-pro/datasets/test1.csv')

