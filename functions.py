import requests
import json
import re
import urllib

def splitFile(inputFile,chunkSize):
	header="\xff\xfb\xe4\x44"
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
		if (len(data) - i) < chunkSize:
			res = res + data[i:len(data)]
			f = open(fn1, 'wb')
			f.write(header + res)
			f.close()
			res = ''
			chunkNames.append(fn1)
			if 1024000 - len(res) < chunkSize:
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

def download_from_vk(array):
	array = ["396547478_456239053", "396547478_456239054"]
	string = ''
	for i in array:
		string = string + "," + i
	
	headers = {
		'origin': 'https://vk.com',
		'accept-encoding': 'gzip, deflate, br',
		'x-requested-with': 'XMLHttpRequest',
		'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
		'content-type': 'application/x-www-form-urlencoded',
		'accept': '*/*',
		'referer': 'https://vk.com/audios396547478',
		'authority': 'vk.com',
		'cookie': 'remixdt=0; remixtst=6a6160ae; remixsid=e08c978875d6955f5cf30f7edfcffb6e5197f9c448626357437a5; remixsslsid=1; remixseenads=2; remixlang=0; remixrefkey=8a3de8954c2156ec2a; remixflash=23.0.0; remixscreen_depth=24; remixcurr_audio=396547478_456239053',
	}
	data = {
		'act': 'reload_audio',
		'al': '1',
		'ids': string
	}
	print data
	r = requests.post('https://vk.com/al_audio.php', headers=headers, data=data)
	response = re.search('\[\[.+\]\]', r.text)
	response = json.loads(response.group(0))
	output = ''
	print response
	for i in response:
		#print i
		#donwloadedfile = urllib.URLopener()
		filename = str(i[1])+"_"+str(i[0])+".mp3"
		#donwloadedfile.retrieve(i[2], filename)

		f = open(filename, 'rb')
		data = f.read()
		f.close()
		bytes = len(data)
		chunkSize = 960
		res = ''
		for j in range(0, bytes+1, chunkSize):
			res = res + data[j:j+chunkSize-4]
		output = output + res
		print j
	print len(output)
