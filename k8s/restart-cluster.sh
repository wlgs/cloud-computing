#!/bin/bash

kubectl delete pod -l ray.io/node-type=head
kubectl delete pod -l ray.io/node-type=worker