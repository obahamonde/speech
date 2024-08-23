from fastapi import Body, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from .schema import SpeechRequest
from .worker import XTTS

xtts = XTTS.from_pretrained()


def create_app() -> FastAPI:
    app = FastAPI(
        tags=["Speech"],
        title="Speech Synthesis API",
        description="OpenAI compliant API for speech synthesis.",
        version="0.0.1",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post(
        "/api/v1/audio/speech",
        response_class=StreamingResponse,
        status_code=status.HTTP_200_OK,
    )
    async def _(body: SpeechRequest = Body(...)):
        try:
            return await xtts.handler(body=body)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error: {e.__class__.__name__} => {e}",
            ) from e

    return app
