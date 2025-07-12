import discord
from redbot.core import commands
import aiohttp

class TelegramLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = "7869124655:AAFmZL2HlsCIbxW0CRVm60-8MhclVhmh5YE"
        self.chat_id = "312891098"

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or not message.content:
            return
        text = f"❌ Удалено сообщение от {message.author} в #{message.channel}:\n{message.content}"
        async with aiohttp.ClientSession() as session:
            await session.post(
                f"https://api.telegram.org/bot{self.token}/sendMessage",
                json={"chat_id": self.chat_id, "text": text}
            )

async def setup(bot):
    await bot.add_cog(TelegramLogger(bot))
