from dependency_injector import containers, providers
from starlette.templating import Jinja2Templates

from evacuate_us.database import Database
from evacuate_us.storage import create_minio_client
from evacuate_us.config import (
    MINIO_SECRET_KEY,
    MINIO_ACCESS_KEY,
    MINIO_URL,
    EVACUATE_BUCKET_NAME,
    DATABASE_DIRECTORY,
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["evacuate_us.routers", "evacuate_us.services"]
    )

    db = providers.Singleton(Database, db_url=DATABASE_DIRECTORY)

    minio_client = providers.Singleton(
        create_minio_client,
        minio_url=MINIO_URL,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        bucket_name=EVACUATE_BUCKET_NAME,
    )

    templates = providers.Singleton(Jinja2Templates, directory="evacuate_us/templates")
