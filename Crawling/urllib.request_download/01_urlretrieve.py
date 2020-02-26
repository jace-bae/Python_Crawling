import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 원하는 이미지를 다운로드
imgURL = "http://post.phinf.naver.net/MjAxNzExMjZfMjM0/MDAxNTExNzA3ODY5MzI2.BMO-NoJUSlwN_-3y2qyEOPv6Wp9JIqcT5Qqj_C7i0Gsg.X-Jkr7_Dvn6J0VEudl5g-FwnShqTbVg2vES997CQaI4g.JPEG/Imr6VJjIVDTIBDPyyNx4Tkyt0yIo.jpg"
htmlURL = "http://google.com"

savePath1 = "E://test1.jpg"
savePath2 = "E://index.html"

# urllib.request.urlretrieve(url, savename)
dw.urlretrieve(imgURL, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("download pass")
