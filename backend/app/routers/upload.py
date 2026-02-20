from fastapi import APIRouter, UploadFile
from ..services.parsers import UnicredParser, PicpayParser, BanrisulParser
from ..services.file_handler import save_file_error

router = APIRouter(
    prefix="/upload_file",
    tags=["Upload File"]
)

@router.post("/unicred")
async def upload_unicred(file: UploadFile):
    try:
        result = UnicredParser()
        result.parser(file)
    except Exception as e:
        save_file_error(file, e, date)

@router.post("/picpay")
async def upload_picpay(file: UploadFile):
    pass

@router.post("/banrisul")
async def upload_banrisul():
    pass