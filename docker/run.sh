#!/bin/bash

docker run -itd --rm --name rt-detr \
  --gpus all \
  -v .:/workspace/rt-detr \
  -v /mnt/e/Data/COCO-2017:/workspace/data/coco2017 \
  teabots/rt-detr \
  /bin/bash
