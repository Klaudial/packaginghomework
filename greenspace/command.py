from argparse import ArgumentParser
from greenspace import greenspace

def process():
   parser = ArgumentParser(description = "Generate appropriate greetings")

   parser.add_argument('--stuff', '-t')
   parser.add_argument('--polite', '-p', action="store_true")
   

   arguments= parser.parse_args()

   print greenspace(arguments.stuff, arguments.family, arguments.title, arguments.polite)

if __name__ == "__main__":
    process()