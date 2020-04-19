欧几里得算法or辗转相除法

在python下使用递归实现


数学证明(不考虑含0的情况):

约数(divisor):若一整数a可被另一整数d整除, 则称d为a的一个约数(divisor)记作d|a

对于两正整数a, b(a>b)存在一最大公约数(greatest common divisor)使得a, b可被其整除

取a, b最大公约数记作gcd(a, b)

设d=gcd(a, b)

对于a, 有a = q * b + r

其中q = a // b

故r = a - q * b

因为d|a且d|b

故d|(a - q * b) = r

又因为此时有b>r，且b, r均为非负整数

则令a = b, b = r重复上述操作

当r = 0时所得的b即为最大公约数
