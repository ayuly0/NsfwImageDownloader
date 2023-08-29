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

	async def nekosfun_async(category, amount = 1):
		result = []
		async with aiohttp.ClientSession() as session:
			tasks = get_tasks(session, f"http://api.nekos.fun:8080/api/{category}", amount)
			responses = await asyncio.gather(*tasks)

			for response in responses:
				res = await response.json()
				result.append(res['image'])
				print(f"[+] Found {unquote(res['image'])}")

			if result != []:
				return result
			else:
				return 0
	
