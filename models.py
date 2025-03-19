from pydantic.dataclasses import dataclass
from datetime import datetime


@dataclass
class UserPreferences:
	timezone: str
 

@dataclass
class User:
	_id: int
	username: str
	password: str
	roles: list
	preferences: UserPreferences
	active: bool
	created_ts: datetime = datetime.now()
 