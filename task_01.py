from queue import Queue
import uuid
import time
import random


class Request:
    """Request class"""

    def __init__(self):
        # Generate unique request id
        self.request_id = uuid.uuid4()

    def __str__(self):
        # Return request's UUID as a string.
        return str(self.request_id)


class ServiceCenter:
    """Class for requests processing"""

    def __init__(self):
        # Create a service center and set up an empty queue for requests.
        self.request_queue = Queue()

    def generate_request(self):
        # Create a new request and add it to the queue.
        request = Request()
        self.request_queue.put(request)
        print(f"Adding request: {request}")

    def process_request(self):
        # Retrieve and process request from the queue, if one exists.

        if not self.request_queue.empty():
            req = self.request_queue.get()
            print(f"Processing request: {req}")
            time.sleep(1)
            print(f"Finished request: {req}")
        else:
            print("Queue is empty — nothing to process!")


if __name__ == "__main__":
    processor = ServiceCenter()

    print("Press 'Enter' to create and process a request")
    print("Press 'q' + 'Enter' to exit\n")

    while True:
        user_input = input(">>> ")

        if user_input.lower() == "q":
            print("Exiting program.")
            break

        # For imitation only
        time.sleep(random.uniform(0.3, 1.0))

        processor.generate_request()
        processor.process_request()
