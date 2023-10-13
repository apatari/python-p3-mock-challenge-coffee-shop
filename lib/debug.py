#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    co1 = Coffee('small')
    co2 = Coffee('med')
    co3 = Coffee('large')

    cu1 = Customer('A')
    cu2 = Customer('B')
    cu3 = Customer('C')

    o1 = Order(cu1, co1, 2.0)
    o2 = Order(cu2, co2, 4.0)
    o3 = Order(cu3, co1, 2.0)
    o4 = Order(cu1, co2, 2.0)
    o5 = Order(cu1, co1, 2.0)


    ipdb.set_trace()
