from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password, hash_password
from app.utils.jwt import create_access_token
from app.common.exceptions import BussinessException
from app.schemas.auth import LoginResponse, RegisterRequest

def login(data: LoginRequest, db: Session):
    """
    用户登录
    """
    # 根据用户账号查询数据库
    user = db.query(User).filter(User.username == data.username).first()

    # 验证用户是否存在和密码是否正确
    if not user:
        raise BussinessException(message="用户不存在")
    if not verify_password(data.password, user.password):
        raise BussinessException(message="密码错误")
    # 验证账号状态
    if user.status == 0:
       raise BussinessException(message="账号已禁用")
    # 创建JWT token
    token = create_access_token(user.id)
    # 返回信息
    return LoginResponse(token=token, user=UserResponse.model_validate(user))

def register(data: RegisterRequest, db: Session):
    """
    用户注册
    """
    # 根据用户账号查询数据库
    user = db.query(User).filter(User.username == data.username).first()

    # 验证用户是否存在
    if user:
        raise BussinessException(message="用户已存在")
    # 创建用户
    user_model = User(
        username=data.username,
        password=hash_password(data.password),
        name=data.name or data.username,
        role="student",
        status=1
    )
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    