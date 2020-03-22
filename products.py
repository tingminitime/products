products = [] # 大清單

while True:
	name = input('請輸入商品名稱: ')

	if name == 'q': # quit
		break

	price = input('請輸入商品價格: ')

	# p = [] # 小清單
	# p.append(name)
	# p.append(price)

	# p = [name, price]

	# products.append(p) # 把小清單塞進大清單
	products.append([name, price]) # 最簡潔寫法

print(products)