import logging
import colorlog


class Logger:
    @staticmethod
    def setup():
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s] %(levelname)-8s: %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red",
            },
        )

        # Console handler
        ch = colorlog.StreamHandler()
        ch.setFormatter(formatter)

        # File handler
        fh = logging.FileHandler("ud.log")
        fh.setFormatter(formatter)

        logger = colorlog.getLogger()
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)
