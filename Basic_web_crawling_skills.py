# %%
# get query
import requests


content = input("请输入搜索内容：")
url = f"https://www.sogou.com/web?query={content}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 "
}
resp = requests.get(url, headers=headers)  # 发送请求
print(resp)
meta_data = resp.text  # 获取响应内容
# print(meta_data)
# print(resp.request.headers)  # 获取响应头
# requests.post(url) # 发送请求
file_path = "4_爬虫入门_下\\sogou.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(meta_data)
# %%post query
url = "https://fanyi.baidu.com/sug"
data = {
    "kw": "count"
}
res = requests.post(url, data=data)
print(res.text)
dic = res.json()
print(dic)
# %%
# more difficult
# 豆瓣电影評分 抓取電影
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 "
}
url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20"
res = requests.get(url, headers=headers)
print(res.text)
dic = res.json()
print(dic)

# %%
# more difficult 方案二：當他的參數（payload）太長的時候
# 查看完整的url
import requests
for i in range(8):  # 8頁，透過觀察douban的url，每當start增加20，就會換下一頁 所以每20做一次迴圈
    start = i = i * 20
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 "
    }
    dic = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": start,
        "limit": "20"
    }
    # params 會自動幫你把字典轉換成query string
    res = requests.get(url, headers=headers, params=dic)
    dic = res.json()# 透過json()轉換成字典
    dic = list(dic)
    print(type(dic))  # Convert dic to a list
    print(dic)
    # print(res.request.url) # 查看完整的url
    count = 0
    for item in dic:
        information = item["title"], item["score"], item["cover_url"]
        print(information)  # 取出電影名稱、評分、封面圖片
        count += 1
        itemURL = item["cover_url"]
        nowItem = item["title"]
        res = requests.get(itemURL)
        if item == item["title"][0]:
            with open(f"{nowItem}.jpg", "wb") as f:
                f.write(res.content)
    print(count)
# %%
# 獲取圖片
url = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p771490367.jpg"
res = requests.get(url)
print(res.content)
with open("爬圖片.jpg", "wb") as f:
    f.write(res.content)

# %%
