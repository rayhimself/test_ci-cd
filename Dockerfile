FROM python:3.8
RUN pip install requests BeautifulSoup4
COPY . /
CMD python browser.py
