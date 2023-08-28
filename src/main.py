from modules.downloader import Downloader
from modules.setup import Setup
import asyncio

downloader = Downloader()
setup = Setup()

setup.create_folder_struct()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def main():
	results = asyncio.run(downloader.download_async("hmtai", "uniform"))
	print('\n'.join(results))

	# downloader.download_while_get_link("hmtai", "yuri", "image/yuri")

main()
