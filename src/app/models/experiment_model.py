from typing import Optional

from sqlmodel import Field, SQLModel


class Experiment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    experiment_name: str
    experiment_description: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
