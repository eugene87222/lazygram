# lazygram

A wrapper of aiogram because I am lazy.

## Requirements

Python 3.10+

## Installation

```bash
git clone https://github.com/eugene87222/lazygram.git
cd lazygram
./setup.sh
```

### To Upgrade

```bash
cd lazygram
git pull
./setup.sh
```

## Usage

```python
from aiogram.filters import Command
import asyncio
from lazygram import LazyGram


class MyBot(LazyGram):
    def __init__(self, token):
        super().__init__(token)

    async def welcome(self, message: Message):
        await message.answer('Hi!')

    def register_handler(self):
        self.router.message.register(self.welcome, Command('start'))


if __name__ == '__main__':
    bot = MyBot('<bot token>')
    asyncio.run(bot.run())

```