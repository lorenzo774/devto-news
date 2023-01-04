class Article:
    def __init__(self, title: str, link: str, author: str, date: str):
        self.title = title
        self.link = link
        self.author = author
        self.date = date

    def __str__(self):
        return f'\n{self.date}\nBy \033[1;3m{self.author}\x1B[0m\n\033[1m\n{self.title}\033[0m\n🔗 {self.link}\n{"__" * 40}\n'