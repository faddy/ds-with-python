from data_structures.queues import Queue


def hot_potato_simulation(count, players):
    q = Queue()
    map(q.enqueue, players)

    while q.size() != 1:
        print 'Queue is     :', q.items
        for i in range(count):
            q.enqueue(q.dequeue())

        print 'Removing item:', q.dequeue()

    winner = q.dequeue()
    return winner
