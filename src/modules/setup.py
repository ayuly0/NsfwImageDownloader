import os
from .sources_category import SourcesCategory

class Setup:
	def __init__(self):
		self.sources_category = SourcesCategory()

	def create_folder_struct(self):
		if not os.path.exists("image/"):
			os.mkdir("image/")

		for source in self.sources_category.sources_folder():
			if not os.path.exists(f"image/{source}"):
				os.mkdir(f"image/{source}")

		for hmtai_sfw in self.sources_category.hmtai_sfw():
			if not os.path.exists(f"image/hmtai-sfw/{hmtai_sfw}"):
				os.mkdir(f"image/hmtai-sfw/{hmtai_sfw}")
		
		for hmtai_nsfw in self.sources_category.hmtai_nsfw():
			if not os.path.exists(f"image/hmtai-nsfw/{hmtai_nsfw}"):
				os.mkdir(f"image/hmtai-nsfw/{hmtai_nsfw}")

		for nekos_sfw in self.sources_category.nekos_sfw():
			if not os.path.exists(f"image/nekos-sfw/{nekos_sfw}"):
				os.mkdir(f"image/nekos-sfw/{nekos_sfw}")

		for nekos_nsfw in self.sources_category.nekos_nsfw():
			if not os.path.exists(f"image/nekos-nsfw/{nekos_nsfw}"):
				os.mkdir(f"image/nekos-nsfw/{nekos_nsfw}")

		for neko_bot_sfw in self.sources_category.neko_bot_sfw():
			if not os.path.exists(f"image/neko-bot-sfw/{neko_bot_sfw}"):
				os.mkdir(f"image/neko-bot-sfw/{neko_bot_sfw}")

		for neko_bot_nsfw in self.sources_category.neko_bot_nsfw():
			if not os.path.exists(f"image/neko-bot-nsfw/{neko_bot_nsfw}"):
				os.mkdir(f"image/neko-bot-nsfw/{neko_bot_nsfw}")

		for neko_love_sfw in self.sources_category.neko_love_sfw():
			if not os.path.exists(f"image/neko-love-sfw/{neko_love_sfw}"):
				os.mkdir(f"image/neko-love-sfw/{neko_love_sfw}")

		for neko_love_nsfw in self.sources_category.neko_love_nsfw():
			if not os.path.exists(f"image/neko-love-nsfw/{neko_love_nsfw}"):
				os.mkdir(f"image/neko-love-nsfw/{neko_love_nsfw}")
