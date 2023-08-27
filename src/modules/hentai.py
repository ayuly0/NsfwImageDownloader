import uuid
import hmtai
import requests
import concurrent.futures
from tqdm import trange

class GetHentaiImage:
    def __init__(self):
        self.h3ntai_links = []

    def get_link(self, source: str, cagetory: str) -> None:
        link = ''

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(hmtai.get, source, cagetory)
            link = future.result()

        self.h3ntai_links.append(link)
    
    def get_image_links(self, source: str, cagetory: str, amount: int = 50) -> None:
        self.h3ntai_links = []
      
        for i in range(amount):
            self.get_link(source, cagetory)


    def download_file(self, url: str, save_path: str) -> None:
        res = requests.get(url)

        with open(save_path, 'wb') as f:
            f.write(res.content)

    def download_while_get_link(self, source: str, cagetory: str, save_path: str, amount: int = 50) -> None:
        with trange(amount, postfix = [{'value': 0}], bar_format = "{percentage:.0f}%|{bar}| {postfix[0][value]}/{total} {desc}") as t:
            for i in t:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    link = hmtai.get(source, cagetory)
                    t.set_description(f'Found {link}')
                    save_path_new = f'{save_path}-{uuid.uuid4().hex}.png'
                    t.set_description(f'Starting download...')
                    executor.submit(self.download_file, link, save_path_new)
                    t.set_description(f'Save as {save_path_new}')
                    t.postfix[0]["value"] = i + 1
                    t.update()

class Help:
    pass

class Menu:
    pass
