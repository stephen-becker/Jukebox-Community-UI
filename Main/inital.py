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

    numRAM = [str(int) for int in gpuRAM]
    a_numRAM = numRAM
    int_numRAM = int(numRAM)

    if int_numRAM <= 15000:
        return colored('Limited RAM, consider using 1b_lyrics!', 'red')
    elif int_numRAM > 15000:
        return colored('With current RAM, most/all models should work fine.', 'green')
    else:
        return colored('Could not evaluate.', 'red')
