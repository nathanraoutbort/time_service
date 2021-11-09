
FROM python

RUN  pip install flask requests 

ADD main.py .


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "./main.py"]
