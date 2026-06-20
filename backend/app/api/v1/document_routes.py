from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)

import os
import shutil

from app.services.ingestion_service import (
    IngestionService
)

router = APIRouter()


@router.post("/upload")

async def upload_document(
    file: UploadFile = File(...),
    allowed_roles: str = Form("admin")
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
        IngestionService.process_document(
            file_path,
            allowed_roles=[
                role.strip().lower()
                for role in allowed_roles.split(",")
                if role.strip()
            ]
        )
    )

    return {
        "message": "Document processed",
        "chunks": result["chunks"]
    }
