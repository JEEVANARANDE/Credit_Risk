import logging
import os
def get_logger(filename, log_dir='logs'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    f = logging.Formatter("[%(asctime)s: - %(levelname)s: %(lineno)d:] - %(filename)s - %(message)s",datefmt='%d-%m-%Y %I:%M:%S %p')#- %(pathname)s: ,f = logging.Formatter("[%(asctime)s: - %(name)s: - %(levelname)s: - %(pathname)s - %(module)s:] - %(filename)s - %(message)s")#
    filename = '{}.log'.format(os.path.basename(filename).split('.py')[0])
    os.makedirs(log_dir,exist_ok=True) 
    fh = logging.FileHandler(filename=os.path.join(log_dir,filename),mode="w")
    fh.setFormatter(f)
    logger.addHandler(fh)
    return logger
