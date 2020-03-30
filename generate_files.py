import os
import random
import csv
from datetime import datetime
import logging

logger = logging.getLogger(__file__)


class GenerateFile:
    def __init__(self, file_name, file_size):
        if os.path.isfile(file_name):
            logger.info(f'File {file_name} exist')
            return

        logger.info(f'Generating file {file_name}')

        line_length = 64

        lines_to_generate = int(self.size(file_size) / line_length)

        d = {
            # 2 bytes from new line and 2 bytes for two commas that separates columns
            'user_id': None,  # 16 bytes
            'date': None,  # 8 bytes
            'value': ''.join(str(random.randint(0, 9)) for x in range(36)),  # 64 - 2 - 2 - 16 - 8 = 36
        }

        with open(file_name, newline='\n', mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=sorted(d.keys()))

            writer.writeheader()

            for x in range(lines_to_generate):
                d['date'] = f"{datetime.now().timestamp():.5f}"
                d['user_id'] = f"{random.randint(0, lines_to_generate):08}"
                writer.writerow(d)

    @staticmethod
    def size(size):
        units = {
            "B": 1,
            "KB": 10 ** 3, "MB": 10 ** 6, "GB": 10 ** 9, "TB": 10 ** 12,
            "KiB": 1024, "MiB": 1024 ** 2, "GiB": 1024 ** 3, "TiB": 1024 ** 4
        }

        number, unit = [string.strip() for string in size.split()]
        return int(float(number)*units[unit])
