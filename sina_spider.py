#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import logging
import re

class CoupletSpider(scrapy.Spider):
    name = 'CoupletSpider'
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1195052695_2_%d.html' % (i) for i in range(1, 20)]


    def parse(self, response):
        for href in response.css('.atc_title a ::attr(href)'):
            yield response.follow(href.extract(), self.parse_couplets)


    def parse_couplets(self, response):
        title = response.css('.articalTitle h2 ::text').extract_first()
        lines = response.css('.articalContent::text, .articalContent *::text').extract()
        output_file = open('output/' + title + '.txt', 'w')
        mid = u'〓'
        end = u'◎'
        for line in lines:
            if (not mid in line) or (not end in line):
                continue
            line = line.replace(end, '').replace('|', '')
            words = re.split(ur"[\u200b\s]+", line, flags=re.UNICODE)
            for word in words:
                if len(word.strip()) == 0:
                    continue
                couplet = word.split(mid)
                if len(couplet) != 2:
                    logging.warning("Error while process " + word)
                    continue
                up, down = couplet
                if (not up) or (not down) or len(up) != len(down):
                    logging.warning("Error while process " + word)
                    continue
                output_file.write((up + u'\n').encode('utf8'))
                output_file.write((down + u'\n').encode('utf8'))
        output_file.close()

