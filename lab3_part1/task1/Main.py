# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket
# (purchased 60 or more days before the event), late ticket
# (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties: --done--
# -the ability to construct a ticket by number; --done--
# -the ability to ask for a ticket’s price; --done--
# -the ability to print a ticket as a String. --done__
from Event import Event
from Tickets import *


def main():
    t1 = Regular_ticket('name', '20-11-21', 1.)
    t2 = Student_ticket('name', '20-11-21', 1.)
    t3 = Late_ticket('name', '20-11-21', 1.)
    t4 = Advance_ticket('name', '20-11-21', 1.)
    event = Event('20-11-21', 'name', 1, 1, 1., [t1, t2, t3, t4])
    event.put_event()
    # print(event.to_dict())
    # print(event)
    # event.remove_ticket(int(input()))
    # print(event)
    # print(t1)
    # print(Regular_ticket.from_dict(t1.to_dict()))
    # print(event)
    # print(Event.get_event('Event_name'))
    # event.add_ticket(Event.buy_ticket(event, '7-09-21'))
    # print(event)
    # print('\n\n\n', event)
    # print(Regular_ticket.buy_ticket(event, '7-09-21'))


main()