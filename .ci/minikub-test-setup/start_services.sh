#!/usr/bin/env bash
set -ex

kubectl create -f postgresConfig.yaml
kubectl create -f statefulSet.yaml
kubectl create -f service.yaml
minikube service testing-service --url=true

GALAXY_TEST_DBURI="postgresql://postgres:postgres@localhost:$(kubectl get service testing-service -o jsonpath='{.spec.ports[0].nodePort}')/galaxy?client_encoding=utf-8"
GALAXY_TEST_AMQP_URL="amqp://localhost:$(kubectl get service testing-service -o jsonpath='{.spec.ports[1].nodePort}')//"
export GALAXY_TEST_DBURI
export GALAXY_TEST_AMQP_URL
