from modules.downloader import Downloader
from modules.setup import Setup
import asyncio

downloader = Downloader()
setup = Setup()

setup.create_folder_struct()

def main():
	loop = asyncio.get_event_loop()
	results = loop.run_until_complete(downloader.download_async("hmtai", "yuri", 10))
	print('\n'.join(results))

	# downloader.download_while_get_link("hmtai", "yuri", "image/yuri")

main()
