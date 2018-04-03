#!/usr/bin/python3
#-*- coding: utf-8 -*-

import threading
import time
import sys
import random

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

def process_temperature(reader):
    while True:
        time.sleep(3)
        reader.process()

        
class ThermometerReader():
    def __init__(self, file_manager, thermometer):
        self.current_temperature = 0
        self.file_manager = file_manager
        self.thermometer = thermometer

    def process(self):
        self.current_temperature = self.thermometer.get_temperature()
        self.file_manager.write(self.current_temperature)

        
class FakeThermometer():
    def __init__(self):
        self.temperature = 0

    def get_temperature(self):
        return random.randint(0, 100)

    
class ConsoleOutput():
    def __init__(self, child):
        self.child = child

    def write(self, output_value):
        print('{0}'.format(output_value))
        self.child.write(output_value)

        
class FileOutput():
    def write(self, output_value):
        print('File output here : {0}'.format(output_value))


        
if __name__ == "__main__":
    main()
