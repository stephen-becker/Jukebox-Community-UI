import sys
from termcolor import colored, cprint

def GetTitleText(sectionNeeded):

    if sectionNeeded == 1:
        return colored('Assigned GPU:', 'red')
    elif sectionNeeded == 2:
        return colored('Google Drive Connector:', 'red')
    elif sectionNeeded == 3:
        return colored('Notebook Compatibility:', 'yellow')

def CheckNotebook(gpuRAM):

    if gpuRAM <= 15000:
        return colored('Limited RAM, consider using 1b_lyrics!', 'red')
    elif gpuRAM > 15000:
        return colored('With current RAM, most/all models should work fine.', 'green')
    else:
        return colored('Could not evaluate.', 'red')
