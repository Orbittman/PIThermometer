#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Raspberry pi thermometer application
"""

import sys
import threading
from time import sleep
from random import randint


class ThermometerReader():
    """gets temp from sensor and writes to output"""
    def __init__(self, file_manager, thermometer):
        self.current_temperature = 0
        self.file_manager = file_manager
        self.thermometer = thermometer

    def process(self):
        self.current_temperature = self.thermometer.get_temperature()
        self.file_manager.write(self.current_temperature)


        
class FakeThermometer():
    """provides random temps from 0 to 100"""
    def __init__(self):
        self.temperature = 0

    def get_temperature(self):
        return randint(0, 100)


    
class ConsoleOutput():
    """Writes temp to std out"""
    def __init__(self, child):
        self.child = child

    def write(self, output_value):
        print('{0}'.format(output_value))
        self.child.write(output_value)

        
        
class FileOutput():
    """Writes temp to file or database"""
    def write(self, output_value):
        print('File output here : {0}'.format(output_value))


        
def process_temperature(reader):
    while True:
        sleep(3)
        reader.process()

        
def main():
    input_command = ""

    file_manager = ConsoleOutput(FileOutput())
    thermometer = FakeThermometer()

    reader = ThermometerReader(file_manager, thermometer)
    print ('starting')

    temp_thread = threading.Thread(name='temp_thread', target=process_temperature, args=(reader,))
    temp_thread.daemon = True
    temp_thread.start()

    print('Thread started')

    while True:
        if input() == 'quit':
            print('quitting')
            sys.exit()
        else:
            print('continuing')


        
if __name__ == "__main__":
    main()
