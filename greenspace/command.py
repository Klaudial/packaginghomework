from argparse import ArgumentParser
from greenspace import greenspace

def process():
   parser = ArgumentParser(description = "A program to calculate and also visualise the amount of greenspace between two places")

   parser.add_argument('start')
   parser.add_argument('end')
   parser.add_argument('steps')

   arguments= parser.parse_args()

   print greenspace(arguments.start, arguments.end, arguments.steps)

if __name__ == "__main__":
    process()