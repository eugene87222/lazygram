# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import logging
import sys


class LazyGram(ABC):
    def __init__(self, token):
        self.bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dispatcher = Dispatcher()
        self.router = Router()

    @abstractmethod
    def register_handler(self):
        pass

    async def run(self):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)        
        self.register_handler()
        self.dispatcher.include_router(self.router)
        await self.dispatcher.start_polling(self.bot)
