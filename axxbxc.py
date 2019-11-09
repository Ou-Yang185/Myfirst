import math

'''while True:
    try:
        text = input('plz input a b c, split with space: ')
        res = text.split(' ')
        a, b, c = [int(i) for i in res]
    except:
        pass
    else:
        break
'''
def function():
            text = input('plz input a b c, split with space: ')
            res = text.split(' ')
            a, b, c = [int(i) for i in res]
            delta = pow(b,2)-4*a*c
            if delta<0:
                print('no solve')
            elif delta == 0:
                print('only one answer:  ')
                x1=x2=float([(-b)+math.sqrt(pow(b,2)-4*a*c)]/(2*a))
                print('x1=x2=',x1)
            else:
                print("function's two answers:")
                x1=float(((-b)+math.sqrt(pow(b,2)-4*a*c))/(2*a))
                x2=float(((-b)-math.sqrt(pow(b,2)-4*a*c))/(2*a))
                print('x1=',x1)
                print('x2=',x2)
def signal():
        function()
        sig=int(input('1 break，others continue:'))
        if sig==1:
            return;
        else:
            signal()
if __name__=="__main__":
    signal()
