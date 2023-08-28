import aiohttp
import asyncio
from urllib.parse import unquote

def get_tasks(session, url, amount):
	tasks = []

	for i in range(amount):
		tasks.append(session.get(url))

	return tasks

class hmfull:

	async def hmtai_async(category, amount = 1):
		result = []
		async with aiohttp.ClientSession() as session:
			tasks = get_tasks(session, f"https://hmtai.hatsunia.cfd/v2/{category}", amount)
			responses = await asyncio.gather(*tasks)

			for response in responses:
				res = await response.json()
				if "message" in res:
					return 0
				else:
					result.append(res['url'])
				print(f"[+] Found {unquote(res['url'])}")

			if result != []:
				return result
			else:
				return 0

	async def nekos_async(category, amount = 1):
		blacklist = ['https://cdn.nekos.life/blowjob/blowjob31.jpg', 'https://cdn.nekos.life/blowjob/blowjob32.jpg', 'https://cdn.nekos.life/lewdkemo/lewd_neko_v2_132.jpg', 'https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1039.gif']
		result = []
		async with aiohttp.ClientSession() as session:
			tasks = get_tasks(session, f"https://nekos.life/api/v2/img/{category}", amount)
			responses = await asyncio.gather(*tasks)

			for response in responses:
				res = await response.json()
				if "msg" in res:
					return 0
				if res['url'] in blacklist:
					continue
				else:
					result.append(res['url'])
				print(f"[+] Found {unquote(res['url'])}")

			if result != []:
				return result
			else:
				return 0

	async def nekobot_async(category, amount = 1):
		blacklist = ['https://i0.nekobot.xyz/0/2/9/1b50d3f619f1bafdf114a530a2570.jpg', 'https://cdn.nekobot.xyz/9/3/9/448bb2ff69b3457a82f32ecd31c06.jpg', 'https://i0.nekobot.xyz/4/9/3/3b6ccf0c081db887fbe38038af996.jpg', 'https://i0.nekobot.xyz/8/6/9/ee21a6ac7d06aabf0b71691e6dfb5.jpg', 'https://cdn.nekobot.xyz/b/4/d/c1fdf4234fbfba326fb282de9ef8c.jpg', 'https://cdn.nekobot.xyz/b/4/d/c1fdf4234fbfba326fb282de9ef8c.jpg']
		result = []
		async with aiohttp.ClientSession() as session:
			tasks = get_tasks(session, f"https://nekobot.xyz/api/image?type={category}", amount)
			responses = await asyncio.gather(*tasks)

			for response in responses:
				res = await response
				if not res.status_code == 200:
					return 0
				if res.json()["success"] == "false":
					return 0
				if res.json()["message"] in blacklist:
					continue
				else:
					result.append(res['message'])
				print(f"[+] Found {unquote(res['message'])}")

			if result != []:
				return result
			else:
				return 0

	
	async def nekolove_async(category, amount = 1):
		result = []
		async with aiohttp.ClientSession() as session:
			tasks = get_tasks(session, f"https://hmtai.hatsunia.cfd/v2/{category}", amount)
			responses = await asyncio.gather(*tasks)

			for response in responses:
				res = await response.json()
				if "message" in res:
					return 0
				else:
					result.append(res['url'])
				print(f"[+] Found {unquote(res['url'])}")

			if result != []:
				return result
			else:
				return 0	
