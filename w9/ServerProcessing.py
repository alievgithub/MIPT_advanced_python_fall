class Connect(Exception):
    pass

class Write(Exception):
    pass


def connect_user(info):
    pass

    with open("ServerProcessing.txt", "w") as file:
        yield from write_file(file)

def write_file(object):
    while True:
        x = yield
        if x == "Stop":
            break
        object.writelines(x)
        object.writelines("\n")
    object.close()


def task_planner():
    users = []
    while True:
        try:
            info = yield
            users.append(info)
        except Connect:
            yield from connect_user(users)


if __name__ == "__main__":
    coroutine = task_planner()
    next(coroutine)
    coroutine.send(["Artem", "Daniil"])
    next(coroutine)
    coroutine.throw(Connect)
    coroutine.send("Hello, wazzup?")
    coroutine.send("None, watching a game, have a Bud. So, what about u?")
    coroutine.send("None, watching a game, have a Bud")

    coroutine.close()
