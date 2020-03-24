# 讀取檔案
products = [] # 大清單

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 放棄這回，跳到下一回開始
		name, price = line.strip().split(',') #每一行用什麼東西切割
		# s = line.strip().split(',')
		# name = s[0]
		# price = s[1]
		products.append([name,  price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')

	if name == 'q': # quit
		break

	price = input('請輸入商品價格: ')
	price = int(price)

	# p = [] # 小清單
	# p.append(name)
	# p.append(price)

	# p = [name, price]

	# products.append(p) # 把小清單塞進大清單
	products.append([name, price]) # 最簡潔寫法

print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
