import json
import re
import requests
import logging

"""
128mp3 M500 88
320mp3 M800 53
flac   F000 91
m4a    C400 66

"""
header = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
}
def search(word, page=1):
    _api = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?n=20&w=" + word + "&p=" + str(page)
    _data = requests.get(_api).text[9:-1]
    print(_data)
    _data = json.loads(_data)
    if _data["code"] != 0:
        logging.error("code: {} message: {}".format(_data["code"], _data["message"]))

def get_vkey(song_mid):
    _api = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?format=json" + \
            "&cid=205361747&uin=0&songmid={0}&filename=C400{0}.m4a&guid=3655047200"
    _url = _api.format(song_mid)
    _res = requests.get(_url, headers=header).json()
    return _res["data"]["items"][0]["vkey"]

def download_url(song_mid, formate="320"):
    formate = str(formate)
    formation = {
        "m4a": {"name": "m4a", "pre": "C400", "tag": 66},
        "128": {"name": "mp3", "pre": "M500", "tag": 88},
        "320": {"name": "mp3", "pre": "M800", "tag": 53},
        "flac": {"name": "flac", "pre": "F000", "tag": 91},
    }
    _d = formation[formate]
    _api = "http://dl.stream.qqmusic.qq.com/{}{}.{}?vkey={}&guid=3655047200&uin=0&fromtag={}"
    return _api.format(_d["pre"], song_mid, _d["name"], get_vkey(song_mid), _d["tag"])
    
if __name__ == "__main__":
    mid = "0032PwI41C08mk"
    url = download_url(mid, formate="flac")
    # t_url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?format=json&cid=205361747&uin=0&songmid=0032PwI41C08mk&filename=C4000032PwI41C08mk.m4a&guid=3655047200"
    # res = requests.get(t_url).json()
    # vkey = res["data"]["items"][0]["vkey"]
    # url = "http://dl.stream.qqmusic.qq.com/M8000032PwI41C08mk.mp3?vkey={}&guid=3655047200&uin=0&fromtag=53".format(vkey)
    print(url)
    # a = requests.get(url, headers=header).content
    # open("D:/a.mp3", "wb").write(a)

