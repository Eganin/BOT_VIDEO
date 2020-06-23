from collections import defaultdict


def handler_data_user(data: list) -> dict:
    '''Группировка данных пользователя'''
    hash = defaultdict(list)
    for line in data:
        id, video_text, user_id = line
        hash[user_id].append(video_text)

    return hash
