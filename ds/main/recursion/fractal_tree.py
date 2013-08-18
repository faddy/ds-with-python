
import turtle
import random

def tree(t, tree_len, size):

    if tree_len < 5 or size <= 0:
        return

    if size <= 3:
        t.color('green')

    t.width(size)
    t.forward(tree_len)

    rt_angle = random.randint(15, 45)
    t.right(rt_angle)
    tree(t, tree_len-10, size-3)

    lt_angle = random.randint(15,45)
    t.left(lt_angle)
    tree(t, tree_len-10, size-3)

    t.right(lt_angle - rt_angle)
    t.backward(tree_len)

    t.color('brown')


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown')
    tree(t, 75, 21)
