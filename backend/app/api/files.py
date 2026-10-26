from fastapi import APIRouter, File, UploadFile
import os
from pathlib import Path
from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, UPLOAD_DIR
from app.common.exceptions import BussinessException
import time
import uuid
import shutil
from app.common.response import Response


router = APIRouter(prefix="/files", tags=["文件管理"])

@router.post("/upload")
def upload(file: UploadFile = File(...)):
  """文件上传的接口"""
  if not file.filename:
    raise BussinessException(message="文件名不能为空")

  # 原始的文件名 用户头像.jpg
  orignal_name = os.path.basename(file.filename)
  # 文件后缀 .jpg
  ext = Path(orignal_name).suffix.lower()
  if ext not in ALLOWED_EXTENSIONS:
    raise BussinessException(
      message=f"文件不能超过{MAX_FILE_SIZE // 1024 // 1024}MB"
    )
  #设置唯一的文件名称 199323312_dasaasaxc.jpg
  disk_name = f"{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}{ext}"
  # 文件实际存储的路径
  save_path = UPLOAD_DIR / disk_name

  #流式写文件
  with open(save_path, "wb") as f:
    shutil.copyfileobj(file.file, f)

  return Response.sucess(
    data={
      "original_name": orignal_name,
      "disk_name": disk_name,
      "zie": file.size,
      "url": f"/uploads/{disk_name}"
    }
  )
