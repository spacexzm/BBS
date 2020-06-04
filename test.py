import json
book = dict()

chapter1 = dict(
	subtitle1 = "aaaaa",
	subtitle2 = "bbbbb",
	subtitle3 = "ccccc",
	)

chapter2 = dict(
	subtitle1 = "eeeee",
	subtitle2 = "fffff",
	subtitle3 = "ggggg",
	)

subsubtitle1 = dict(
	title1 = "abcd",
	title2 = "efgh",
	title3 = "ijkl")

chapter3 = dict(
	subtitle1 = "hhhhh",
	subtitle2 = "iiiii",
	subtitle3 = subsubtitle1)

book['chapter1'] = chapter1
book['chapter2'] = chapter2
book['chapter3'] = chapter3
json_book = json.dumps(book)

if __name__ == "__main__":
    print(book)
    print(json_book)




