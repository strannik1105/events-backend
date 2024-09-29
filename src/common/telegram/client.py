from aiogram import Bot
from aiogram.types import BufferedInputFile

from common.config.config import Config


class TelegramClient:
    def __init__(self) -> None:
        config = Config.get_instance()

        self._bot = Bot(token=config.TG_API_TOKEN)
        self._channel_id = config.TG_CHANNEL_ID

    async def publish_message(self, image: bytes, title: str, text: str) -> None:
        text = f"<b>{title}</b>\n{text}"
        img = BufferedInputFile(image, "test") # .from_file("1.png", "test")

        await self._bot.send_photo(self._channel_id, img, caption=text, parse_mode="html")
        