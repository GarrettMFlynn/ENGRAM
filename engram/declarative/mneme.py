""" 
This module defines :class:'Mneme'
"""

from engram.procedural import features

import datetime

class Mneme(object):
    def __init__(self, id,raw=None,tag=None,settings=None):
        """
        This is the constructor for the Mneme data object,
        the smallest unit of memory tracked by ENGRAM.
        """

        self.id = id
        self.date = datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
        self.tag = tag
        self.feature = settings['feature']

        self.data = features.select(self.feature,raw,settings)


    def __repr__(self):
        return "Mneme('{},'{}',{})".format(self.id, self.date)

    def __str__(self):
        return '{} _ {}'.format(self.id, self.date)