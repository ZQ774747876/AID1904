class ListHelper:
    @staticmethod
    def find(list_target, func):
        for item in list_target:
            if func(item):
                return item
    @staticmethod
    def skill_number01(list_target, func):
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count
    @staticmethod
    def atk_sum(list_target, func):
        """
         自定义类的列表求和
        :param list_target: 目标列表
        :param func: 自定义对象的处理逻辑
        :return: 总和
        """
        result = 0
        for item in list_target:
            result += func(item)
        return result


    #
    # def fun01(list_target):
    #     for item in list_target:
    #         if item.name=="如来神掌":
    #             return item
    # def fun02(list_target):
    #     for item in list_target:
    #         if item.atk>50:
    #             return item
    # def fun03(list_target):
    #     for item in list_target:
    #         if item.cd==0:
    #             return item
    #
    #
    # def condition01(item):
    #     return item.atk>50
    # def condition02(item):
    #     return  item.cd==0
    # def condition03(item):
    #     return  item.name=="如来神掌"





# def atk_sum(list_target,func):
#     result=0
#     for item in list_target:
#        result+=func(item)
#     return result
#[1,3,4,56,7,6,5,5]
#
# def func(item):
#    return item.atk

# def max_skill(list_target):
#     max=list_target[0]
#     for i in range(1,len(list_target)):
#         if list_target[i].atk>max.atk:
#             max=list_target[i]
#     return max
#
# def max_skill(list_target):
#     max = list_target[0]
#     for i in range(1, len(list_target)):
#         if list_target[i].speed > max.speed:
#             max = list_target[i]
#     return max


