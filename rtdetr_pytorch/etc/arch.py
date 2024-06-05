
import argparse
import os
import sys
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..'))

from src.core import YAMLConfig
import src.misc.dist as dist
from src.solver import TASKS

def main(args, ) -> None:
  '''main
  '''
  # dist.init_distributed()

  cfg = YAMLConfig(
      args.config,
  )

  print(cfg.model)
    


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('--config', '-c', type=str, )

  args = parser.parse_args()

  main(args)
