import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name,"wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","https://rpic.douyucdn.cn/asrpic/180921/4699574_5090062_014cd_2_0905.jpg")
    ])


if __name__ == "__main__":
    main()

    