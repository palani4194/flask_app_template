# flask-scaffold install

1. Install - cookiecutter

    pip install --user cookiecutter

2. Create your application from this template:

    cookiecutter https://bitbucket.org/microservicesembibe/docker_stub_flask.git

3. Setup project using docker

    cd yourproject
    sudo docker build -t yourimagename .
    sudo docker run -it --name yourcontainername -p 7000:7000 yourimagename

4. And then open it at browser [http://127.0.0.1:7000/]
