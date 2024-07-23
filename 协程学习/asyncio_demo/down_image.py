import time
import requests
import asyncio
import aiohttp


def func1(url: str):
    print("开始下载图片")
    response = requests.get(url)
    print("下载完成")
    file_name = url.rsplit("%")[-1]
    with open(file_name, mode="wb") as file_obj:
        file_obj.write(response.content)


async def func2(session, url):
    print("开始下载图片")
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit("%")[-1]
        with open(file_name, mode="wb") as file_obj:
            file_obj.write(content)


async def fetch(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(func2(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == "__main__":
    url_list = [
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1605334109373&di=1b8ef4662e7df303cae3d184b35d8e55&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F30%2F29%2F01300000201438121627296084016.jpg",
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1605334109372&di=ee8c7258dc470df5307849f07b7b2f6a&imgtype=0&src=http%3A%2F%2Fa3.att.hudong.com%2F55%2F22%2F20300000929429130630222900050.jpg",
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1605334109372&di=06e6858b27323d0e45e50036f44efb59&imgtype=0&src=http%3A%2F%2Fa1.att.hudong.com%2F05%2F00%2F01300000194285122188000535877.jpg"]
    start_time = time.time()
    # asyncio.get_event_loop().run_until_complete(fetch(url_list))
    for i in url_list:
        func1(i)
    end_time = time.time() - start_time
    print(end_time)

