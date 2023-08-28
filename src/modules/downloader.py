import os
import uuid
import hmtai
import requests
import asyncio
import aiohttp
import async_timeout
import concurrent.futures
from tqdm import trange
from urllib.parse import urlparse, unquote
from multiprocessing.pool import ThreadPool
from .sources_cagetory import SourcesCagetory

class Downloader:
	def __init__(self):
		self.h3ntai_links = []
		self.sem = asyncio.Semaphore(2)

	def get_link(self, source: str, cagetory: str) -> None:
		link = ''

		with concurrent.futures.ThreadPoolExecutor() as executor:
			future = executor.submit(hmtai.get, source, cagetory)
			link = future.result()

		self.h3ntai_links.append(link)

	def get_image_links(self, source: str, cagetory: str, amount: int = 50) -> None:
		self.h3ntai_links = []
	  
		for i in range(amount):
			self.get_link(source, cagetory)

	# Download Functions

	def download_file(self, url: str, save_path: str) -> None:
		try:

			res = requests.get(url)
	
			with open(save_path, 'wb') as f:
				for chunk in res.iter_content(chunk_size = 1024):
					if not chunk:
						continue
					f.write(chunk)

		except Exception as ex:
			print("Exception in download_file()", ex)

	async def download_url_async(self, url, session, source, cagetory) -> str:
		size = self.get_lenght_file_url(url)
		ext = self.get_ext_from_url(url)
		file_name = f"image/{self.source_filter(source, cagetory)}/{cagetory}/{uuid.uuid4().hex}{ext}"
		print(f"[+] Downloading {url}")
		async with async_timeout.timeout(240):
			async with session.get(url) as response:
				with open(file_name, "wb") as fd:
					async for data in response.content.iter_chunked(1024):
						fd.write(data)
		return '[+] Successfully downloaded ' + file_name + f" [{self.format_size(size, 'mb')}]"

	# Download Mode

	async def download_async(self, source: str, cagetory: str, amount: int = 50):
		print("[+] Starting get links...")
		self.get_image_links(source, cagetory, amount)

		async with aiohttp.ClientSession() as session:
			tasks = [self.download_url_async(url, session, source, cagetory) for url in self.h3ntai_links]
			return await asyncio.gather(*tasks)

	def download_while_get_link(self, source: str, cagetory: str, amount: int = 50) -> None:
		with trange(amount, postfix = [{'value': 0}], bar_format = "{percentage:.0f}%|{bar}| {postfix[0][value]}/{total} {desc}") as t:
			for i in t:
				with concurrent.futures.ThreadPoolExecutor() as executor:
					link = hmtai.get(source, cagetory)
					extension = self.get_ext_from_url(link)
					dir_name = os.path.dirname(save_path)
					_, file_name = os.path.split(save_path)

					t.set_description(f'Found {link}')

					save_path_new = f'{dir_name}/{file_name}-{uuid.uuid4().hex}{extension}'

					t.set_description(f'Starting download...')

					executor.submit(self.download_file, link, save_path_new)

					t.set_description(f'{save_path_new}')
					t.postfix[0]["value"] = i + 1
					t.update()

	# Utils
	def get_ext_from_url(self, url) -> str:
		url = unquote(url)
		url = urlparse(url).path
		_, ext = os.path.splitext(os.path.basename(url))

		return ext

	def get_lenght_file_url(self, url):
		res = requests.head(url, allow_redirects=True)
		size = int(res.headers.get("content-length", -1))
		return size

	def format_size(self, size, unit = "kb"):
		exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
		size = size / 1024 ** exponents_map[unit]
		return f"{round(size, 2)} {unit.upper()}"

	def source_filter(self, source, cagetory):
		sources_cagetory = SourcesCagetory()

		if source == "hmtai":
			if cagetory in sources_cagetory.hmtai_sfw():
				return "hmtai-sfw"
			elif cagetory in sources_cagetory.hmtai_nsfw():
				return "hmtai-nsfw"

		elif source == "nekos":
			if cagetory in sources_cagetory.nekos_sfw():
				return "nekos-sfw"
			elif cagetory in sources_cagetory.nekos_nsfw():
				return "nekos-nsfw"
		elif source == "nekobot":
			if cagetory in sources_cagetory.neko_bot_sfw():
				return "neko-bot-sfw"
			elif cagetory in sources_cagetory.neko_bot_nsfw():
				return "neko-bot-nsfw"
		elif source == "neko-love":
			if cagetory in sources_cagetory.neko_love_sfw():
				return "neko-love-sfw"
			elif cagetory in sources_cagetory.neko_love_nsfw():
				return "neko-love-nsfw"



	
