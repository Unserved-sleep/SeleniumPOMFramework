from configparser import ConfigParser

config = ConfigParser()
config.read("configurations/config.ini")

class ReadConfig:
    @staticmethod
    def get_url():
        return config.get("common","baseURL")

    @staticmethod
    def get_username():
        return config.get("common","username")

    @staticmethod
    def get_password():
        return config.get("common","password")