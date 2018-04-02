import threading
import time
import sys
from random import *

def main():
    currentTemperature=0
    inputCommand = ""

    fileManager = consoleOutput(fileOutput())
    thermometer = fakeThermometer()

    reader = thermometerReader(fileManager, thermometer)
    print ('starting')

    tempThread = threading.Thread(name='temp_thread', target=processTemperature, args=(reader,))
    tempThread.daemon = True
    tempThread.start()

    print('Thread started')

    while True:
        if raw_input() == 'quit':
            print('quitting')
            sys.exit()
        else:
            print('continuing')

def processTemperature(reader):
    while True:
        time.sleep(3)
	reader.process()

class thermometerReader():
    def __init__(self, fileManager, thermometer):
        self.currentTemperature = 0
        self.fileManager = fileManager
	self.thermometer = thermometer

    def process(self):
        self.currentTemperature = self.thermometer.getTemperature()
        self.fileManager.write(self.currentTemperature)

class fakeThermometer():
    def __init__(self):
 	self.temperature = 0

    def getTemperature(self):
	return random()

class consoleOutput():
    def __init__(self, child):
	self.child = child

    def write(self, outputValue):
	print('{0}'.format(outputValue))
	self.child.write(outputValue)

class fileOutput():
    def write(self, outputValue):
	print('File output here : {0}'.format(outputValue))

if __name__ == "__main__":
    main()
