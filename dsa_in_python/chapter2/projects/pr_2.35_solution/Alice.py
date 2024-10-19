import time
from Bob import Bob


class Alice:
    """
    Mimics the creation of an internet packet
    """

    def __init__(self):

        self._packet = ""

    def create_packet(self):
        """
        Create packet
        """
        self._packet = "Internet Packet from Alice"

    def send_packet(self):
        """
        Send the packet
        """

        while True:
            self.create_packet()
            time.sleep(5)
            # send packet
            print("Packet sent")
            Bob(self._packet)


if __name__ == "__main__":
    alice = Alice()
    alice.create_packet()
    alice.send_packet()