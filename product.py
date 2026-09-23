class Dimensions:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

class Reviews:
    def __init__(self, ratings, reviewerName, comment):
        self.ratings = ratings
        self.reviewerName = reviewerName
        self.comment = comment

class ProductData:
    def __init__(self, id, productName, price,category, width, height, depth, tags, reviews):
        self.id = id
        self.productName = productName
        self.price = price
        self.category = category
        self.dimensions = Dimensions(width, height, depth)
        self.tags = tags
        self.reviews = reviews


reviews = list()
r1 = Reviews(3, "Vignesh", "Better")
reviews.append(r1)

reviews.append(Reviews(4, "Rahul", "Good"))

productN = ProductData(1, "Calvin Klein CK One",500, "fragrance",
                       "29.36", "23.22", "20.00", ["Fragrance", "Perfume"], reviews)
print(productN.__dict__)
print(productN.reviews[0].__dict__)


