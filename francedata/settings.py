# -*- coding: utf-8 -*-

# Scrapy settings for francedata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'francedata'

SPIDER_MODULES = ['francedata.spiders']
NEWSPIDER_MODULE = 'francedata.spiders'

DUPEFILTER_CLASS = 'francedata.filters.URLScreenFilter'
LOG_LEVEL = 'INFO'
TELNETCONSOLE_ENABLED = False
