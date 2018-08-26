## Youtube api for stikpro
Библиотека для работы с API YouTube. Сделано для скрапера YouTube.

**Зависимости:**
* `apiclient`

**Содержит функции:**
* `parse_channel_id` - принимает на вход URL канала, возвращает айди канала для работы библиотеки
* `het_channel_info` - принимает на вход ID канала, возвращает информацию о канале:
 ```json
 {
  "title": "Имя канала",
  "description": "Описание канала",
  "customUrl": "Приставка к юрл",
  "published": "Дата открытия канала",
  "imgUrl": "URL изображения канала",
  "county": "Страна канала",
  "statistics": {
    "followers": "Кол-во подписчиков",
    "views": "Общее кол-во просмотров",
    "videoCount": "Кол-во видео на канале"
  }
 }
 ```
 * `get channel_playlists` - принимает на вход ID канала, возвращает список ID плейлистов канала
 * `get_videos_from_playlist` - принимает на вход ID плейлиста, возвращает список с информацией о каждом видео:
 ```json
 {
  "title": "Имя видео",
  "description": "Описание видео",
  "imgUrl": "Обложка видео",
  "tags": "Список тегов видео",
  "defaultAudioLanguage": "Язык стандартной аудиодорожки",
  "statistics": {
    "viewCount": "Кол-во просмотров",
    "likeCount": "Кол-во лайков",
    "dislikeCount": "Кол-во дизлайков",
    "commentCount": "Кол-во комментариев"
  }
 }
 ```
 
 **Пример использования:**
 ```python
from lib import YoutubeAPI

# Инициализация апи. В аргументы передается developer key
yc = YoutubeAPI('AIzaSyAD2ggZZwCyYSvz4tpg4pFK9FCPTncPos4')

# Получение ID канала
ch_id = yc.parse_channel_id('https://www.youtube.com/channel/UCvKPc71Dd8qnuKZd2nRyH4g')

# Получение списка плейлистов канала
a = yc.get_channel_playlists(ch_id=ch_id)

# Создание списка, проход по всем плейлистам и добавление в список информации о видео
v = []
for e in a:
    v.append(list(yc.get_videos_from_playlist(pl_id=e, max_results=50)))

# Сбор структуры
data = {
    "ch_info": yc.get_channel_info(ch_id),
    "videos_info": v
}
