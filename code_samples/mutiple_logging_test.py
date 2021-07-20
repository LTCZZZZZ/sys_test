# 输出多个日志文件

import logging


def get_logger(logger_name, log_file, level=logging.INFO):
    fileHandler = logging.FileHandler(log_file, mode='a')
    # 下面两行可以注释掉
    formatter = logging.Formatter('%(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
    fileHandler.setFormatter(formatter)

    vlog = logging.getLogger(logger_name)
    vlog.setLevel(level)
    vlog.addHandler(fileHandler)

    return vlog


if __name__ == '__main__':
    log_file1 = 'logger_test1.log'
    log_file2 = 'logger_test2.log'

    logger1 = get_logger('one', log_file1)
    logger2 = get_logger('two', log_file2)

    logger1.info('>>> test1 log msg: %s', "111111111111111111111")
    logger2.info('>>> test2 log msg: %s', "222222222222222222222")
