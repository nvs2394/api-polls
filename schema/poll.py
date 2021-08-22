from pydantic.main import BaseModel


class Poll(BaseModel):
    title: str
    type: str
    created_by: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_at: str
    updated_at: str
