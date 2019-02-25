import checker
import aggregator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dump', help='Dump file path')
args = parser.parse_args()

aggregator.aggregate(args.dump)
checker.check('./aggregator.json')