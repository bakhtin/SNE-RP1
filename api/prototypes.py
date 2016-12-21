'''
Get file data by its block IDs

blocks: blocks as in Inode property (dict)
contiguous_data: actual data of the file

def get_data(blocks):
    return contiguous_data

Upload file data and return IDs of the blocks (filenames in socials)

def upload_data(contiguous_data):
    return blocks
'''
import requests
import json

def splitFile(inputFile,chunkSize):
	f = open(inputFile, 'rb')
	data = f.read()
	f.close()

	bytes = len(data)

	noOfChunks= bytes/chunkSize
	if(bytes%chunkSize):
		noOfChunks+=1

	chunkNames = []
	res = ''
	for i in range(0, bytes+1, chunkSize):
		fn1 = "chunk%s.mp3" % i
		res = res + header + data[i:i+ chunkSize]
		if 1024000 - len(res) < chunkSize:
			f = open(fn1, 'wb')
			f.write(header + res)
			f.close()
			res = ''
			chunkNames.append(fn1)
		if (len(data) - i) < chunkSize:
			res = res + data[i:len(data)]
			f = open(fn1, 'wb')
			f.write(header + res)
			f.close()
			res = ''
			chunkNames.append(fn1)
				
	return chunkNames

access_token = "4f050c2ec93a5ed968d23d3358d220632ecdbfe9c34beb95971bb05acdd3e75dd8ce3a181bdf181b9a665"
def upload_to_vk(array, filename):
	request_url = "https://api.vk.com/method/audio.getUploadServer" + "?access_token=" + access_token
	r = requests.get(request_url)
	url_to_upload = json.loads(r.text)['response']['upload_url']
	res = ""
	
	for i in array:
		files = {'file': (i, open(i, 'rb'), 'multipart/form-data', {'Expires': '0'})}
		r = requests.post(url_to_upload, files=files)
		response = json.loads(r.text)
		request_url = "https://api.vk.com/method/audio.save" + "?access_token=" + access_token
		payload = {'server': response['server'], 'audio': response['audio'], 'hash': response['hash']}
		r = requests.get(request_url, params=payload)
		print r.text

#header="\xff\xfb\xe4\x44"
#chunkNames = splitFile("123.mp3", 956)
#upload_to_vk(chunkNames, "123")


