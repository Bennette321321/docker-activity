### How to Run This Container

1. Clone this repository:
```git clone https://github.com/Bennette321321/docker-activity.git```

2. Open docker-activity:
```cd docker-activity```

3. Build the Docker image:
```docker build -t docker-activity .```

4. Run the container with your name as an environment variable:
```docker run -e secret_user=<your_name> docker-activity```
