__import__('sys').path.append('../')

import os
import uuid
from lib import hmtai
import requests
import asyncio
import aiohttp
import async_timeout
from urllib.parse import urlparse, unquote
from .sources_category import SourcesCategory

class Downloader:
	def __init__(self):
		self.h3ntai_links = []

	async def get_image_links(self, source: str, category: str, amount: int = 50) -> None:	
		self.h3ntai_links = await hmtai.get(source, category, amount)

	# Download Functions

	async def download_url_async(self, url, session, source, category) -> str:
		size = self.get_lenght_file_url(url)
		ext = self.get_ext_from_url(url)
		file_name = f"image/{self.source_filter(source, category)}/{category}/{uuid.uuid4().hex}{ext}"
		print(f"[+] Downloading {unquote(url)}")
		try:
			async with async_timeout.timeout(360):
				async with session.get(url) as response:
					with open(file_name, "wb") as fd:
						async for data in response.content.iter_chunked(1024):
							fd.write(data)		
		except Exception as ex:
			return '[+] Failed downloaded ' + file_name + f" [{self.format_size(size, 'mb')}]"

		return '[+] Successfully downloaded ' + file_name + f" [{self.format_size(size, 'mb')}]"

	# Download Mode

	async def download_async(self, source: str, category: str, amount: int = 50):
		print("\n------ Searching ------\n")

		await self.get_image_links(source, category, amount)

		print('\n------ Downloader ------\n')

		async with aiohttp.ClientSession() as session:
			tasks = [self.download_url_async(url, session, source, category) for url in self.h3ntai_links]
			return await asyncio.gather(*tasks)

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

	def source_filter(self, source, category):
		sources_category = SourcesCategory()

		if source == "hmtai":
			if category in sources_category.hmtai_sfw():
				return "hmtai-sfw"
			elif category in sources_category.hmtai_nsfw():
				return "hmtai-nsfw"

		elif source == "nekos":
			if category in sources_category.nekos_sfw():
				return "nekos-sfw"
		elif source == "nekosfun":
			if category in sources_category.nekosfun_sfw():
				return "nekosfun-sfw"
			elif category in sources_category.nekosfun_nsfw():
				return "nekosfun-nsfw"



	
