from datetime import datetime
start_time = datetime.now()
a = 2**16
while True:
    if a>0:
        print(a)
        a -= 1
        continue 
    else:
        end_time = datetime.now()
        score = end_time - start_time
        print(f'The end, time score is {score}')
        break