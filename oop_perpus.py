from libs.library import Library, Member

# create lib object
book_lib = Library("Book Library")

# create john object member
user_john = Member("John Doe")
user_john.activate()  # active john membership

# create jane object member
user_jane = Member("Jane Doe")

# register member to lib
book_lib.register_member(user_john)
book_lib.register_member(user_jane)

for member in book_lib.members:
    print(f"{member} status is: {'active' if member.is_active else 'not active'}")
