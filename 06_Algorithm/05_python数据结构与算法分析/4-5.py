#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2022-07-15 23:16:55

from turtle import *

my_turtle = Turtle()
my_win = my_turtle.getscreen()

def draw_spiral(my_turtle, line_len):
    if len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()
