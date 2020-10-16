
def solution(c, m):
    if c == 1:
        print("elastic collision")
        return

    elif c == 0:
        print(f"0 bounces\n{m} meters traveled")
        return

    bounce_count = 0
    traveled_meters = 0
    traveled_meters += m

    while True:
        if m > 0.1:
            m *= c
            bounce_count += 1
            traveled_meters += m * 2
        else:
            traveled_meters -= m
            break

    print(f"{bounce_count} bounces\n{round(traveled_meters, 2)} meters traveled")
    return


if __name__ == '__main__':
    solution(0.99, 10)
