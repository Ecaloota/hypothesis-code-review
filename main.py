from datetime import datetime
from pydantic import BaseModel, validator


class MyPydanticModel(BaseModel):
    """
    A regular Pydantic model with some validators
    to test.
    """

    name: str
    start: datetime
    end: datetime
    action: float

    @validator("start", "end")
    def ensure_has_tzinfo(v):
        """Ensures that the start and end values given are timezone-aware"""
        if v is not None:
            if not hasattr(v, "tzinfo") or v.tzinfo is None:
                raise ValueError("Datetimes must contain timezone information!")
        return v

    @validator("end")
    def ensure_end_after_start(v, values):
        """Ensures that the end time occurs after the start time"""
        if v is not None and values["start"] is not None:
            if v <= values["start"]:
                raise ValueError("End must be later than start!")
        return v
