#!/bin/bash

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com
docker build -t hallween-event ./app
docker tag hallween-event:latest 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com/hallween-event:latest
