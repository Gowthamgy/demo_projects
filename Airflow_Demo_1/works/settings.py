BOT_NAME = 'works'

SPIDER_MODULES = ['works.spiders']
NEWSPIDER_MODULE = 'works.spiders'

# Example pipeline import
ITEM_PIPELINES = {
    'works.pipelines.MySQLPipeline': 300,
}
