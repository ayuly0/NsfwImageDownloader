"""
HMTAI PORT REWRITE - by @NMWIN_D (twitter) & NickSaltFoxu ( comeback, guys )
Used original port made by NickSaltFoxu
HMTAI is an Anime / Hentai (NSFW) Image API which simplifies how you fetch random images from the official REST API!\n
"""
from .hmfull import hmfull

class CategoryNotFound(Exception):
	def __init__(self, categoryn):
		self.categoryn = categoryn
		self.message = f"I don't found '{categoryn}' in list of categories. Please, check docs for right names."
		super().__init__(self.message)

class SourceNotFound(Exception):
	def __init__(self, source):
		self.source = source
		self.message = f"I don't found {source} in list of categories. Please, check docs for right names."
		super().__init__(self.message)

class NoSourceEntered(Exception):
	def __init__(self):
		self.message = f"Source name is empty."
		super().__init__(self.message)

class NoCategoryEntered(Exception):
	def __init__(self):
		self.message = f"Category name is empty."
		super().__init__(self.message)

async def get(source = None, category = None, amount = 1):
	if source == None:
		raise NoSourceEntered
	if category == None:
		raise NoCategoryEntered
	if source == "hmtai":
		res = await hmfull.hmtai_async(category, amount)
		try:
			if res == 0:
				raise CategoryNotFound(category)
			else:
				return res
		except Exception as e:
			print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")

	elif source == "nekos":
		try:
			res = await hmfull.nekos_async(category, amount)
			if res == 0:
				raise CategoryNotFound(category)
			else:
				return res
		except Exception as e:
			print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")

	elif source == "nekosfun":
		try:
			res = await hmfull.nekosfun_async(category, amount)
			if res == 0:
				raise CategoryNotFound(category)
			else:
				return res
		except Exception as e:
			print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")


def useHM(version = None, category = None):
	return get("hmtai",f"{category}")
