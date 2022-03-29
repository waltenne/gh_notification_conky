import os

class BadTux:
    def __init__(self):
        self.workdir  = os.path.dirname(os.path.realpath(__file__))
    
    def Notification(self, type: int) -> int:
        self.type = type
        if self.type == 1:
            notification  = self.workdir+"/resource/e_olha_so.mp3"
            return notification
        elif self.type == 2:
            notification  = self.workdir+"/resource/zika_de_mais.mp3"
            return notification
        elif self.type == 3:
            notification  = self.workdir+"/resource/sensacional.mp3"
            return notification
        elif self.type == 4:
            notification  = self.workdir+"/resource/vai.mp3"
            return notification

