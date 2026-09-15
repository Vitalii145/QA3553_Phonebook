# import logging
# import colorlog
# def configure_logging():
#     logging.basicConfig(
#         level=logging.INFO,
#         format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         # filename="test.log",
#         # filemode="w"
#
#     )


import logging
import colorlog
def configure_logging():
    logger = logging.getLogger(__name__)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    console_handler = colorlog.StreamHandler()
    console_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s: %(message)s",
        force_color=True,
        log_colors={
            "DEBUG": "purple",
            "INFO": "cyan",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        }
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_formatter = logging.Formatter("%(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger