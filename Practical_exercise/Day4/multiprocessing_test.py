import multiprocessing
import time


A  = 0
# 숫자를 출력하는 함수
def print_numbers():
    global A
    for i in range(5):
        print("i:",i)
        print("공통A: ", A)
        A+=1
        time.sleep(1)
if __name__ == '__main__':
# 두 개의 프로세스 생성 및 시작
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_numbers)
    process1.start()
    process2.start()
    process1.join()
    process2.join()