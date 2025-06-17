import time
import random

def simulate_traffic(mode="normal"):
    while True:
        request_count = 1
        if mode == "ddos":
            request_count = random.randint(20, 40)  # High volume
        else:
            request_count = random.randint(1, 5)  # Normal traffic

        with open("requests.log", "a") as f:
            for _ in range(request_count):
                f.write("fake_request\n")

        time.sleep(1)

if __name__ == "__main__":
    mode = input("Enter traffic mode (normal/ddos): ").strip().lower()
    simulate_traffic(mode)

