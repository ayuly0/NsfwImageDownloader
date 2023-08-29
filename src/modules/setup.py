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

		for nekosfun_sfw in self.sources_category.nekosfun_sfw():
			if not os.path.exists(f"image/nekosfun-sfw/{nekosfun_sfw}"):
				os.mkdir(f"image/nekosfun-sfw/{nekosfun_sfw}")
		
		for nekosfun_nsfw in self.sources_category.nekosfun_nsfw():
			if not os.path.exists(f"image/nekosfun-nsfw/{nekosfun_nsfw}"):
				os.mkdir(f"image/nekosfun-nsfw/{nekosfun_nsfw}")
