import mlflow
import os

# Can load from .env
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "password"
os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:8000"
os.environ["MLFLOW_EXPERIMENT_NAME"] = "proj_1"
os.environ["MLFLOW_ARTIFACT_LOCATION"] = "s3://mlflow"

mlflow.set_tracking_uri("http://127.0.0.1:8000")
model = mlflow.pyfunc.load_model(f"models:/ElasticnetWineModel/Staging")
print(model)
