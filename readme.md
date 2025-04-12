# OS Activity - Docker Environment Variable Demo

1. Start Project: run "git init"

2. Create Program: Create app.py and type the code

3. Containerize the Program: Create Dockerfile and type the code

4. Setup local Docker Registry

- Start a registry: run "docker run -d -p 5000:5000 --name registry registry:2"
- Build Docker Image: run "docker build -t localhost:5000/demo ."
- Push Docker Image: run "docker push localhost:5000/demo"

5. Run the Container: run "docker run -e secret_user=<your_name> localhost:5000/demo"

6. Create documents
