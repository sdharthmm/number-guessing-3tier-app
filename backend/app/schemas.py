# schemas.py

# Pydantic BaseModel is used for request/response validation
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict


# This schema defines what client must send when creating score
class ScoreCreate(BaseModel):

    # Player name must be string
    player_name: str

    # Attempts must be integer
    attempts: int


# This schema defines what API will return
class ScoreResponse(BaseModel):
    id: int
    player_name: str
    attempts: int

    model_config = ConfigDict(from_attributes=True)
# Add inside schemas.py

class GuessRequest(BaseModel):
    number: int


class GuessResponse(BaseModel):
    message: str
    attempts: int
    game_over: bool