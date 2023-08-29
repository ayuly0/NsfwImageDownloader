from modules.downloader import Downloader
from modules.setup import Setup
from modules.menu import Menu
import asyncio

downloader = Downloader()
setup = Setup()
menu = Menu()

setup.create_folder_struct()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
	start = False
	source = None
	category = None
	amount = None

	while not start:
		
		source = menu.select_source()

		category = menu.select_category(source)

		amount = menu.only_number("Amount of image you wnat to download?", int)

		source = source.split('-')

		print("Your Choose")

		print("\tSource:",source[0])
		print("\tCategory:",category)
		print("\tAmount:",amount)

		change = menu.confirm("Do you want to change? ", False)

		start = True if not change else False

	results = await downloader.download_async(source[0], category, amount)
	print('\n------ Results ------\n')
	print('\n'.join(results))

while True:
	__import__('os').system('cls')
	
	asyncio.run(main())

	print('\n')
	again = menu.confirm("Do you want to use agian?", True)
	if not again:
		break

	__import__('os').system('cls')
