#练习：一段文字，在文字中可能存在括号配对错误的情况，要求写一段代码，去检测这段文字中有没有括号
#书写错误，括号包含{}[]()
from day02.sstack import *
txet="dsjhsdkja(s(dfhfkj}s[d}hf{i}u{s)eayhfdifsugyoiwaygoiyhioygfiesyesio"
parens="{}[]()"
left_parens="{[("
# 验证配对是否正确
opposite={'}':'{',']':'[',')':'('}
#负责提供便利列的括号
def parent(txet):
    i,txet_len=0,len(txet)
    while True:
    #循环遍历字符串，到结尾结束，遇到括号提供给ver
        while i<txet_len and txet[i] not in parens:
            i +=1
        if i>=txet_len:
            return
        else:
            yield  txet[i],i
            i+=1
def ver():
    for pr,i in parent(txet):
       if pr in left_parens:
           st.Push((pr,i))
       elif st.is_empty() or st.Pop()[0] !=opposite[pr]:
           print("unmatching is found at %d for %s"%(i,pr))

           break
    # for 循环正常结束
    else:
        if st.is_empty():
            print("ALL parenesas are matched")
        else:
            p=st.Pop()
        print("Unmatching is found at %d for %s "%(p[1],p[0]))





#主程序只负责做括号的验证
st=SStack()#初始化一个栈
ver()