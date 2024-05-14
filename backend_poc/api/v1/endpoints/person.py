from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from backend_poc.schema.person_schema import FindPerson, FindPersonResult, Person, UpsertPerson
from backend_poc.schema.base_schema import Blank
from backend_poc.services.person_service import PersonService
from backend_poc.core.container import Container

router = APIRouter(prefix="/person", tags=["person"])

@router.get("")
@inject
async def get_person_list(
    find_query: FindPerson = Depends(),
    service: PersonService = Depends(Provide[Container.person_service])
) -> FindPersonResult:
    return service.get_list(find_query)

@router.get("/{person_id}")
@inject
async def get_person(
    person_id: int,
    service: PersonService = Depends(Provide[Container.person_service])
) -> Person:
    return service.get_by_id(person_id)

@router.put("")
@inject
async def create_person(
    person: UpsertPerson,
    service: PersonService = Depends(Provide[Container.person_service])
) -> Person:
    return service.add(person)

@router.patch("/{person_id}")
@inject
async def edit_person(
    person_id: int,
    person: UpsertPerson,
    service: PersonService = Depends(Provide[Container.person_service])
) -> Person:
    return service.patch(person_id, person)

@router.delete("/{person_id}")
@inject
async def delete_person(
    person_id: int,
    service: PersonService = Depends(Provide[Container.person_service])
):
    return service.remove_by_id(person_id)
