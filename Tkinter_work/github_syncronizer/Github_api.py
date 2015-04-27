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
            showwarning("warning","There is no repo here !! Will create one for you")
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
            except PermissionError:
                continue
        index.commit("synced at {}".format(message()))

    def incremental_commit(self,terminal=None):
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
            try:
                index.add([w])
                if terminal:
                    terminal.print("added a file {}".format(w))
                index.commit("\tadded a file {}".format(w))
            except PermissionError:
                if terminal:
                    terminal.print("\tpermission denied for the file "+w)
                print("permission denied for the file "+w)
        for change in changes:
            try:
                index.add([change])
                index.commit("changed file {}".format(change))
                if terminal:
                    terminal.print("\tadded file {}".format(change))
                print("added file {}".format(change))

            except FileNotFoundError:
                index.remove([change])
                index.commit("removed file  {}".format(change))
                if terminal:
                    terminal.print("\tremoved file {}".format(change))
                print("removed file {}".format(change))
            except PermissionError:
                print("No permission")
        self.push()


    def push(self):
        try:
            self.repo.git.push()
        except:
            print("Offline mode")
            self.offline =True