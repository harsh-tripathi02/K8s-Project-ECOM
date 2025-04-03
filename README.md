# K8s-Project-ECOM

Welcome to the **K8s-Project-ECOM**, a Kubernetes-based microservices project for an e-commerce application. This project demonstrates how to deploy and manage multiple microservices (Product, Order, and Payment) using Kubernetes.

## Project Overview

This project consists of the following microservices:

1. **Product Service**: Provides product details.
2. **Order Service**: Manages customer orders.
3. **Payment Service**: Handles payment processing.

Each service is containerized using Docker and deployed to Kubernetes as a Deployment with a corresponding Service for internal communication. An Ingress is configured to route traffic to the appropriate service based on the URL path.

## Folder Structure

- `k8s/`: Contains Kubernetes manifests for deployments, services, and ingress.
- `Product-Service/`: Contains the Product Service code and Dockerfile.
- `Order-Service/`: Contains the Order Service code and Dockerfile.
- `Payment-Service/`: Contains the Payment Service code and Dockerfile.

## How to Deploy

1. **Build Docker Images**:
   Navigate to each service folder and build the Docker images:
```bash
docker build -t <your-dockerhub-username>/product-service ./Product-Service
docker build -t <your-dockerhub-username>/order-service ./Order-Service
docker build -t <your-dockerhub-username>/payment-service ./Payment-Service
```

2. **Push Images to Docker Hub** :

```bash 
docker push <your-dockerhub-username>/product-service
docker push <your-dockerhub-username>/order-service
docker push <your-dockerhub-username>/payment-service
```
3. **Apply Kubernetes Manifests**: Deploy the services and ingress to your Kubernetes cluster:

```bash
kubectl apply -f k8s/
```
4. **Access the Application**: Add the following entry to your `/etc/hosts` file (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows):

```
127.0.0.1 my-ecommerce-app.local
```

Access the services via:

- `http://my-ecommerce-app.local/products`
- `http://my-ecommerce-app.local/orders`
- `http://my-ecommerce-app.local/payments`


*Scaling the Pods*
Kubernetes makes it easy to scale your application to handle increased traffic. You can scale the number of pods for any service using the `kubectl scale` command.

*Example: Scaling the Product Service*
To scale the Product Service to 5 replicas:

```kubectl scale deployment product-service --replicas=5```

*Autoscaling*
You can also enable autoscaling to dynamically adjust the number of pods based on CPU or memory usage:

```kubectl autoscale deployment product-service --min=2 --max=10 --cpu-percent=80```

This command ensures that the Product Service will have at least 2 pods and at most 10 pods, scaling automatically when CPU usage exceeds 80%.

### Key Features
- *Microservices Architecture*: Each service is independently deployable and scalable.
- *Kubernetes Deployment*: Uses Deployments, Services, and Ingress for efficient management.
- *Dockerized Services*: Each service is containerized for portability and consistency.
- *Ingress Configuration*: Routes traffic to the appropriate service based on URL paths.

### Future Enhancements
- Add a frontend service to interact with the backend services.
- Implement a database for persistent storage.
- Integrate monitoring and logging tools like Prometheus and Grafana.