### OS Activity - Docker Environment Variable Demo

1. Start Project
```git init```

2. Create Program: Create app.py and type the code

3. Containerize the Program: Create Dockerfile and type the code

4. Setup local Docker Registry

- Start a registry: ```docker run -d -p 5000:5000 --name registry registry:2```
- Build Docker Image: ```docker build -t localhost:5000/demo .```
- Push Docker Image: ```docker push localhost:5000/demo```

5. Run the Container: ```docker run -e secret_user=<your_name> localhost:5000/demo```

6. Create documents
