import sys
from termcolor import colored, cprint

def GetTitleText(sectionNeeded):

    if sectionNeeded == 1:
        return colored('Assigned GPU:', 'red')
    elif sectionNeeded == 2:
        return colored('Google Drive Connector:', 'red')
    elif sectionNeeded == 3:
        return colored('System Status:', 'red')