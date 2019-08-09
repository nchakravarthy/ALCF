import parsl
import os
from parsl.app.app import python_app, bash_app
from parsl.config import Config
from parsl.configs.local_threads import config
from parsl.executors.threads import ThreadPoolExecutor
import time

local_threads = Config(
  executors=[
     ThreadPoolExecutor(
          max_threads=100,
          label='local_threads'
       )
   ]
)

parsl.load(local_threads)

@python_app

def sleeper():
    while True:
        num = input('How long to sleep for in seconds: ')
        try:
            num = float(num)
        except ValueError:
            print('Please enter a number.\n')
            continue
        print('Before: %s' % time.ctime())
        time.sleep(num)
        print('After: %s\n' % time.ctime())
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()