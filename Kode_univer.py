import requests
import pwd_vk

token = pwd_vk.access_token
version = pwd_vk.v

def message_in(message_user):
    mes_out = message_user[:140]
    return mes_out

def message_post_vk(message_user, token, version):
    return requests.post(f'https://api.vk.com/method/wall.post?message={message_user}&access_token={token}&v={version}')

if __name__ == '__main__':

    # input message
    message_user = input()

    # check message length
    if len(message_user) > 140:
        print('Сообщение должно содержать не более 140 символов.')
        print('Длина сообщения: ' + str(len(message_user)) + '.')
        print('Будет опубликованно сообщение: \"' + message_in(message_user) + '\".')

    # trim message to 140 characters
    message_user = message_in(message_user)
    # print(len(message_user))

    # posting message on VKontakte
    try:
        mymes = message_post_vk(message_user, token, version)
        print(mymes)
        print('Сообщение опубликовано.')
    except ConnectionError:
        print('Ошибка подключения.')








