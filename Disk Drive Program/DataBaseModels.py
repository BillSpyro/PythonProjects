
method = input("Hello User, please choose a method (FCFS: 0, SSTF: 1, SCAN: 2, C-SCAN: 3): ")
initial = input("Please input a starting value (Example '20'): ")
initial = int(initial)
requests = input("What are the requests? (Please fill it out like this '22 40 12'): ")
requests = requests.split(" ")
for i in range(0, len(requests)):
    requests[i] = int(requests[i])
detailed = input("Do you want a detailed output? (0 for no, 1 for yes): ")
if detailed == '1':
    detailed = True
else:
    detailed = False

def FCFS(initial, requests, detailed):

    queue = []
    order = []
    movement = 0
    totalMovement = 0
    turn = 1

    print("~~~~~")
    print("FCFS Method")
    order.append(initial)
    while len(requests) > 0:
        if len(queue) < 3:
            queue.append(requests[0])
            del requests[0]
        else:
            order.append(queue[0])
            del queue[0]
            queue.append(requests[0])
            del requests[0]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    while len(queue) > 0:
        order.append(queue[0])
        del queue[0]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    if detailed:
        print("~~~~~")
    maxTurn = len(order)
    for i in order:
        if turn < maxTurn:
            movement = i - order[0 + turn]
            movement = abs(movement)
            totalMovement += movement
            turn += 1
            if detailed:
                print("Movement: " + str(movement))
    print("~~~~~")
    print("Final Order: " + str(order))
    print("Total Movement: " + str(totalMovement))
    return order

def SSTF(initial, requests, detailed):

    queue = []
    order = []
    movement = 0
    totalMovement = 0
    difference = 0
    differenceTurn = 0
    turn = 1

    print("~~~~~")
    print("SSTF Method")
    order.append(initial)
    while len(requests) > 0:
        if len(queue) < 3:
            queue.append(requests[0])
            del requests[0]
        else:
            differenceList = []
            for i in queue:
                difference = order[0 + differenceTurn] - i
                difference = abs(difference)
                differenceList.append(difference)
            differenceTurn += 1
            order.append(queue[differenceList.index(min(differenceList))])
            del queue[differenceList.index(min(differenceList))]
            queue.append(requests[0])
            del requests[0]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    while len(queue) > 0:
        differenceList = []
        for i in queue:
            difference = order[0 + differenceTurn] - i
            difference = abs(difference)
            differenceList.append(difference)
        differenceTurn += 1
        order.append(queue[differenceList.index(min(differenceList))])
        del queue[differenceList.index(min(differenceList))]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    if detailed:
        print("~~~~~")
    maxTurn = len(order)
    for i in order:
        if turn < maxTurn:
            movement = i - order[0 + turn]
            movement = abs(movement)
            totalMovement += movement
            turn += 1
            if detailed:
                print("Movement: " + str(movement))
    print("~~~~~")
    print("Final Order: " + str(order))
    print("Total Movement: " + str(totalMovement))
    return order

def SCAN(initial, requests, detailed):

    queue = []
    order = []
    movement = 0
    totalMovement = 0
    difference = 0
    differenceTurn = 0
    reverse = False
    turn = 1

    print("~~~~~")
    print("SCAN Method")
    order.append(initial)
    while len(requests) > 0:
        if len(queue) < 3:
            queue.append(requests[0])
            del requests[0]
        else:
            differenceList = []
            if not reverse:
                for i in queue:
                    if i > order[0 + differenceTurn]:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference)
                    else:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference + 1000)
                if all(i > 1000 for i in differenceList):
                    differenceList = []
                    reverse = True
            if reverse:
                for i in queue:
                    if i < order[0 + differenceTurn]:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference)
                    else:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference + 1000)
                if all(i > 1000 for i in differenceList):
                    differenceList = []
                    reverse = False
            if not reverse:
                for i in queue:
                    if i > order[0 + differenceTurn]:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference)
                    else:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference + 1000)
            differenceTurn += 1
            order.append(queue[differenceList.index(min(differenceList))])
            del queue[differenceList.index(min(differenceList))]
            queue.append(requests[0])
            del requests[0]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    while len(queue) > 0:
        differenceList = []
        if not reverse:
            for i in queue:
                if i > order[0 + differenceTurn]:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference)
                else:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference + 1000)
            if all(i > 1000 for i in differenceList):
                differenceList = []
                reverse = True
        if reverse:
            for i in queue:
                if i < order[0 + differenceTurn]:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference)
                else:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference + 1000)
            if all(i > 1000 for i in differenceList):
                differenceList = []
                reverse = False
        if not reverse:
            for i in queue:
                if i > order[0 + differenceTurn]:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference)
                else:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference + 1000)
        differenceTurn += 1
        order.append(queue[differenceList.index(min(differenceList))])
        del queue[differenceList.index(min(differenceList))]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    if detailed:
        print("~~~~~")
    maxTurn = len(order)
    for i in order:
        if turn < maxTurn:
            movement = i - order[0 + turn]
            movement = abs(movement)
            totalMovement += movement
            turn += 1
            if detailed:
                print("Movement: " + str(movement))
    print("~~~~~")
    print("Final Order: " + str(order))
    print("Total Movement: " + str(totalMovement))
    return order

def CSCAN(initial, requests, detailed):

    queue = []
    order = []
    movement = 0
    totalMovement = 0
    difference = 0
    differenceTurn = 0
    fromZero = False
    turn = 1

    print("~~~~~")
    print("C-SCAN Method")
    order.append(initial)
    while len(requests) > 0:
        if len(queue) < 3:
            queue.append(requests[0])
            del requests[0]
        else:
            differenceList = []
            if not fromZero:
                for i in queue:
                    if i > order[0 + differenceTurn]:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference)
                    else:
                        difference = order[0 + differenceTurn] - i
                        difference = abs(difference)
                        differenceList.append(difference + 1000)
                if all(i > 1000 for i in differenceList):
                    differenceList = []
                    fromZero = True
            if fromZero:
                for i in queue:
                    difference = 0 - i
                    difference = abs(difference)
                    differenceList.append(difference)
            fromZero = False
            differenceTurn += 1
            order.append(queue[differenceList.index(min(differenceList))])
            del queue[differenceList.index(min(differenceList))]
            queue.append(requests[0])
            del requests[0]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    while len(queue) > 0:
        differenceList = []
        if not fromZero:
            for i in queue:
                if i > order[0 + differenceTurn]:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference)
                else:
                    difference = order[0 + differenceTurn] - i
                    difference = abs(difference)
                    differenceList.append(difference + 1000)
            if all(i > 1000 for i in differenceList):
                differenceList = []
                fromZero = True
        if fromZero:
            for i in queue:
                difference = 0 - i
                difference = abs(difference)
                differenceList.append(difference)
        fromZero = False
        reverse = False
        differenceTurn += 1
        order.append(queue[differenceList.index(min(differenceList))])
        del queue[differenceList.index(min(differenceList))]
        if detailed:
            print("~~~~~")
            print("requests: " + str(requests))
            print("queue: " + str(queue))
            print("order: " + str(order))
    if detailed:
        print("~~~~~")
    maxTurn = len(order)
    for i in order:
        if turn < maxTurn:
            movement = i - order[0 + turn]
            movement = abs(movement)
            totalMovement += movement
            turn += 1
            if detailed:
                print("Movement: " + str(movement))
    print("~~~~~")
    print("Final Order: " + str(order))
    print("Total Movement: " + str(totalMovement))
    return order

if method == '0':
    FCFS(initial, requests, detailed)
elif method == '1':
    SSTF(initial, requests, detailed)
elif method == '2':
    SCAN(initial, requests, detailed)
elif method == '3':
    CSCAN(initial, requests, detailed)
else:
    print("Method was not chosen")
