#!/bin/bash
export ROOT_DIR=${PWD}

cd ${ROOT_DIR}/badmoviesapi/v-env/lib/python3.7/site-packages && 
zip -r9 ${ROOT_DIR}/badmoviesapi/badmoviesapi.zip . &&
cd ${ROOT_DIR}/badmoviesapi && zip -g badmoviesapi.zip badmoviesapi.py 


