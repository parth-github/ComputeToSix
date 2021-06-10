import operator

number = range(1,10)

def operate(n, op1, op2):
  # operator precedence
  if op2 in [operator.mul, operator.floordiv] and op1 not in [operator.mul, operator.floordiv] :
    op1_result = int(op2(n,n))
    result = int(op1(n, op1_result))
  else:
    op1_result =int(op1(n,n))
    result = int(op2(op1_result, n))
  print(f"{op1_result}" + ":" + f"{result}")
  if result == 6:
    return True
  else: return False

ops = [('+', operator.add),
        ('-', operator.sub), 
        ('*', operator.mul),
        ('/', operator.floordiv)]
        #('sqrt', math.pow)]
        
for num in number:
  print(f"####{num}####")
  for op1 in ops:
    for op2 in ops:
      if operate(num, op1[1], op2[1]) == True:
        print(f"{num} " +  op1[0] + f" {num} " + op2[0]+ f" {num} " + " = 6")
