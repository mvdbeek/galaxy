#!/usr/bin/env bash
set -ex

kubectl create -f configMap.yaml
kubectl create -f stateFule.yaml
kubectl create -f service.yaml
minikube service postgres-service --url=true

GALAXY_TEST_DBURI="postgresql://postgres:postgres@localhost:$(kubectl get service postgres-service -o jsonpath='{.spec.ports[*].nodePort}')"
export GALAXY_TEST_DBURI
