from configparser import ConfigParser
from common_modules.logger import get_logger
import os


logger = get_logger("CONFIG")
class Config:
    config = ConfigParser()

    @staticmethod
    def get(section_name: str, param_name: str):
        return Config.config.get(section_name, param_name)

    @staticmethod
    def getint(section_name: str, param_name: str):
        return Config.config.getint(section_name, param_name)

    @staticmethod
    def getboolean(section_name: str, param_name: str):
        return Config.config.getboolean(section_name, param_name)

    @staticmethod
    def init(*files, **environs):
        """
        Инициализация конфига
        Сначала передаюстя файлы. Каждый последующий перезатирает старые данные, если они совпадают.
        Затем передаются параметры окружения
        :param files: file.ini, settings_dev.ini
        :param environs: SECTION=PREFIX_, RABBIT=APP_RABBIT_
        """
        for file in files:
            if os.path.isfile(file):
                Config.config.read(file)
                logger.info(f'{file} file added')
            else:
                logger.warning(f'{file} not found')
        for section, section_prefix in environs.items():
            dict = {section:
                        {name.replace(section_prefix, ''): value for name, value in os.environ.items()
                         if section_prefix in name}
                    }
            Config.config.read_dict(dict)
