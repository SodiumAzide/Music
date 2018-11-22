"""
http://songsearch.kugou.com/song_search_v2?callback=jQuery112408853652784417396_1542814807649&keyword=claris&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1542814807651
https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=
"""
import requests 

def search(word):
    _api = "http://songsearch.kugou.com/song_search_v2?keyword={}&pagesize=30&page=".format(word)
    data = requests.get(_api).json()
    _return = []
    for _ in data["data"]["lists"]:
        name = _["FileName"].replace("<em>").replace("</em>")
        if _["HQPayType"] == 0:
            _return.append({"name": name, "hash": _["HQFileHash"], "format": "320"})
        else:
            _return.append({"name": name, "hash": _["FileHash"], "format": "128"})

def download_url(song_mid, formate=None):
    return "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=" + song_mid
