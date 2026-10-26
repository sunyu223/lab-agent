from pydantic import BaseModel

class FileResponse(BaseModel):
  '''文件上传返回'''
  original_name: str
  disk_name: str
  size: int
  url: str