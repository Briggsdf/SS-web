import os


class LocalConfig(object):
    SECRET_KEY = 'Not_a_chance'


class DeploymentConfig(LocalConfig):
    SECRET_KEY = os.environ.get('SECRET_KEY')
