from collections import deque

class CharityDonationTracker:
    def __init__(self):
        self.donation_history = []
        self.undo_stack = []
        self.donation_requests = deque()

    def add_donation(self, donor, amount):
        donation = (donor, amount)
        self.donation_history.append(donation)
        self.undo_stack.append(donation)
        print(f"Donation added: {donor} donated ${amount}")

    def undo_donation(self):
        if self.undo_stack:
            donation = self.undo_stack.pop()
            self.donation_history.remove(donation)
            print(f"Undone donation: {donation[0]} - ${donation[1]}")
        else:
            print("No donations to undo")

    def add_donation_request(self, charity, amount):
        request = (charity, amount)
        self.donation_requests.append(request)
        print(f"Donation request added: {charity} requests ${amount}")

    def process_donation_request(self):
        if self.donation_requests:
            request = self.donation_requests.popleft()
            print(f"Processing donation request: {request[0]} - ${request[1]}")
        else:
            print("No donation requests to process")

    def display_donation_history(self):
        if self.donation_history:
            print("Donation History:")
            for donor, amount in self.donation_history:
                print(f"{donor}: ${amount}")
        else:
            print("No donations in history")

    def display_donation_requests(self):
        if self.donation_requests:
            print("Pending Donation Requests:")
            for charity, amount in self.donation_requests:
                print(f"{charity}: ${amount}")
        else:
            print("No pending donation requests")

# Example usage
tracker = CharityDonationTracker()

tracker.add_donation("mukama", 100)
tracker.add_donation("uyisenga", 50)
tracker.add_donation("lea", 200)

tracker.add_donation_request("Local Food Bank", 500)
tracker.add_donation_request("Animal Shelter", 300)

tracker.display_donation_history()
tracker.display_donation_requests()

tracker.undo_donation()
tracker.process_donation_request()

tracker.display_donation_history()
tracker.display_donation_requests()