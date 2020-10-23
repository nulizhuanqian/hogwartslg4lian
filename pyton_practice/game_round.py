# -*_ coding: utf-8 -*-
# @Time     :2020/10/23 18:15
# @Author   :lian
# @File     :.py
"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""
# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    #我的初始血量
    my_hp = 1000
    #我的初始攻击
    my_power = 200
    #敌人的初始血量
    enemy_hp = 1000
    #敌人的初始攻击
    enemy_power = 199
    # 加入循环，让游戏可以进行多轮
    while True:
        #我的剩余血量=我的初始血量-敌人的攻击
        my_hp = my_hp - enemy_power
        #敌人的剩余血量=敌人的初始血量-敌人的攻击
        enemy_hp = enemy_hp - my_power
        #打印我的剩余血量
        print(my_hp)

        # 判断我的血量小于等于0
        if my_hp <= 0:
            print("我输了")
            # 满足条件跳出循环
            break
        #敌人的血量小于等于0
        elif enemy_hp <= 0:
            print("我赢了")
            break
#调用函数
fight()