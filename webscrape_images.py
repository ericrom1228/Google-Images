'''
This program saves images from google to a download directory
You can specify file type, size, ect by adjusting the arguments 
see link for arguments
'''

# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
response = google_images_download.googleimagesdownload() 

search_queries =[
	'green shirt', 
	'red pants',  
	'blue jeans', 
	'yellow sneakers'
	] 

def downloadimages(query):
	# https://google-images-download.readthedocs.io/en/latest/arguments.html
	arguments = {"keywords": query, 
				"format": "jpg", 
				"limit":4, 
				"print_urls":True} 
	try: 
		response.download(arguments) 
		 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":True} 
		try: 
			response.download(arguments) 
		except: 
			pass

for query in search_queries: 
	downloadimages(query) 
	print() 
