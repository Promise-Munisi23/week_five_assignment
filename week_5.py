class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def call(self, number):
        print(f"Calling {number}... 📞")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Color: {self.color}")


phone = Smartphone("Apple", "iPhone 13", 128, "Space Gray")
phone.display_info()
phone.call("123-456-7890")
phone.send_message("123-456-7890", "Hello, how are you?")
