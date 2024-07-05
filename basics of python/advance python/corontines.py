
def search():
    import time
    s = {1, 2, 3, 4, 5, 6, 7}

    time.sleep(2)

    while True:
        time = (yield )
        if time in s:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    ob = search()
    print("searching strts")
    next(ob)
    ob.send(2)
    ob.close()
