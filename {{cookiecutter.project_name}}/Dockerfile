FROM python:alpine3.7 
COPY . /{{cookiecutter.project_name}}
WORKDIR /{{cookiecutter.project_name}}
RUN pip3 install -r requirements.txt
CMD [ "python3","run.py" ] 
