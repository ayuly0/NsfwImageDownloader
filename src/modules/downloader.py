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

class Url:

	@staticmethod
	def get_extension_file(url) -> str:
		url = unquote(url)
		url = urlparse(url).path
		_, extensition = os.path.splitext(os.path.basename(url))

		return extensition
	@staticmethod
	def get_size_file(url):
		res = requests.head(url, allow_redirects=True)
		size = int(res.headers.get("content-length", -1))
		return size

class File:

	@staticmethod
	def format_size(size, unit = "kb"):
		exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
		size = size / 1024 ** exponents_map[unit]
		return f"{round(size, 2)} {unit.upper()}"


class Downloader:
	# Download Functions

	async def download_url_async(self, url, session, source, category) -> str:
		size = Url.get_size_file(url)
		ext = Url.get_extension_file(url)

		file_name = f"image/{SourcesCategory.source_filter(source, category)}/{category}/{uuid.uuid4().hex}{ext}"
		print(f"[+] Downloading {unquote(url)} [{File.format_size(size, 'mb')}]")
		try:
			async with async_timeout.timeout(360):
				async with session.get(url) as response:
					with open(file_name, "wb") as fd:
						async for data in response.content.iter_chunked(1024):
							fd.write(data)		
		except Exception as ex:
			return '[+] Failed downloaded ' + file_name + f" [{File.format_size(size, 'mb')}]"

		return '[+] Successfully downloaded ' + file_name + f" [{File.format_size(size, 'mb')}]"

	# Download Mode

	async def download_async(self, source: str, category: str, amount: int = 50):
		print("\n------ Searching ------\n")

		links_wrap = await hmtai.get(source, category, amount)

		print('\n------ Downloader ------\n')

		async with aiohttp.ClientSession() as session:
			tasks = [self.download_url_async(url, session, source, category) for url in links_wrap]
			return await asyncio.gather(*tasks)

	
	
