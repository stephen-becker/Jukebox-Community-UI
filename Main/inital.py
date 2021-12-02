import sys
from termcolor import colored, cprint

def GetTitleText(sectionNeeded):

    match sectionNeeded:
        case 1:
            return colored('Assigned GPU:', 'red')
        case 2:
            return colored('Google Drive Connector:', 'red')
        case 3:
            return colored('System Status:', 'red')