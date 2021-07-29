# LECTION

# Логирование
#
# Всегда полезно знать что происходило с нашей программой в процессе выполнения
# Это осуществляется с помощью стандартной библиотеки логирования

# Существует 5 уровней логирования

# DEBUG 	Детальная информация, интересная только при отладке
#
# INFO 	    Подтверждение, что все работает как надо
#
# WARNING 	Индикация того, что что-то пошло не так, и возможны проблемы в будущем
#           (заканчивается место на диске, етс)
#           Программа продолжает работать как надо.
#
# ERROR 	Относительно серьезная проблема, программа не смогла выполнить некоторый функционал.
#
# CRITICAL 	Реально серьезная проблема, программа не может работать дальше.
#
# Уровень WARNING стоит по умолчанию.

# import logging


# def fibonacci(n):
#     f_0 = 0
#     f_1 = 1
#     for i in range(n):

#         logging.debug(f"{f_0}, {f_1} = {f_1}, {f_0+f_1}")
#         yield f_0
#         f_0, f_1 = f_1, f_0 + f_1
        


# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG, filename='data\\fib.log')
# logging.basicConfig(
#     level=logging.INFO,
#     handlers=[logging.FileHandler('data\\fib.log', 'w', 'utf-8')],
# )

# i = 0
# for number in fibonacci(10):
#     logging.info(f"get fibonacci ({i}) = {number}")
#     i += 1


## Логирование ошибок

# def division(x):
#     return x / 0


# logging.basicConfig(filename='data\\errors.log', level=logging.INFO, filemode="w")

# number = 2
# try:
#     logging.info('try')
#     division(number)
# except Exception:
#     logging.exception(f'Error with {number}')

## Конфигурация для объектов логирования

# info_logger = logging.getLogger('info_logger')
# info_logger.setLevel(logging.INFO)
# fh = logging.FileHandler("data\\info_logger.log", 'w', 'utf-8')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# info_logger.addHandler(fh)


# debug_logger = logging.getLogger('debug_logger')
# debug_logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler("data\\debug_logger.log", 'w', 'utf-8')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# debug_logger.addHandler(fh)


# def fibonacci(n):
#     f_0 = 0
#     f_1 = 1
#     for i in range(n):

#         debug_logger.debug(f"{f_0}, {f_1} = {f_1}, {f_0+f_1}")
#         yield f_0
#         f_0, f_1 = f_1, f_0 + f_1
        
# i = 0
# for number in fibonacci(10):
#     info_logger.info(f"get fibonacci ({i}) = {number}")
#     i += 1




## json configuration

# import logging
# import logging.config

# log_config = {
#     "version": 1,
#     "formatters": {
#         "my_formatter": {
#             "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#         },
#     },
#     "handlers": {
#         "file_handler": {
#             "class": "logging.FileHandler",
#             "formatter": "my_formatter",
#             "filename": "data\\from_json.log",
#             "mode":"w"
#         },
#         "cmd_handler": {
#             "class": "logging.StreamHandler",
#             "formatter": "my_formatter"
#         },
#     },
#     "loggers": {
#         "info_log": {
#             "handlers": ["file_handler", "cmd_handler"],
#             "level": "INFO",
#         }
#     },
# }


# logging.config.dictConfig(log_config)
# log = logging.getLogger('info_log')

# def fibonacci(n):
#     f_0 = 0
#     f_1 = 1
#     for i in range(n):

#         log.debug(f"{f_0}, {f_1} = {f_1}, {f_0+f_1}")
#         yield f_0
#         f_0, f_1 = f_1, f_0 + f_1
       
# i = 0
# for number in fibonacci(10):
#     log.info(f"get fibonacci ({i}) = {number}")
#     i += 1

# print(help(logging))


# PRACTICE

# Для функции, считающей факториал числа добавить логирование DEBUG 
# после каждой операции в цикле(или в шаге рекурсии) с промежуточными результатами.

# Посчитать факториалы 5 различных чисел. Добавить логирование в режиме INFO для каждого результата.

# Конфигурацию для логирования загрузить из  js файла, который нужно создать.

# DEBUG пишет в файл, INFO пишет в другой файл и на консоль