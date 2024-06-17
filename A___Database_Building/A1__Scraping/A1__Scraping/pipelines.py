import csv, os
from scrapy.exporters import CsvItemExporter
from A1__Scraping.items import Pokemon

class CsvPipeline:
    def open_spider(self, spider):
        file_name = 'pokemon_data.csv'
        if not os.path.exists(file_name):
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Number', 'Name'])

        self.file = open(file_name, 'a', newline='')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, Pokemon):
            self.exporter.export_item(item)
        
        return item
