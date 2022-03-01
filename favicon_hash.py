import requests
import mmh3
import base64
import sys,getopt
def favicon_hash(url):
	# url = 'https://www.baidu.com/favicon.ico'
	res = requests.get(url)
	picb64 = base64.b64encode(res.content)
	ha = mmh3.hash(picb64)
	# print (picb64)
	return print(ha)


def main(argv):
	try:
		opts,args = getopt.getopt(argv,'-h-u:-v',['help','url=','version'])
	except getopt.GetoptError:
		print(' favicon_hash.py -h 查看用法')
		sys.exit(2)
	for opt,arg in opts:
		if opt in ('-h','--help'):
			print('''usage:
				favicon_hash.py -u/--url <favicon_url>\t基础使用\n
				favicon_hash.py -h\t帮助信息\n
				favicon_hash.py -v\t版本信息''')
			sys.exit()
		elif opt in ('-u','--url'):
			 url = arg
			 favicon_hash(url)
			 sys.exit()
		elif opt in ('-v','--version'):
			print('Ver 1.0.0')
			sys.exit()



if __name__ == '__main__':
	# url = input('please input favicon_url:')
	# favicon_hash(sys.argv)
	# favicon_hash('https://www.baidu.com/favicon.ico')
	main(sys.argv[1:])
	# favicon_hash(url)