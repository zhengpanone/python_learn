#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :sampletest_v6.py
@说明    :下载基云惠康json文件脚本，更新信息为增加--outdir参数用于指定存储文件位置信息
@时间    :2020/07/03 14:11:35
@作者    :李双双
@版本    :6.0
'''

import time
import time
import requests
from hashlib import md5
from base64 import b64encode
import json
import sys
import os
import pathlib
import argparse
import aiohttp
import asyncio

appId = 'mpdxb4gqnlmq9yg'
appSecret = 'a8fxf5jxd61qvatavdn199ljr'

latestURL = 'https://api.genekang.com/version1'
oldURL = 'https://api.genekang.com/v2'

parser = argparse.ArgumentParser()
parser.add_argument('--code', metavar='FILE', type=str, help='Required')
parser.add_argument('--outdir', metavar='FILE', type=str)
args = parser.parse_args()

code = args.code
outdir = args.outdir
# os.mkdir(code)
output = os.path.join(outdir, code)
pathlib.Path(output).mkdir(parents=True, exist_ok=True)


def getSign():
    ts = str(time.time())[:10]
    sumsign = appId + appSecret + ts
    sign = md5(sumsign.encode()).hexdigest().upper()
    sumauth = appId + ':' + ts
    auth = b64encode(sumauth.encode()).decode()
    head = {"Authorization-Str": auth}
    return sign, head


async def getInfo(session, name):
    sign, head = getSign()
    out = output + f'/{name}/'
    # os.mkdir(out)
    pathlib.Path(out).mkdir(parents=True, exist_ok=True)
    # requests.adapters.DEFAULT_RETRIES = 5
    url = latestURL + f'/{name}-report?sign={sign}&scode={code}'
    async with session.get(url, verify_ssl=False, headers=head) as response:

        getjs = await response.content
        print(getjs)

    # getjs = requests.get(
    #     latestURL + f'/{name}-report?sign={sign}&scode={code}', headers=head).json()
        getjs_ = getjs if name != 'inherit' else getjs['diseases']
        with open(out + f'{name}-report.json', 'w', encoding="utf-8") as nrf:
            json.dump(getjs_, nrf, ensure_ascii=False)

        for i in getjs_:
            item = i['itemid']
            url = latestURL + f'/{name}-item?sign={sign}&scode={code}&itemid={item}'
            async with session.get(url, verify_ssl=False, headers=head) as response:
                js = await response.content.json()

                with open(out + f'{name}-item.{item}.json', 'w') as nif:
                    json.dump(js, nif, ensure_ascii=False)

                _name = 'drug' if name == 'guideline-drug' else name

                js = requests.get(
                    latestURL + f'/{_name}-info?sign={sign}&scode={code}&itemid={item}', headers=head).json()
                with open(out + f'{_name}-info.{item}.json', 'w', encoding="utf-8") as nif:
                    json.dump(js, nif, ensure_ascii=False)

                if name == 'tumour':
                    name_ = 'disease'
                # elif name == 'guideline-drug':
                #    continue
                else:
                    name_ = name
                js = requests.get(
                    latestURL + f'/{name_}-gene?sign={sign}&scode={code}&itemid={item}', headers=head).json()
                with open(out + f'{name_}-gene.{item}.json', 'w', encoding="utf-8") as ngf:
                    json.dump(js, ngf, ensure_ascii=False)
                if name == 'disease':
                    js = requests.get(
                        latestURL + f'/reference-item?sign={sign}&scode={code}&itemid={item}', headers=head).json()
                    with open(out + f'reference-item.{item}.json', 'w', encoding="utf-8") as rif:
                        json.dump(js, rif, ensure_ascii=False)
                if name == 'tumor':
                    name = 'disease'
                    js = requests.get(
                        latestURL + f'/reference-item?sign={sign}&scode={code}&itemid={item}', headers=head).json()
                    with open(out + f'reference-item.{item}.json', 'w', encoding="utf-8") as rif:
                        json.dump(js, rif, ensure_ascii=False)


def getIH(name):
    sign, head = getSign()
    out = output + f'/{name}/'
    # os.mkdir(out)
    pathlib.Path(out).mkdir(parents=True, exist_ok=True)
    requests.adapters.DEFAULT_RETRIES = 5
    getjs = requests.get(
        latestURL + f'/{name}-report?sign={sign}&scode={code}&page_size=5000', headers=head).json()
    getjs_ = getjs['diseases']
    with open(out + f'{name}-report.json', 'w') as nrf:
        json.dump(getjs_, nrf, ensure_ascii=False)

    for i in getjs_:
        item = i['itemid']
        js = requests.get(
            latestURL + f'/{name}-item?sign={sign}&scode={code}&itemid={item}', headers=head).json()
        with open(out + f'{name}-item.{item}.json', 'w') as nif:
            json.dump(js, nif, ensure_ascii=False)

        _name = 'drug' if name == 'guideline-drug' else name
        js = requests.get(
            latestURL + f'/{_name}-info?sign={sign}&scode={code}&itemid={item}', headers=head).json()
        with open(out + f'{_name}-info.{item}.json', 'w') as nif:
            json.dump(js, nif, ensure_ascii=False)

        if name == 'tumour':
            name_ = 'disease'
        elif name == 'guideline-drug':
            continue
        else:
            name_ = name
        js = requests.get(
            latestURL + f'/{name_}-gene?sign={sign}&scode={code}&itemid={item}', headers=head).json()
        with open(out + f'{name_}-gene.{item}.json', 'w') as ngf:
            json.dump(js, ngf, ensure_ascii=False)
        if name == 'disease':
            js = requests.get(
                latestURL + f'/reference-item?sign={sign}&scode={code}&itemid={item}', headers=head).json()
            with open(out + f'reference-item.{item}.json', 'w') as rif:
                json.dump(js, rif, ensure_ascii=False)


def getreference(name):
    sign, head = getSign()
    out = output + f'/{name}/'
    requests.adapters.DEFAULT_RETRIES = 5
    getjs = requests.get(
        latestURL + f'/{name}-report?sign={sign}&scode={code}', headers=head).json()
    for i in getjs:
        item = i['itemid']
        if name == 'tumour':
            name = 'disease'
        js = requests.get(
            latestURL + f'/reference-item?sign={sign}&scode={code}&itemid={item}', headers=head).json()
        with open(out + f'reference-item.{item}.json', 'w') as rif:
            json.dump(js, rif, ensure_ascii=False)

async def main():

    # 样本疾病
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(getInfo(session,"disease"))]
        # getInfo(session,'disease')
        await asyncio.wait(tasks)
if __name__ == '__main__':

    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    print(time.time() - start_time)