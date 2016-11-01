# coding: utf8
from django.core.management.base import BaseCommand
from parse_app.models import Parts
from BeautifulSoup import BeautifulSoup
import time
from selenium import webdriver
from parse_table import settings
import os


class Command(BaseCommand):
    help = 'Parse and save data from table in "http://avtoparts.com.ua/Search/ComponentsByCategory?category=39"'

    def handle(self, *args, **options):
        driver = webdriver.PhantomJS(executable_path=os.path.join(settings.BASE_DIR,'phantomjs'))
        driver.set_window_size(1120, 550)
        driver.get('http://avtoparts.com.ua/Search/ComponentsByCategory?category=39')

        elem1 = driver.find_element_by_class_name('moreComponents')
        while elem1.text == 'Ещё результаты'.decode('utf-8'):
            elem1.click()

        time.sleep(20)
        soup = BeautifulSoup(driver.page_source)
        table = soup.find('table')
        rows = table.findAll('tr')

        data = []
        for row in rows[1:]:
            cols = row.findAll('td')[:5] + row.findAll('td')[6:9]
            cols1 = [ele.text.strip() for ele in cols]
            cols1[3] = cols1[3].replace('&gt;5', '5 +')
            data.append([i for i in cols1])

        for i in data:
            Parts.objects.get_or_create(code_text=i[0],
                                        name_text=i[1],
                                        brand_text=i[2],
                                        number_stock=i[3],
                                        number_reserve=i[4],
                                        price_float=i[5],
                                        price_discount=i[6],
                                        note_text=i[6],
                                        )
