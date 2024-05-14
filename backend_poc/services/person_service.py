from backend_poc.repository.person_repository import PersonRepository
from backend_poc.services.base_service import BaseService


class PersonService(BaseService):
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository
        super().__init__(person_repository)