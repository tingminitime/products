import os # operating system

# 讀取檔案
def read_file(fileName):
	products = [] # 大清單
	# 如果有products.csv這個檔案，就讀取
	with open(fileName, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 放棄這回，跳到下一回開始
			name, price = line.strip().split(',') #每一行用什麼東西切割
			# s = line.strip().split(',')
			# name = s[0]
			# price = s[1]
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
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
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(fileName, products):
	with open(fileName, 'w', encoding = 'utf-8') as f:
			f.write('商品,價格\n')
			for p in products:
				f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	fileName = 'products.csv'
	if os.path.isfile(fileName): # 檢查檔案在不在
		print('yeah! 找到檔案了!')
		products = read_file(fileName)
	else:
		print('找不到檔案...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()