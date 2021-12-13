import requests
import pwd_vk
# import urllib.parse - message encoding issue, not resolved
# the code for publishing to Facebook should work, the problem is in the personal access key, I understand

token = pwd_vk.access_token
version = pwd_vk.v
token_fb = pwd_vk.access_token_fb
my_wall_number = pwd_vk.fb_number

# check message length and trim message to 140 characters
def message_in(message_user):
    if len(message_user) > 140:
        print('Сообщение должно содержать не более 140 символов.')
        print('Длина сообщения: ' + str(len(message_user)) + '.')
        print('Будет опубликованно сообщение: \"' + message_in(message_user) + '\".')
    mes_out = message_user[:140]
    return mes_out

def message_post_vk(message_user, token, version):
    vk_mes_out = requests.post(f'https://api.vk.com/method/wall.post?message={message_user}&access_token={token}&v={version}')
    return vk_mes_out

def message_post_fb(my_wall_number, message_user, token_fb):
    fb_mes_out = requests.post(f'https://graph.facebook.com/v12.0/{my_wall_number}?message={message_user}&access_token={token_fb}')
    return fb_mes_out


if __name__ == '__main__':
    # input message
    message_user = input('Введите сообщение: ')
    message_user = message_in(message_user)

    # posting message on VKontakte
    try:
        vk_mymes = message_post_vk(message_user, token, version)
        print('Ответ сервера VK: ', vk_mymes.json())
    except ConnectionError:
        print('Ошибка подключения во Vkontakte.')

    # posting message on Facebook
    try:
        fb_mymes = message_post_fb(my_wall_number, message_user, token_fb)
        print('Ответ сервера FB: ', fb_mymes.json())
    except ConnectionError:
        print('Ошибка подключения в Facebook.')







