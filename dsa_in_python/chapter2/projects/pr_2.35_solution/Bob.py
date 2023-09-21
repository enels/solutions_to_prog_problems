import time


class Bob:

    def __init__(self, packet):
        self._received_packet = packet
        time.sleep(1)   # waits for packets from Alice
        self._check_for_packet()

    def _check_for_packet(self):
        """
        Checks if packet has been received
        """

        # check if packet has been received
        if self._received_packet != "":
            print("Packet Received")
            print(self._received_packet)
            self._received_packet = ""