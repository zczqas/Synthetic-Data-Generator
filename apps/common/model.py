from sqlalchemy import (
    Column,
    BigInteger,
    Boolean,
    func,
    DateTime,
)


class TimeStampMixin:
    """Timestamping mixin"""

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
