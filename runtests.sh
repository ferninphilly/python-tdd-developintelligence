#!/bin/bash
cd ${PWD}/introduction_to_codepipeline/labs
#Run all tests
python -m unittest;
#Print out results from tests
coverage run --source . -m unittest discover && coverage report