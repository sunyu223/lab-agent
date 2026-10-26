import bcrypt

def hash_password(password: str) -> str:
    """对密码进行哈希加密处理"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    """验证密码是否正确"""
    """ “123”->"xsguaoshochh" """
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"), hashed_password.encode("utf-8")
        )
    except ValueError:
        return False