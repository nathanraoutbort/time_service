Pull the project 
Run "docker build -t time_service ." in the root directory of the project 
Run "docker build -t nproxy ./nginx" in the root directory of the project
Run "docker-compose up -d" in the root directory of the project

Browse to your localhost/127.0.0.1 and add the ip as a query param
Example : http://127.0.0.1/?ip=8.8.8.8

And that it !


More details :
The yml file will create  2 services called "nproxy" and "time_service"
nproxy is nginx that lisen on port 80 and will foward the requests to "time_service" with port 5001
"time_service" running python script called "main.py"  using flask,json,request liberis for receiving http requests and make calls   
