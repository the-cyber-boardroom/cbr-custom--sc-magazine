#!/bin/bash

uvicorn cbr_custom_sc_magazine.lambdas.handler:app --host 0.0.0.0 --port 8080