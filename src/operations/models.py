from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, Text, ForeignKey

from src.auth.models import user
from src.database import metadata

post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("text", Text),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)