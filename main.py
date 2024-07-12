import requests,random
from bs4 import BeautifulSoup
from faker import Faker
class FaceBook_RegIster():
    def init(self):
        self.done = False
        self.cookies = {
            "lsd": "",
            "jazoest": "",
            "ccp": "",
            "reg_instance": "",
            "submission_request": "",
            "reg_impression_id": ""
        }
        self.password = "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(10))
        self.email = "angledev" + "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(15))
        self.Name = fake.first_name()
        self.Name2 = fake.last_name()
        self.admin()
    def admin(self):
        print("[+] get cookies ..")
        self.get_cookies()
        print('[+] Create The Account ..')
        self.register()
    def get_cookies(self):
        url = "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        lsd = soup.select_one('input[name=lsd]')['value']
        jazoest = soup.select_one('input[name=jazoest]')['value']
        ccp = soup.select_one('input[name=ccp]')['value']
        reg_instance = soup.select_one('input[name=reg_instance]')['value']
        submission_request = soup.select_one('input[name=submission_request]')['value']
        reg_impression_id = soup.select_one('input[name=reg_impression_id]')['value']
        self.cookies['lsd'] = lsd
        self.cookies['jazoest'] = jazoest
        self.cookies['ccp'] = ccp
        self.cookies['reg_instance'] = reg_instance
        self.cookies['submission_request'] = submission_request
        self.cookies['reg_impression_id'] = reg_impression_id
    def register(self):
        url = "https://mbasic.facebook.com/reg/submit/?cid=103"
        headers = {
            "Host": "mbasic.facebook.com",
            "Cookie": f"datr={self.cookies['reg_instance']}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "547",
            "Origin": "https://mbasic.facebook.com",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers"
        }
        data = f"lsd={self.cookies['lsd']}&jazoest={self.cookies['jazoest']}&ccp={self.cookies['ccp']}&reg_instance={self.cookies['reg_instance']}&submission_request={self.cookies['submission_request']}&helper=&reg_impression_id={self.cookies['reg_impression_id']}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names%5B%5D=firstname&field_names%5B%5D=reg_email&field_names%5B%5D=sex&field_names%5B%5D=birthday_wrapper&field_names%5B%5D=reg_passwd&firstname={self.Name}&lastname={self.Name2}&reg_email={self.email}%40yopmail.com&sex={random.randint(1,2)}&custom_gender=&did_use_age=false&birthday_month=random.randint(1,12)&birthday_day=random.randint(1,28)&birthday_year={random.randint(1996,2005)}&age_step_input=&reg_passwd={self.password}&submit=Sign+Up"
        r = requests.post(url,headers=headers,data=data)
        if 'take you through a few steps to confirm your account on Facebook' in r.text:
            print('[+] Done Create Account !')
            print('[+] Username : Not Found ( Login Use Email )')
            print("[+] Email :" + self.email + "@yopmail.com")
            print("[+] Password : " + self.password)
            print("[+] Status : Confirm")
            print('='*40)
        elif 'There was an error with your registration. Please try registering again.' in r.text:
            print('[X] Blocked From Facebook')
            print('='*40)
        else:
            try:
                user_id = r.cookies['c_user']
                print('[+] Done Create Account !')
                print('[+] Username : '+r.cookies['c_user'])
                print("[+] Email :" + self.email + "@yopmail.com")
                print("[+] Password : " + self.password)
                print("[+] Status : Done Create Account")
                print('='*40)
            except:
                print("[X] Use Vpn")
                print('='*40)
while True:
 FaceBook_RegIster()
