import requests
from base64 import b64encode
import json


def uploadFile(filePath):
	headers = {
	    'Authorization': 'token 06fdde6755d5ac900db6a056957f93622d0de2a0',
	    'User-Agent': 'Zombrooc'
	}

	with open(filePath, 'rb') as f:
		g = str(b64encode(f.read())).strip("\'")[2:]

	data = '{"path": "{filePath}", "message": "TesteCommit", "content": "{content}", "branch": "master"}'.format(filePath=filePath, content=g)

	response = requests.put('https://api.github.com/repos/Zombrooc/VirtualAgenda/contents/text4.jpg', headers=headers, data=data)
	print(response.text)


def deleteFile():
	headers = {
		'Authorization': 'token 06fdde6755d5ac900db6a056957f93622d0de2a0',
	    'User-Agent': 'Zombrooc'
	}


	data = '{"message": "First Commit - Delete Func", "sha": "1285636b4364a5caa1d2f1147a2ae4830ebd56f2"}'

	response = requests.delete('https://api.github.com/repos/Zombrooc/VirtualAgenda/contents/text3.jpeg', headers=headers, data=data)


def listFiles():
	headers = {
	    'Authorization': 'token 06fdde6755d5ac900db6a056957f93622d0de2a0',
	    'User-Agent': 'Zombrooc'
	}

	response = requests.get('https://api.github.com/repos/Zombrooc/VirtualAgenda/contents/', headers=headers)
	x = response.json()


	for el in x:
		print(el['download_url'],'\n\n')


def updateFile():
	headers = {
	    'Authorization': 'token 06fdde6755d5ac900db6a056957f93622d0de2a0',
	    'User-Agent': 'Zombrooc'
	}

	with open('85.jpg', 'rb') as f:
		g = str(b64encode(f.read())).strip("\'")[2:]

	data = '{"message": "TesteCommit", "content": "'+g+'", "sha": "79c868fb14a9f5c2f7634d399586c1689c19c84e"}'

	response = requests.put('https://api.github.com/repos/Zombrooc/VirtualAgenda/contents/text4.jpg', headers=headers, data=data)
	print(response.text)


print(authenticate('06fdde6755d5ac900db6a056957f93622d0de2a0', 'Zombrooc'))