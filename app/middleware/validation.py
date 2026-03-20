from fastapi import Request, HTTPException
import starlette.status as status

MAX_PAYLOAD_SIZE = 1024 * 50  # 50KB limit for event ingestion

async def validate_payload_size(request: Request):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_PAYLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Payload too large. Maximum size allowed is {MAX_PAYLOAD_SIZE} bytes."
        )
