# FastAPI-python-app
Run the following commands once you ssh into your AWS EC2 instance
1. sudo apt-get update
2. sudo apt install -y python3-pip nginx
3. sudo vim /etc/nginx/sites-enabled/fastapi_nginx //To configure the nginx for routing traffic to AWS server
4. sudo service nginx restart
5. git clone https://github.com/biswajitsaha12/fastapi_app.git //clone git project
6. pip3 install -r requirements.txt
7. python3 -m uvicorn main:app //To execute the code