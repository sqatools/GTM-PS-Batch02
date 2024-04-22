import logging


#logging.info("Welcome to test cases execution")
#logging.warning("This test cases may be failed due provide value")
#logging.debug("Debug code to find the failures")
#logging.error("link is not working")
#logging.critical("Login is not working")
#logging.info("execution successful")

logging.basicConfig(
    filename="execution.log",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s - %(filename)s- %(lineno)s- %(name)s-'%(levelname)s -%(message)s'"
)

logger= logging.getLogger()

logger.info("Welcome to logging module")
