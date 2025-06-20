from datetime import  datetime


def get_unique_name():
    return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

