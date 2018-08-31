from apiclient.discovery import build


class YoutubeAPI:

    DEVELOPER_KEY: str = None
    YOUTUBE_API_SERVICE_NAME: str = None
    YOUTUBE_API_VERSION: str = None

    api_client = None

    def __init__(self, dev_key: str):
        self.DEVELOPER_KEY = dev_key
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3'
        try:
            self.api_client = \
                build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=self.DEVELOPER_KEY)
        except Exception as e:
            print('Failed build youtube api client: {}'.format(e))

    @staticmethod
    def parse_channel_id(api_client_arg, channel_link: str) -> str or None:
        if channel_link.count('/user/') != 0:
            result = api_client_arg.api_client.channels().list(part='snippet,contentDetails,statistics', forUsername=channel_link[channel_link.find('user/') + 5:]).execute()
            return result.get('items')[0].get('id')
        id_pos: int = channel_link.find('channel/')
        if id_pos == -1:
            return None
        return channel_link[id_pos + 8:]

    def get_channel_info(self, ch_id: str) -> dict or None:
        try:
            result: dict = self.api_client.channels().list(part='snippet,contentDetails,statistics', id=ch_id) \
                .execute().get('items')[0]
            ch_snippet = result.get('snippet')
            ch_stat = result.get('statistics')
        except Exception as e:
            print('Failed to collect channel info: {}'.format(e))
            return None
        return {
            "title": ch_snippet.get('title'),
            "description": ch_snippet.get('description'),
            "customUrl": ch_snippet.get('customUrl'),
            "published": ch_snippet.get('publishedAt')[: 10],
            "imgUrl": ch_snippet.get('thumbnails').get('default').get('url'),
            "country": ch_snippet.get('country'),
            "statistics": {
                "followers": ch_stat.get('subscriberCount'),
                "views": ch_stat.get('viewCount'),
                "videoCount": ch_stat.get('videoCount')
            }
        }

    def get_channel_playlists(self, ch_id: str, max_results: int = 25) -> list or None:
        try:
            result: dict = self.api_client.playlists().\
                list(part='snippet,contentDetails', channelId=ch_id, maxResults=max_results).execute()
        except Exception as e:
            print('Failed to collect channel playlists: {}'.format(e))
            return None
        return list(map(lambda x: x.get('id'), result.get('items')))

    def get_videos_from_playlist(self, pl_id: str, max_results: int = 25, next_page_token: str = None) -> list:
        try:
            result: dict = self.api_client.playlistItems() \
                .list(part='snippet,contentDetails', maxResults=max_results, playlistId=pl_id, pageToken=next_page_token).execute()
        except Exception as e:
            print('Failed to collect playlists item info: {}'.format(e))
            return []

        def map_callback(video):
            try:
                video_info: dict = self.api_client.videos() \
                    .list(part='snippet,contentDetails,statistics', id=video.get('contentDetails').get('videoId')) \
                    .execute().get('items')[0]
                video_snippet = video_info.get('snippet')
                video_statistics = video_info.get('statistics')
            except Exception as e:
                print('Failed to collect video info: {}'.format(e))
                return None
            return {
                "title": video_snippet.get('title'),
                "description": video_snippet.get('description'),
                "imgUrl": video_snippet.get('thumbnails').get('default').get('url'),
                "tags": video_snippet.get('tags'),
                "defaultAudioLanguage": video_info.get('defaultAudioLanguage'),
                "video_id": video_info.get('id'),
                "statistics": {
                    "viewCount": video_statistics.get('viewCount'),
                    "likeCount": video_statistics.get('likeCount'),
                    "dislikeCount": video_statistics.get('dislikeCount'),
                    "commentCount": video_statistics.get('commentCount')
                }
            }

        return map(map_callback, result.get('items')), result.get('nextPageToken')

