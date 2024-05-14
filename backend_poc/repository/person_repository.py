from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from backend_poc.model.person import Person
from backend_poc.repository.base_repository import BaseRepository


class PersonRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Person)