import os, configparser

class Config:
    def __init__(self):
        self.workdir   = os.path.dirname(os.path.realpath(__file__))
        
    def Return(self, type):
        config = configparser.ConfigParser(interpolation=None)
        file   = self.workdir+'/integration.ini'
        config.read(file)
        if type == 'user':
            return config['GITHUB']['GITHUB_USER']
        elif type == 'token':
            return config['GITHUB']['GITHUB_TOKEN']
        elif type == 'reponame':
            return config['GITHUB']['GITHUB_REPOSITORY']

Config().Return('user')