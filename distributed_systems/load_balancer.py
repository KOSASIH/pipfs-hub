import requests


def create_load_balancer(hosts):
    # Create a load balancer using HAProxy or NGINX

    response = requests.get(f"http://{hosts[0]}/load_balance/{len(hosts)}")
    load_balancer_url = response.json()["load_balancer_url"]

    return load_balancer_url


def send_request(load_balancer_url, data):
    # Send a request to a load balancer

    response = requests.post(load_balancer_url, json=data)

    return response.json()
