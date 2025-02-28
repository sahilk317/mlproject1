from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariable:
    # url = 'mongodb+srv://sahil_katariya:DOX2wDm6TLe2tG7U@cluster0.ftyha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    mongodb_url: str = os.getenv("MONGO_DB_URL")

    def validate(self):
        if not self.mongodb_url:
            raise ValueError("MONGO_DB_URL environment variable is not set.")

# Create an instance and validate
env_var = EnvironmentVariable()
env_var.validate()

# Initialize MongoDB client with error handling
try:
    mongo_client = pymongo.MongoClient(env_var.mongodb_url)
    print("MongoDB connection established successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    mongo_client = None  # Set to None if connection fails
