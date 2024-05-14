from dependency_injector import containers, providers

from backend_poc.core.config import configs
from backend_poc.core.database import Database
from backend_poc.repository import *
from backend_poc.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "backend_poc.api.v1.endpoints.person"
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    person_repository = providers.Factory(PersonRepository, session_factory=db.provided.session)

    person_service = providers.Factory(PersonService, person_repository=person_repository)