from pyrogram import Client
from pyrogram.errors import RPCError
import asyncio

"""
一个TGbot初始化小脚本
"""


async def main():
    api_id = str(input("Please enter your api_id:"))
    api_hash = str(input("Please enter your api_hash:"))
    bot_token = str(input("Please enter your bot_token:"))
    proxy_addr = str(input("Please enter your proxy_address(socks5):"))
    proxy_port = int(input("Please enter your proxy_port:"))
    master = str(input("Please enter your username:"))
    proxies = {
        "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
        "hostname": proxy_addr,
        "port": proxy_port
    }
    print("Your api_id is: ", api_id)
    print("Your api_hash is: ", api_hash)
    print("Your bot_token is: ", bot_token)
    if not (len(str(api_id)) and len(api_hash) and len(bot_token) and len(proxy_addr)):
        print("Please enter agian!")
    else:
        print("Starting client...")
        try:
            async with Client("my_bot", proxy=proxies, api_id=api_id, api_hash=api_hash,
                              bot_token=bot_token) as app:
                await app.send_message(master, "嗨, 我在正常工作哦！")
        except RPCError as r:
            print(r)

from pyrogram import Client

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token, ipv6=True
)

app.run()
asyncio.run(main())
