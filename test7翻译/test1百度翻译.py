"""
使用百度翻译平台api
网址：https://fanyi-api.baidu.com/api/trans/product/desktop?req=detail&login_type=weixin
前往平台开启翻译
"""
import time

import requests
import hashlib
import random
import json


class BaiduTranslator:
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    langs = ['zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra', 'spa', 'th', 'ara',
             'ru', 'pt', 'de', 'it', 'el', 'nl', 'pl', 'bul', 'est', 'dan',
             'fin', 'cs', 'rom', 'slo', 'swe', 'hu', 'cht', 'vie']
    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    def __init__(self, appId, secretKey,rate):
        """
        :param appId: id
        :param secretKey: key
        :param rate: 翻译速度，rate个/s
        """
        self.appId = appId
        self.secretKey = secretKey
        self.rate = rate

    def _detectLang(self, lang) -> bool:
        """检查lang的合法性"""
        if lang in self.langs:
            return True
        else:
            return False

    def _consolidate(self, query, toLang: str, fromLang: str = 'auto') -> dict:
        """拼包"""
        if not self._detectLang(toLang):
            raise ValueError("目标语种错误")
        salt = str(random.randint(32768, 65536))
        sign = self.appId + query + salt + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        payload = {
            'q': query,
            'from': fromLang,
            'to': toLang,
            'appid': self.appId,
            'salt': salt,
            'sign': sign
        }
        return payload

    def translate(self, query, toLang: str, fromLang: str = 'auto'):
        """翻译一段"""
        payload = self._consolidate(query, toLang, fromLang)
        try:
            response = requests.post(self.url, data=payload, headers=self.headers)
            result = json.loads(response.text)
            if 'trans_result' in result:
                return result['trans_result'][0]['dst']
            else:
                return result['error_msg'] + " " + result['error_code']
        except Exception as e:
            print(f"请求错误: {e}")
            raise ValueError("因网络或账户问题翻译失败")
        finally:
            time.sleep(1/self.rate)


if __name__ == '__main__':
    aid = '20240508002045378'
    key = 'nDWuwx0XqnEZuiGfIgEW'
    r = 1
    translator = BaiduTranslator(aid, key,r)
    print(translator.translate(r"XVIII", "zh"))
