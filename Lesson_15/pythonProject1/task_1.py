# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
logger = logging.getLogger()

handler_debug = logging.FileHandler('debug_info.log')
handler_debug.setLevel(logging.DEBUG)
logger.addHandler(handler_debug)
logger.debug("Debug message")

handler_warning = logging.FileHandler('warnings_errors.log')
handler_warning.setLevel(logging.WARNING)
logger.addHandler(handler_warning)
logger.warning("Warning message")



