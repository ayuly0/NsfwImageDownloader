import inquirer
from .sources_category import SourcesCategory

class Menu:

	def selection(self, message = None, choices = None) -> str:
		questions = [
				inquirer.List("answers",
				  message=message,
				  choices=choices),
				]
		answers = inquirer.prompt(questions)

		return answers["answers"]

	def confirm(self, message = None, default = True) -> bool:
		confirm = {
				inquirer.Confirm('confirm',
					 message = message,
					 default = default,
					 ),
				}
		confirmation = inquirer.prompt(confirm)

		return confirmation["confirm"]

	def select_source(self):
		sources_category = SourcesCategory()
		sources = sources_category.sources_folder()
		source = self.selection(message = "What source you want to use?", choices = sources)

		return source

	def select_category(self, source):
		source_category = SourcesCategory()
		category = []
		list_category = {
				"sfw":
					{
						"hmtai": sorted(source_category.hmtai_sfw()),
						"nekos": sorted(source_category.nekos_sfw()),
						"nekosfun": sorted(source_category.nekosfun_sfw())
					},

				"nsfw":
					{
						"hmtai": sorted(source_category.hmtai_nsfw()),
						"nekosfun": sorted(source_category.nekosfun_nsfw())
					}
			}

		_source, type_source = source.split('-')

		category = self.selection(message = "What category you want to use?", choices = list_category[type_source][_source])

		return category

	def only_number(self, message, input_type=str, default = 50):
		while True:
			try:
				ans = input(f"{message} (default: {default}) ")
				if ans == "":
					return default
				return input_type(ans)
			except:
				print("Only number!")
