import requests

def download_and_save(url, x):
	pdf = requests.get(url)

	filename = "Chapter"+str(x)
	with open(filename,'wb') as f:
		f.write(pdf.content)

def get_pdfs():
	number = 1
	x=1
	url = "http://sites.math.rutgers.edu/~ajl213/CLRS/Ch"+str(number)+".pdf"
	while(number<=35):
		download_and_save(url,x)
		number+=1
		x+=1

if __name__ == '__main__':
	get_pdfs()