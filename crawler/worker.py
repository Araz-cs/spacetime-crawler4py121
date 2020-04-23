from threading import Thread

from utils.download import download
from utils import get_logger
from scraper import scraper
import datetime
import time
from urllib.parse import urlparse

last_seen = dict()

class Worker(Thread):
    def __init__(self, worker_id, config, frontier):
        self.logger = get_logger(f"Worker-{worker_id}", "Worker")
        self.config = config
        self.frontier = frontier
        super().__init__(daemon=True)
        
    def run(self):
        while True:
            
            tbd_url = self.frontier.get_tbd_url()

            if not tbd_url:
                self.logger.info("Frontier is empty. Stopping Crawler.")
                break

            delta = datetime.timedelta(seconds=.5)
            split = urlparse(tbd_url).netloc.split('.')
            #extract domain from url (does not account for toay.blah./blah/blah/)
            domain = split[-3] + '.' + split[-2] + '.' + split[-1]
            print ("DOMAIN: " + domain)
            # if we've accessed tbd_url domain within 500ms then sleep
            #   sleep(500ms)
            if domain in last_seen and (datetime.datetime.now() - last_seen[domain] < delta):
                print ("====SLEEPING====")
                time.sleep(.5)
            # store tbh_url accessed at current time.
            last_seen[domain] = datetime.datetime.now()
        
            resp = download(tbd_url, self.config, self.logger)
            self.logger.info(
                f"Downloaded {tbd_url}, status <{resp.status}>, "
                f"using cache {self.config.cache_server}.")
            scraped_urls = scraper(tbd_url, resp)
            for scraped_url in scraped_urls:
                self.frontier.add_url(scraped_url)
            self.frontier.mark_url_complete(tbd_url)
            time.sleep(self.config.time_delay)
