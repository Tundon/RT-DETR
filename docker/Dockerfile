FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime


RUN apt update -qq && \
    apt install -y git vim

COPY rtdetr_pytorch/requirements.txt /workspace

RUN pip --no-cache-dir install -r /workspace/requirements.txt
