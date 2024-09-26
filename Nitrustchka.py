import requests
import random
import string
import time

def generate_nitro_code():
    code = ""
    for _ in range(16):
        code += random.choice(string.ascii_letters + string.digits)
    return code

# юрл вебхука (Webhook Url)
webhook_url = ''

for _ in range(100):
    nitro_code = generate_nitro_code()
    nitro_url = "https://discord.gift/" + nitro_code

    #Кастомка (не работает) (Custom message, dont work)

    message = ""
    
    # Кидает сообщение (send message
    data = {"content": nitro_url}
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Отправил брат:", nitro_url)
    else:
        print("Не получилось отправить.")
    
    # Добавляет вэйт в 1 секунду, ибо дс ограничивает бота, если он отправляет очень много сообщений (1 second wait)
    time.sleep(1)
#maked by SamoreZ, or Uofi._
