from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import os
import shutil

from app.services.ingestion_service import (
    IngestionService
)

router = APIRouter()


@router.post("/upload")

async def upload_document(
    file: UploadFile = File(...)
):
    # Create uploads directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    # Read uploaded file
    contents = await file.read()

     #Write file safely
    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    result = (
        IngestionService.process_document(file_path)
    )

    return {
        "message": "Document processed",
        "chunks": result["chunks"]
    }