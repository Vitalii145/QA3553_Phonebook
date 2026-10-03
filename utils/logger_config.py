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

from datetime import datetime
from pathlib import Path
import logging
import colorlog
# def configure_logging():
#     logger = logging.getLogger(__name__)
#     if logger.handlers:
#         return logger
#     logger.setLevel(logging.INFO)
#     logger.propagate = False
#     console_handler = colorlog.StreamHandler()
#     console_formatter = colorlog.ColoredFormatter(
#         "%(log_color)s%(levelname)s: %(message)s",
#         force_color=True,
#         log_colors={
#             "DEBUG": "purple",
#             "INFO": "cyan",
#             "WARNING": "yellow",
#             "ERROR": "red",
#             "CRITICAL": "red,bg_white",
#         }
#     )
#     console_handler.setFormatter(console_formatter)
#     logger.addHandler(console_handler)
#     file_handler = logging.FileHandler("app.log", encoding="utf-8")
#     file_formatter = logging.Formatter("%(levelname)s: %(message)s")
#     file_handler.setFormatter(file_formatter)
#     logger.addHandler(file_handler)
#     return logger
#
#     logs_dir = Path(__file__).resolve().parents[1] / "logs"
#     logs_dir.mkdir(exist_ok=True)
#
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     log_path = logs_dir / f"test_{timestamp}.log"
#
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#
#     logging.getLogger("selenium").setLevel(logging.WARNING)
#
#     formatter = logging.Formatter(
#         "%(asctime)s-%(levelname)s-%(name)s-%(message)s"
#     )
#
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)
#     console_handler.setFormatter(formatter)
#
#     file_handler = logging.FileHandler(
#         log_path,
#         mode="w",
#         encoding="utf-8",
#     )
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(formatter)
#
#     logger.handlers.clear()
#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)

from datetime import datetime
import logging
from pathlib import Path
import colorlog

def configure_logging():
    logs_dir = Path(__file__).resolve().parents[1] / "logs"
    logs_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = logs_dir / f"test_{timestamp}.log"
    logger = logging.getLogger()
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logging.getLogger("selenium").setLevel(logging.WARNING)
    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = colorlog.ColoredFormatter(
        "%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
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
    file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s-%(levelname)s-%(name)s-%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger