from tkinter.messagebox import showwarning
from django.utils.datetime_safe import strftime
from git.exc import InvalidGitRepositoryError
from git.repo.base import Repo

__author__ = 'Girish'

class Github_wrap:
    def __init__(self, master, repo=None):
        if repo:
            self.repo = repo

        self.master = master

    def set_repo(self, repo):
        self.validate(repo)

    def validate(self,repo):
        try:
            self.repo = Repo(repo)
            print(self.repo.remotes)
        except InvalidGitRepositoryError:
            showwarning("There is no repo here !! Will create one for you")
            self.repo = Repo.init(repo)


    def commit(self, message):
        """

        :param message: a function which returns a string of the message to display
        :return:
        """
        index = self.repo.index
        changes =[diff.a_blob.path for diff in index.diff(None)]
        for change in changes:
            try:
                index.add([change])
            except FileNotFoundError:
                index.remove([change])
        index.commit("synced at {}".format(message()))

    def incremental_commit(self):
        """

        :param message: a function which returns a string of the message to display
        :return:
        """
        print("inside commit")
        index = self.repo.index
        print(self.repo.untracked_files)
        changes =[diff.a_blob.path for diff in index.diff(None)]
        print(changes)

        for w in self.repo.untracked_files:
            index.add([w])
            index.commit("added a file {}".format(w))
        for change in changes:
            try:
                index.add([change])
                index.commit("changed file {}".format(change))
                print("added file {}".format(change))

            except FileNotFoundError:
                index.remove([change])
                index.commit("removed file  {}".format(change))
                print("removed file {}".format(change))
        self.push()


    def push(self):
        self.repo.git.push()