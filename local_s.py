import matplotlib.pyplot as plt
import time #timeモジュールのインポート
import math 
import random
"""
局所探索　挿入近傍
初期解はnearest_neighborを用いて得る。
最初に見つけた近傍解に移動する。
探索する点は変更し続ける。

"""
def distance(x1,y1,x2,y2):
    a=(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
    return math.sqrt(a)


def insert_neighbor_insert(route,a,b):
    a_num = route.pop(a)
    route.insert(b,a_num)


def swap_neighbor(route,a,b):
    tmp = route[b]
    route[b] = route[a]
    route[a] = tmp


def nearest_n(route, listA):
    tar = 0
    tar_i = 0
    x = listA[tar][1]
    y = listA[tar][2]
    route.append(tar) 
    listA.pop(tar-1)

    while(len(listA)>1):
        min = 10000000
        for i in range (len(listA)):
            if distance(x,y,listA[i][1],listA[i][2]) < min:
                min = distance(x,y,listA[i][1],listA[i][2])
                tar = listA[i][0]
                tar_i = i
        route.append(tar)
        x = listA[tar_i][1]
        y = listA[tar_i][2]
        listA.pop(tar_i)

    route.append(listA[0][0])


def random_route(route, listA, list_num):
    for i in  range(list_num):
        tar=random.randint(0,list_num-i-1)
        route.append(listA[tar][0])
        listA.pop(tar)

    
def insert_neighbor_evaluation(route,listA,a,b):
    sum_A = 0
    sum_B = 0
    a_p = a +1 
    a_m = a -1
    list_num = len(route)
    b_p = b + 1
    b_m = b-1
    if a_p >= list_num:
        a_p = 0
    if a == 0:
        a_m = list_num - 1
    if b_p >= list_num:
        b_p = 0
    if b == 0:
        b_m = list_num - 1

    if a < b:
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])

        sum_B += distance(listA[route[a_p]-1][1] , listA[route[a_p]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b]-1][1] , listA[route[b]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
    
    else:
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])

        sum_B += distance(listA[route[a_p]-1][1] , listA[route[a_p]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b]-1][1] , listA[route[b]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])

    return sum_B - sum_A


def swap_neighbor_evaluation(route,listA,a,b):
    
    sum_A = 0
    sum_B = 0
    a_p = a +1 
    a_m = a -1
    list_num = len(route)
    b_p = b + 1
    b_m = b-1
    if a_p >= list_num:
        a_p = 0
    if a == 0:
        a_m = list_num - 1
    if b_p >= list_num:
        b_p = 0
    if b == 0:
        b_m = list_num - 1

    if b-a == 1 :
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
        sum_B += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
    
    elif a == 0 and b == list_num-1:
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])
        sum_B += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])

    else:
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
        sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])

        sum_B += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[a_m]-1][1] , listA[route[a_m]-1][2])
        sum_B += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
        sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b_m]-1][1] , listA[route[b_m]-1][2])

    return sum_B - sum_A


def swap_two_opt(route,listA,a,b):
    sum_A = 0
    sum_B = 0
    a_p = a +1 
    list_num = len(route)
    b_p = b + 1
    if a_p >= list_num:
        a_p = 0
    if b_p >= list_num:
        b_p = 0
    sum_A += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[a_p]-1][1] , listA[route[a_p]-1][2])
    sum_A += distance(listA[route[b]-1][1] , listA[route[b]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])
    
    sum_B += distance(listA[route[a]-1][1] , listA[route[a]-1][2], listA[route[b]-1][1] , listA[route[b]-1][2])
    sum_B += distance(listA[route[a_p]-1][1] , listA[route[a_p]-1][2], listA[route[b_p]-1][1] , listA[route[b_p]-1][2])

    return sum_B - sum_A


def insert_two_opt(route,a,b):
    a = a +1 
    list_num = len(route)
    b = b 
    if a >= list_num:
        a = 0
    if b >= list_num:
        b = 0
    while(1):
        tmp = route[a]
        route[a] = route[b]
        route[b] = tmp

        a+=1
        b-=1
        if a >= list_num:
            a = 0
        if b < 0:
            b = list_num-1 
        
        if  (b < a and a == b+1) or (a == b):
            break;
        if a == list_num-1 and b == 0:
            tmp = route[a]
            route[a] = route[b]
            route[b] = tmp
            break;
        

def get_total_distance(list_copy,route):
    total_distance = 0 
    for i in range (len(list_copy)-1):
        total_distance = total_distance + distance(list_copy[route[i]-1][1], list_copy[route[i]-1][2], list_copy[route[i+1]-1][1], list_copy[route[i+1]-1][2]) 
    total_distance = total_distance + distance(list_copy[route[len(list_copy)-1]-1][1], list_copy[route[len(list_copy)-1]-1][2], list_copy[route[0]-1][1], list_copy[route[0]-1][2]) 
    return total_distance


def loop_two_opt(route,list_copy):
    list_num = len(route)
    change_count = 0
    end_count = 0
    tar = 0
    i_count = 0

    while(end_count != list_num):
        if tar >= list_num:
            tar =0

        insert_to = tar + i_count + 3

        if insert_to >= list_num:
            insert_to -= list_num
        if abs(insert_to - tar) <3 :
            i_count = 0
            end_count += 1
            tar +=1
            continue;
        if swap_two_opt(route,list_copy,tar,insert_to) < 0:
            insert_two_opt(route,tar,insert_to)
            change_count += 1
            end_count = 0
            tar += 1
            i_count = 0
        else:
            i_count +=1


def double_blidge(route,a,b,c,d):
    num_list = []
    num_list.append(a)
    num_list.append(b)
    num_list.append(c)
    num_list.append(d)
    num_list.sort()
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]
    d = num_list[3]

    list_num = len(route)
    a_p = a+1
    b_p = b+1
    c_p = c+1
    d_p = d+1
    if a_p >= list_num:
        a_p = 0
    if b_p >= list_num:
        b_p = 0
    if c_p >= list_num:
        c_p = 0
    if d_p >= list_num:
        d_p = 0
    
    tar = 0
    result_list = []

    tar = c_p
    while(tar != d):
        result_list.append(route[tar])
        tar+=1
        if tar >= list_num:
            tar = 0
    result_list.append(route[tar])
    
    tar = b_p
    while(tar != c):
        result_list.append(route[tar])
        tar+=1
        if tar >= list_num:
            tar = 0
    result_list.append(route[tar])
    
    tar = a_p
    while(tar != b):
        result_list.append(route[tar])
        tar+=1
        if tar >= list_num:
            tar = 0
    result_list.append(route[tar])

    tar = d_p
    while(tar != a):
        result_list.append(route[tar])
        tar+=1
        if tar >= list_num:
            tar = 0
    result_list.append(route[tar])

    for i in range(list_num):
        route[i] = result_list[i]


def list_copy_move(a,b):
    list_num = len(a)
    for i in range(list_num):
        a[i] = b[i]

if __name__ == '__main__':


    listA=[] #appendのために宣言が必要
    while True:
        try:
            listA.append(list(map(int,input().split())))

        except:
            break;
    list_copy = listA.copy()
    list_ram = listA.copy()
    list_num = len(list_copy)
    route = []

    #random_route(route,listA,list_num)
    nearest_n(route,listA)
    total_distance = get_total_distance(list_copy,route)

    change_count = 0
    loop_num = 10
    loop_list = route.copy()

    for i in range (loop_num):
        tar_1 = random.randint(0,list_num-1)
        tar_2 = random.randint(0,list_num-1)
        tar_3 = random.randint(0,list_num-1)
        tar_4 = random.randint(0,list_num-1)
        while(abs(tar_2-tar_1)<2 or abs(tar_3-tar_1)<2 or abs(tar_4-tar_1)<2 or abs(tar_2-tar_3)<2 or abs(tar_2-tar_4)<2 or abs(tar_4-tar_3)<2):
                
            tar_1 = random.randint(0,list_num-1)
            tar_2 = random.randint(0,list_num-1)
            tar_4 = random.randint(0,list_num-1)
            tar_3 = random.randint(0,list_num-1)

        double_blidge(loop_list,tar_1,tar_2,tar_3,tar_4)
        loop_two_opt(loop_list,list_copy)
        if total_distance > get_total_distance(list_copy,loop_list):
            list_copy_move(route,loop_list)
            total_distance = get_total_distance(list_copy,loop_list)
            print("new_score! ",total_distance)
            change_count +=1
        print(i)

    total_distance = get_total_distance(list_copy,route)

    print("評価値", int(total_distance))
    print("交換回数",change_count)

    route_x = []
    route_y = []


    for i in range (len(list_copy)):
        route_x.append(list_copy[route[i]-1][1])
        route_y.append(list_copy[route[i]-1][2])
    route_x.append(list_copy[route[0]-1][1])
    route_y.append(list_copy[route[0]-1][2])

    plt.plot(route_x, route_y)
    plt.scatter(route_x, route_y, color = "b", label="score")
    plt.show()