include .env

start:
	mlflow ui --default-artifact-root s3://mlflow/ -p 8000