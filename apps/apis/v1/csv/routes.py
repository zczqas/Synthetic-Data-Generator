from typing import Optional

from urllib.parse import quote

from fastapi import (
    APIRouter,
    HTTPException,
    status,
)
from fastapi.responses import FileResponse

from apps.apis.v1.csv.helpers import (
    generate_csv,
)


router = APIRouter(prefix="/csv", tags=["CSV"])


@router.get("/prompt")
def get_csv_prompt(
    category: Optional[str] = None,
):
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a category for csv generation",
        )

    try:
        filename = generate_csv(category)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e

    if filename is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to generate CSV file for category: {category}",
        )

    filename_bytes = filename.encode("utf-8")
    quoted_name = quote(filename_bytes)

    return FileResponse(quoted_name, media_type="text/csv", filename=filename or "")
