import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Ваш токен сообщества и ID группы
GROUP_TOKEN = 'vk1.a.ROAATc7cYPpVB1ZwFgxvmfIAGHfRP4hzJp7U2es2Ooyrd_fTrs4VEGNOFq_on0wtSv5nM3pRXhsDgZYjW-wkyT-ctSst27RPkO6QxztmBn2bWg3BSngi3XAb1bIYxj2i9fIf9cCDZYi1kSPI-pO69AsVx_vlNoTWY7pI5BT1LOcbyD6BZVKzZ9v0IpI7Y330BA1NW0BRtlkg14VNyGKXdQ'
GROUP_ID = 178521119

# Авторизация в ВК
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

# Функция для отправки ответа
def send_reply(comment_id, owner_id, text):
    vk.wall.createComment(
        owner_id=-GROUP_ID,  # Минус перед ID группы для указания на стену сообщества
        post_id=owner_id,    # ID поста
        message=text,
        reply_to_comment=comment_id
    )

dt = ["Ваше открытие изменит учебники Политеха.",
"Не бойтесь ошибиться — Капица тоже начинал с малого.",
"Ваша идея станет гордостью лабораторий Политеха.",
"Ждите награду — Алферов тоже однажды ждал.",
"Ваш проект вдохновит целое поколение студентов.",
"Смело экспериментируйте — Политех это ценит.",
"Ваши разработки найдут применение в промышленности.",
"Каждая идея приближает вас к великому открытию.",
"Станьте новатором, как и первые выпускники Политеха.",
"Ваш труд заметят — Политех не забывает своих героев.",
"Не спешите, важное открытие требует времени.",
"Ваша теория станет основой новых исследований.",
"Работайте с увлечением — так рождаются легенды.",
"Ваше имя войдет в историю науки."]

# Основной цикл
for event in longpoll.listen():
    if event.type == VkBotEventType.WALL_REPLY_NEW:  # Отслеживаем новые комментарии
        comment = event.object
        text = comment['text']
        comment_id = comment['id']
        post_id = comment['post_id']

        # Проверяем, есть ли цифры
        if text.isdigit() and post_id == 8847:
            num = int(text)
            if 1<= num <= 14:
                send_reply(comment_id, post_id, dt[num-1])
