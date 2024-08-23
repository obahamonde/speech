from typing import Literal, Optional, TypeAlias

from pydantic import BaseModel, Field, computed_field
from typing_extensions import Literal

SpeakerName: TypeAlias = Literal[
    "Claribel Dervla",
    "Daisy Studious",
    "Gracie Wise",
    "Tammie Ema",
    "Alison Dietlinde",
    "Ana Florence",
    "Annmarie Nele",
    "Asya Anara",
    "Brenda Stern",
    "Gitta Nikolina",
    "Henriette Usha",
    "Sofia Hellen",
    "Tammy Grit",
    "Tanja Adelina",
    "Vjollca Johnnie",
    "Andrew Chipper",
    "Badr Odhiambo",
    "Dionisio Schuyler",
    "Royston Min",
    "Viktor Eka",
    "Abrahan Mack",
    "Adde Michal",
    "Baldur Sanjin",
    "Craig Gutsy",
    "Damien Black",
    "Gilberto Mathias",
    "Ilkin Urbano",
    "Kazuhiko Atallah",
    "Ludvig Milivoj",
    "Suad Qasim",
    "Torcull Diarmuid",
    "Viktor Menelaos",
    "Zacharie Aimilios",
    "Nova Hogarth",
    "Maja Ruoho",
    "Uta Obando",
    "Lidiya Szekeres",
    "Chandra MacFarland",
    "Szofi Granger",
    "Camilla Holmström",
    "Lilya Stainthorpe",
    "Zofija Kendrick",
    "Narelle Moon",
    "Barbora MacLean",
    "Alexandra Hisakawa",
    "Alma María",
    "Rosemary Okafor",
    "Ige Behringer",
    "Filip Traverse",
    "Damjan Chapman",
    "Wulf Carlevaro",
    "Aaron Dreschner",
    "Kumar Dahl",
    "Eugenio Mataracı",
    "Ferran Simen",
    "Xavier Hayasaka",
    "Luis Moray",
    "Marcos Rudaski",
]
SpeakerLanguage: TypeAlias = Literal["en", "es"]
AudioFormat: TypeAlias = Literal["mp3", "wav", "ogg", "flac"]
SpeakerEmotion: TypeAlias = Literal[
    "cheerful",
    "excited",
    "neutral",
    "happy",
    "sad",
    "angry",
    "fearful",
    "disgusted",
    "surprised",
]


class SpeechRequest(BaseModel):
    model: Literal["xtts"] = Field(
        default="xtts", description="The speech synthesis model to use."
    )
    input: str = Field(..., description="The text to convert to speech.")
    voice: SpeakerName = Field(
        default="Nova Hogarth", description="The voice to use for the speech."
    )
    voice_id: Optional[str] = Field(
        default=None, description="The custom voice to use for the speech."
    )
    response_format: AudioFormat = Field(
        default="mp3", description="The desired format for the speech output."
    )
    speed: float = Field(
        default=1.0,
        ge=0.25,
        le=4.0,
        description="The speed of the generated speech (0.25x to 4.0x).",
    )
    language: SpeakerLanguage = Field(
        default="en", description="The language of the input text."
    )
    emotion: SpeakerEmotion = Field(
        default="cheerful", description="The emotion of the speaker."
    )

    @computed_field
    @property
    def speaker(self) -> str:
        return self.voice_id or self.voice
