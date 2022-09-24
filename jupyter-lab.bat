MD workspace
CD workspace


REM # (1) install pipenv
REM ##  Require install python:3 first
CALL pip3 install pipenv

REM # (2) install python 3.10 env
CALL pipenv --python 3.10

REM # (3) open jupyter-lab
CALL pipenv run jupyter-lab