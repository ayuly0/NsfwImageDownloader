class SourcesCategory:
	
	def sources(self):
		return ["hmtai", "nekos", "nekobot", "nekosfun"]

	def sources_folder(self):
		return ["hmtai-sfw", 'hmtai-nsfw', "nekos-sfw", "nekosfun-sfw", "nekosfun-nsfw"]

	def hmtai_sfw(self):
		return ["wave","tea","punch","poke","pat","kiss","feed","hug","cuddle","cry","slap","lick","bite","dance","boop","sleep","like","kill","nosebleed","threaten","tickle","depression","jahy_arts","neko_arts","coffee_arts","wallpaper","mobileWallpaper"]

	def hmtai_nsfw(self):
		return ["anal","ass","bdsm","cum","classic","creampie","manga","femdom","hentai","incest","masturbation","public","ero","orgy","elves","yuri","pantsu","glasses","cuckold","blowjob","boobjob","footjob","handjob","boobs","thighs","pussy","ahegao","uniform","gangbang","tentacles","gif","nsfwNeko","nsfwMobileWallpaper","zettaiRyouiki"]

	def nekos_sfw(self):
		return ["wallpaper","ngif","tickle","feed","gecg","gasm","slap","avatar","lizard","waifu","pat","8ball","kiss","neko","spank","cuddle","fox_girl","hug","smug","goose","woof"]
	
	def nekosfun_sfw(self):
		return ["kiss","lick","hug","baka","cry","poke","smug","slap","tickle","pat","laugh","feed","cuddle"]

	def nekosfun_nsfw(self):
		return ["4K","ass","blowjob","boobs","cum","feet","hentai","wallpapers","spank","gasm","lesbian","lewd","pussy"] 
	
	@staticmethod
	def source_filter(source, category):
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

