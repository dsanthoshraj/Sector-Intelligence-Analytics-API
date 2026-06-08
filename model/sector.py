from pydantic import BaseModel, Field, ConfigDict, field_validator, field_serializer
from datetime import datetime
from bson import ObjectId
from typing import Optional
from dateutil import parser as date_parser

class Sector(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: Optional[str] = Field(alias="_id", default=None)
    end_year: Optional[datetime] = None
    intensity: Optional[int] = None
    sector: Optional[str] = None
    topic: Optional[str] = None
    insight: Optional[str] = None
    url: Optional[str] = None
    region: Optional[str] = None
    start_year: Optional[datetime] = None
    impact: Optional[str] = None
    added: Optional[datetime] = None
    published: Optional[datetime] = None
    country: Optional[str] = None
    relevance: Optional[int] = None
    pestle: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    likelihood: Optional[int] = None

    @field_validator('end_year', 'start_year', 'added', 'published', mode='before')
    @classmethod
    def parse_datetime(cls, v):
        if v is None or v == '':
            return None
        if isinstance(v, datetime):
            return v
        if isinstance(v, str):
            try:
                return date_parser.parse(v)
            except (ValueError, TypeError):
                return None
        return v

    @field_validator('intensity', 'relevance', 'likelihood', mode='before')
    @classmethod
    def parse_int(cls, v):
        if v is None or v == '':
            return None
        if isinstance(v, int):
            return v
        if isinstance(v, str):
            try:
                return int(v)
            except ValueError:
                return None
        return v

    @field_validator('impact', 'insight', 'source', 'title', mode='before')
    @classmethod
    def coerce_string(cls, v):
        if v is None or v == '':
            return None
        if isinstance(v, str):
            return v
        return str(v)

    @field_serializer('id')
    def serialize_id(self, v: Optional[str]) -> Optional[str]:
        return v