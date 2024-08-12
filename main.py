import logging

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename='info.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logger.info('Started')
    do_something()
    logger.info('Finished')

def do_something():
    logger.info('Doing something')

if __name__ == '__main__':
    main()