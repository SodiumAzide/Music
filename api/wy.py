"""
http://music.163.com/api/song/enhance/download/url?br=320000&id=28445467
"""
import requests

def download_url(song_mid, formate=320):
    _api = "http://music.163.com/api/song/enhance/download/url?br={}&id={}"
    res = requests.get(_api.format(formate * 1000, song_mid)).json()
    _url = res["data"]["url"]
    if _url is None:
        return "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_mid)
    return _url


if __name__ == "__main__":
    url = download_url(851062)
    print(url)
