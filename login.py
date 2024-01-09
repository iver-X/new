class login:
	def __init__(self):
		self.ada = []
	def __login__(self):
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f' {b} COKIE MU ASU :{asu} ')
		open("cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3950.0 Iron Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
 token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                open("token.x", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		os.system('clear')
		exit()
	except Exception as e:
		os.system("rm -f token.x")
		os.system("rm -f cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
