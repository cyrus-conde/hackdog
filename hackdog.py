#Decompiled by MR.K7C8NG
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def exit():
    print '\x1b[1;91m[!] exit'
    os.sys.exit()


def wait(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


intro1 = 'HH    HH     A	   CCCCC  KK	KK  DDDDD	 OOOOO	 GGGGGG'
intro2 = 'HH    HH    A A	 CC       KK  KK    DD   DD	O     O	 G	   '
intro3 = 'HHHHHHHH   A   A	CC	  KKKK	    DD	 DD	O     O	 G GGGG'
intro4 = 'HH    HH  AAAAAAA	 CC       KK  KK    DD   DD	O     O	 G    G'
intro5 = 'HH    HH AA     AA	   CCCCC  KK	KK  DDDDD	 OOOOO	 GGGGGG'

def tick():
    titick = [
     '.   ', '..  ', '... ']
    for o in titick:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92m Connecting \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []



def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print intro1
        print intro2
        print intro3
        print intro4
        print intro5
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN YOUR FACEBOOK ACCOUNT \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36m Username \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36m Password \x1b[1;91m:\x1b[1;92m ')
        tick()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No Connection'
            exit()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                hdog = open('login.txt', 'w')
                hdog.write(z['access_token'])
                hdog.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin Successful'
                os.system('xdg-open https://www.youtube.com/channel/UCHIWqhRSv3kf124JHkixBnw')
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No Connection'
                exit()

        if 'checkpoint' in url:
        	print '\n\x1b[1;91m[!] \x1b[1;93m checkpoint!'
            	print '\n\x1b[1;91m[!] \x1b[1;93m Please login your account in browser'
        	os.system('rm -rf login.txt')
            	time.sleep(1)
            	exit()
        else:
            	print '\n\x1b[1;91m[!] Login Failed'
            	os.system('rm -rf login.txt')
           	time.sleep(1)
            	login()


def menu():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('clear')
            print '\n\x1b[1;91m[!] \x1b[1;93m checkpoint!'
            print '\n\x1b[1;91m[!] \x1b[1;93m Please login your account in browser'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] No Connection'
            exit()

    os.system('clear')
    print intro1
    print intro2
    print intro3
    print intro4
    print intro5
    print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama
    print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
    print '\x1b[1;37;40m1. information Pengguna'
    print '\x1b[1;37;40m2. Guard       '
    print '\x1b[1;37;40m3. LogOut            '
    print '\x1b[1;31;40m0. exit            '
    print
    select()


def select():
    hdog = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if hdog == '':
        print '\x1b[1;91m[!] Select option'
        select()
    else:
        if hdog == '1':
            information()
        else:
            
            if hdog == '2':
                guard()
            else:
                if hdog == '3':
                    os.system('rm -rf login.txt')
                    os.system('xdg-open https://www.youtube.com/channel/UCHIWqhRSv3kf124JHkixBnw')
                    exit()
                else:
                    if hdog == '0':
                        exit()
                    else:
                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hdog + ' \x1b[1;91m select again'
                        select()


def information():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print intro1
    print intro2
    print intro3
    print intro4
    print intro5 
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    wait('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92m Wait a minute \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + token)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mTidak ada'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mTidak ada'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNomor HP\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m      : \x1b[1;91mTidak ada'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m        : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m        : \x1b[1;91mTidak ada'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] Pengguna tidak ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()

def guard():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print intro1
    print intro2
    print intro3
    print intro4
    print intro5
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Activate'
    print '\x1b[1;37;40m2. Switch it off'
    print '\x1b[1;31;40m0. Back'
    print
    g = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if g == '1':
        active = 'true'
        guard_check(token, active)
    else:
        if g == '2':
            nonactive = 'false'
            guard_check(token, nonactive)
        else:
            if g == '0':
                select()
            else:
                if g == '':
                    exit()
                else:
                    exit()


def get_userid(token):
    url = 'https://graph.facebook.com/me?access_token=%s' % token
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def guard_check(token, enable=True):
    id = get_userid(token)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % token}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print intro1
        print intro2
        print intro3
        print intro4
        print intro5
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92m Activated'
        raw_input('\n\x1b[1;91m[ \x1b[1;97m Back \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print intro1
	        print intro2
	        print intro3
	        print intro4
	        print intro5
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91m Disabled'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            exit()

if __name__ == '__main__':
	login()
# okay decompiling 3.pyc
