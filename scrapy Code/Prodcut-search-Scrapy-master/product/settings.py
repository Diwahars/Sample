# Scrapy settings for product project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'product'

SPIDER_MODULES = ['product.spiders']
NEWSPIDER_MODULE = 'product.spiders'

ITEM_PIPELINES = ['product.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "ecommerce"
MONGODB_COLLECTION = "product"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'product (+http://www.yourdomain.com)'
