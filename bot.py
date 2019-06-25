import requests
import datetime
from time import sleep

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout':100, 'offset': None}
        response = requests.get(self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return response
    
    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

def main():
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Долгой жизни тебе, тан, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Честь тебе, тан, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Я прямо за тобой, {}'.format(last_chat_name))
            today += 1

    new_offset = last_update_id + 1
    
token = '712698190:AAHYip08IZHbSs0NgNkk1PDWZcqKisaYKLA'    
greet_bot = BotHandler(token)
greetings = ('привет', 'hi', 'hello')
now = datetime.datetime.now()

if __name__ == '__main__':
    try:
        print('starting bot')
        main()
    except KeyboardInterrupt:
        exit()

