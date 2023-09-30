import os

DATABASE_DIRECTORY = "sqlite+aiosqlite:///./db.db"

MINIO_ACCESS_KEY = os.getenv("MINIO_SERVER_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SERVER_SECRET_KEY")

EVACUATE_BUCKET_NAME = "evacuate_us"
MINIO_URL = "minio:9000"
