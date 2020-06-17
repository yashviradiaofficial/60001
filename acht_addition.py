class Nums(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        nums1 = self.x + other.x
        nums2 = self.y + other.y
        return nums1 + nums2

c = Nums(3, 5)
origin = Nums(4, 6)
print(c.__add__(origin))
