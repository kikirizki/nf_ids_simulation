import time
import random
from collections import deque

class MovingAverageIDS:
    def __init__(self, window_size=10, threshold=15):
        self.window_size = window_size
        self.threshold = threshold
        self.request_times = deque(maxlen=window_size)

    def log_request(self, current_rate):
        self.request_times.append(current_rate)
        avg_rate = sum(self.request_times) / len(self.request_times)
        if avg_rate > self.threshold:
            print(f"[ALERT] Potential DDoS detected! Avg rate: {avg_rate:.2f}")
        else:
            print(f"[INFO] Normal traffic. Avg rate: {avg_rate:.2f}")


def simulate_server():
    ids = MovingAverageIDS(window_size=10, threshold=15)
    
    print("[SERVER] Running... Waiting for requests")
    while True:
        try:
            with open("requests.log", "r") as f:
                lines = f.readlines()
                if lines:
                    current_rate = len(lines)
                    ids.log_request(current_rate)
                    open("requests.log", "w").close()  # Clear log
                else:
                    ids.log_request(0)
        except FileNotFoundError:
            ids.log_request(0)
        time.sleep(1)

if __name__ == "__main__":
    simulate_server()
