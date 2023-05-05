# def add(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n
#     print(sum)
#
#
# add(2, 5, 4)
#
#
# def calculate(n, **kwargsargs):
#     print(kwargsargs)
#     for key in kwargsargs:
#         print(key)
#
#     n += kwargsargs["add"]
#     n *= kwargsargs["multiply"]
#     print(n)
#
#
# calculate(5, add=5, multiply=3)
#

class Insta:

    def __int__(self, **kwargs):
        self.feed = kwargs.get("feed")
        self.reels = kwargs.get("reels")
        self.msgs = kwargs.get("msgs")


my_account = Insta(feed= "feed", reels = "reels", msgs= "love")
print(my_account.msgs)
