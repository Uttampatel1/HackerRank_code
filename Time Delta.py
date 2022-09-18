import datetime
format_str = '%a %d %b %Y %H:%M:%S %z' # The format
t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()
        
    parse_t1 = datetime.datetime.strptime(t1, format_str)
    parse_t2 = datetime.datetime.strptime(t2, format_str)



    delta = parse_t1 - parse_t2

    delta = int(abs(delta.total_seconds()))
    print(delta)