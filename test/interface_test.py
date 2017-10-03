#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Meng xiangguo <mxgnene01@gmail.com>
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                        2017/10/3  下午4:40

import requests
import unittest


class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list'

    def test_get_event_null(self):
        '''发布会ID为空'''
        r = requests.get(self.url, params={'eid': ''})
        result = r.json()
        # print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_success(self):
        '''发布会 id 为 1，查询成功'''

        r = requests.get(self.url, params={'eid': '1'})
        result = r.json()
        # print(result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['data']['name'], "达令上市")
        self.assertEqual(result['data']['address'], "国家会议中心")
        self.assertEqual(result['data']['start_time'], "2019-09-29T10:09:20Z")


if __name__ == '__main__':
    unittest.main()