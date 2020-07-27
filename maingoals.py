from collections import Counter

def main():
	filepath = open(r"goals.txt", "r")
	list = filepath.readlines()
	counts = Counter(list)
	newList = sorted(list, key=lambda x: (counts[x], x), reverse=True)
	c = Counter(newList)
	for word, count in c.items():
		print(word, count)
	filepath.close()

if __name__ == "__main__":
	main()
