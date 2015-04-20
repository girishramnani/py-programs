
__author__ = 'Girish'


class Github:
    def __init__(self, master, repo=None):
        if repo:
            self.repo = repo
        self.master = master

    def set_user_and_pass(self):
        pass


    def set_repo(self, repo):
        if self.validate():
            self.repo = repo


    def validate(self):
        pass


    def add_all(self):
        pass

    def commit(self, message):
        pass

    def push(self, home, remote=None):
        if remote is None:
            self.remote = "origin"
