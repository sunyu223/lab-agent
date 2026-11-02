from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.services import user_service
from app.common.response import Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserUpdateRequest
router = APIRouter(prefix="/user", tags=["用户信息接口"])

@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
  """获取当前登录用户信息"""
  return Response.sucess(data=user_service.get_user_info(current_user))

@router.put("/update")
def update_user_info(data: UserUpdateRequest,
                     current_user: User = Depends(get_current_user), 
                     db: Session = Depends(get_db)
                     ):
  """更新当前登录用户信息"""
  res = user_service.update_user_info(current_user, data, db)
  return Response.sucess(data=res)

