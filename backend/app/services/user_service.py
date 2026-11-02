from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest
from sqlalchemy.orm import Session
from re import X


def get_user_info(user: User ) -> UserResponse:
    return UserResponse.model_validate(user)

def update_user_info(user: User, data: UserUpdateRequest, db: Session) -> UserResponse:
    user_dict = data.model_dump(exclude_unset=True) # 获取非空的字段 
    for field, value in user_dict.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)
    