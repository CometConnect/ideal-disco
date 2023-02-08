from selenium import webdriver
from bs4 import BeautifulSoup
from bs4.element import PageElement
from pandas import DataFrame
from dataclasses import dataclass


def __parse(element: PageElement) -> str:
    return element.get_text().strip()


def __strip(target: list) -> list:
    out = []
    for v in target:
        if v != '\n':
            out.append(v)
    return out


def __init(url: str) -> BeautifulSoup:
    browser = webdriver.Chrome("D:/setup/chromedriver_win32/chromedriver.exe")
    browser.get(f"https://en.wikipedia.org/wiki/{'_'.join(url.split(' '))}")
    return BeautifulSoup(browser.page_source, "html.parser")


def __save(data: list, filename: str):
    DataFrame(data, columns=list(filter(
        lambda x: not x.startswith('__'),
        dir(data[0])
    ))).to_csv(f"{filename}.csv")


def table1():
    @dataclass
    class Data:
        apparent_magnitude: str
        name: str
        bayer_designation: str
        distance: str
        spectral_class: str
        mass: str
        radius: str
        luminosity: str

    soup = __init("List of brightest stars and other record stars")
    rows = __strip(list(soup.find('tbody').children))
    data = []
    for item in rows:
        res = __strip(list(item.children))

        try:
            data.append(Data(
                __parse(res[0]),
                __parse(res[1].find('a')),
                __parse(res[2]),
                __parse(res[3]),
                __parse(res[4]),
                __parse(res[5]),
                __parse(res[6]),
                __parse(res[7])
            ))
        except:
            pass

        __save(data, "table1")


def table2():
    @dataclass
    class Data:
        name: str
        constellation: str
        right_ascension: str
        declination: str
        distance: str
        spectral_type: str
        mass: str
        radius: str
        discovery_year: str

    soup = __init("List of brown dwarfs")
    rows = __strip(list(soup.find_all('tbody')[7].children))
    data = []

    for item in rows:
        res = __strip(list(item.children))

        try:
            data.append(Data(
                __parse(res[0].find('a')),
                __parse(res[1].find('a')),
                __parse(res[2]),
                __parse(res[3]),
                __parse(res[4]),
                __parse(res[5]),
                __parse(res[6]),
                __parse(res[7]),
                __parse(res[8])
            ))
        except:
            pass

        __save(data, "table2")
