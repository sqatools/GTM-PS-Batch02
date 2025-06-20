import logging

logging.basicConfig(
    filename="excecution.log",
    level=logging.INFO,
    filemode='a',
    format="%(asctime)s - %(filename)s- %(lineno)s- %(name)s-'%(levelname)s -%(message)s'"
)

logger = logging.getLogger()
