from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter()


@router.get("/{pie_id}")
def get_pie_by_id(pie_id: Annotated[int, Path(ge=1, lt=1_000)]):
    return {
        "pie": {"id": pie_id},
    }
