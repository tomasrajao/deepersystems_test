from datetime import datetime

from bson import  ObjectId
from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    id: Optional[str] = None
    user: str
    password: str
    is_user_admin: bool
    is_user_manager: bool
    is_user_tester: bool
    user_timezone: str
    is_user_active: bool = True
    created_at: datetime = datetime.now()
    
    def parse_roles(self):
        roles = []
        if self.is_user_admin:
            roles.append('admin')
        if self.is_user_manager:
            roles.append('manager')
        if self.is_user_tester:
            roles.append('tester')
        return roles
 
    def to_mongo(self):
        return {
            "_id": ObjectId(self.id) if self.id else ObjectId(),
            "username": self.user,
            "password": self.password,
            "roles": self.parse_roles(),
            "preferences": self.user_timezone,
            "active": self.is_user_active,
            "created_ts": self.created_at,
        }
