import vk_api.vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
import urllib.request, json 
import requests
from key import token, id

class Server:

            def __init__(self, api_token, group_id, server_name: str="Empty"):

                # Даем серверу имя
                self.server_name = server_name

                # Для Long Poll
                self.vk = vk_api.VkApi(token=api_token)

                self.upload = vk_api.VkUpload(self.vk)

                # Для использования Long Poll API
                self.long_poll = VkBotLongPoll(self.vk, group_id)

                # Для вызова методов vk_api
                self.vk_api = self.vk.get_api()

            def send_img(self, send_id, attachments, text):
                """
                Отправка сообщения через метод messages.send
                :param send_id: vk id пользователя, который получит сообщение
                :param message: содержимое отправляемого письма
                :return: None
                """
                self.vk_api.messages.send(peer_id=send_id,
                                          message=text,
                                          attachment = attachments,
                                          random_id=123456 + random.randint(1,27))

            def send_msg(self, send_id, message):
                """
                Отправка сообщения через метод messages.send
                :param send_id: vk id пользователя, который получит сообщение
                :param message: содержимое отправляемого письма
                :return: None
                """
                self.vk_api.messages.send(peer_id=send_id,
                                          message=message,
                                          random_id=123456 + random.randint(1,27))
            #def GetText():
                #pass
            def start(self):
                for event in self.long_poll.listen():
                    #print(event.message.text, " ", event.message.peer_id)
                    print(event)
                    print(id)
                    #if event.message.text == "привет":
                     #   self.send_msg(event.object.peer_id, "Привет от бота")
                    
                        

if __name__ ==  "__main__":
    server1 = Server(token, id, "server1")
    server1.start() 
