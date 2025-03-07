import pandas as pd


class Member:
    def __init__(self, name):
        self.name = name
        self.is_active = True
        self.borrowed_books = []

    def __str__(self):
        return self.name

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def register_member(self, member: Member):
        self.members.append(member)

    def get_active_members(self):
        active_members = []
        for member in self.members:
            if member.is_active:
                active_members.append(member)
        return active_members

    def get_members_df(self):
        l_members = []
        for member in self.members:
            l_members.append([member.name, member.is_active])

        df = pd.DataFrame(l_members, columns=["name", "status"])
        return df
