import sys
from pymongo import *
from pymongo.errors import ConnectionFailure
def main():
   """ Connect to MongoDB """
   try:
      client = MongoClient('localhost', 27017)
      print "Connected successfully"
   except ConnectionFailure, e:
      sys.stderr.write("Could not connect to MongoDB: %s" % e)
      sys.exit(1)
if __name__ == "__main__":
   main()
