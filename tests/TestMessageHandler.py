from talker.message_handler import *

handler = MessageHandler()
handler.handle_message('how many adgroup do i have in campaign ABC')
handler.handle_message('how many campaign do i have')
handler.handle_message('how many campaigns in my account')

handler.handle_message('how many ad group in campaign 1234')
handler.handle_message('how many adgroups in my account')