from piComm.transmitter import transmitter_main
from piComm.receiver import receiver_main


if __name__ == '__main__':
    option = input("1 - Transmitter | 2 - Receiver | 0 - Exit")
    while option != 0:
        if option == 1:
            transmitter_main()
        elif option == 2:
            receiver_main()
        option = input("1 - Transmitter | 2 - Receiver | 0 - Exit")