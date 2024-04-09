from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class BaseResponseSchema(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
