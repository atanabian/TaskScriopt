import API
from tabulate import tabulate
import argparse
from docopt import docopt


usage = """
Usage:
TaskScript.py --init 
TaskScript.py --add <category> <description> [<status>] 
TaskScript.py --show [<category>]
TaskScript.py --delete [<category>]
"""

args = docopt(usage)

if args['--init'] : 
    API.init()

    print("Table Created :) ")

if args['--show'] : 
    category = args['<category>']
    print(tabulate(API.display(category)))

if args['--delete'] :
    category = args['<category>']
    API.delete(category)

if args['--add'] : 
    category = args['<category>']
    description = args['<description>']
    status = args['<status>']
    
    API.insert(category , description , status)

    print("Task added!")

