import checker
import aggregator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dump', help='Dump file path')
args = parser.parse_args()

checker.check(args.dump)
aggregator.aggregate()