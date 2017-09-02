from Recipe_Book_Class import RecipeBook

filename = "Recipe_Book.txt"

New_Recipe_Book = RecipeBook()

New_Recipe_Book.parser(filename)

print len(New_Recipe_Book._Recipe_List)

