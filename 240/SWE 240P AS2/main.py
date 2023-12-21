class Stack:                        # stack function emulated by list
    def __init__(self):
        self.stack = []

    def print_stack(self):
        print(f"{self.stack}")

    def push_stack(self,element):
        self.stack.append(element)

    def pop_stack(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


# stack = Stack()
# stack.push_stack(2)
# stack.push_stack(3)
# stack.push_stack(4)
# stack.push_stack(5)
# stack.pop_stack()
# print(f"peek return{stack.peek()}")
# stack.pop_stack()
# stack.print_stack()


# Python3 program to evaluate a given
# expression where tokens are
# separated by space.


# Function that returns value of
# expression after evaluation.
class EvalExpression():
    def __init__(self):
        pass
    # Function to find precedence
    # of operators.

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0          # brace 0

    # Function to perform arithmetic
    # operations.
    def applyOp(self,a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b


    def evaluate(self,tokens):
    # stack to store integer stack_operand.

        stack_operator = Stack()
        stack_operand = Stack()

    # stack to store operators.
        i = 0

        while i < len(tokens):

        # Current token is a whitespace,
        # skip it.
            if tokens[i] == ' ':
                i += 1
                continue

        # Current token is an opening
        # brace, push it to 'stack_operator'
            elif tokens[i] == '(':
                stack_operator.push_stack('(')

        # Current token is a number, push
        # it to stack for numbers.
            elif tokens[i].isdigit():

                val = 0

            # There may be more than one
            # digits in the number.
                while i < len(tokens) and tokens[i].isdigit():
                    val = (val * 10) + int(tokens[i])  # 1 10 100 digit
                    i += 1

                stack_operand.push_stack(val)   # add to operand stack

            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            # token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
                i -= 1

        # Closing brace encountered,
        # solve entire brace.
            elif tokens[i] == ')':
                #
                while stack_operator.size() != 0 and stack_operator.peek() != '(':
                    for element in stack_operator.stack:
                        if element != '(':
                            break
                        else:
                            stack_operand.push_stack("NaN")
                            break

                    val2 = stack_operand.pop_stack()
                    val1 = stack_operand.pop_stack()
                    op = stack_operator.pop_stack()
                    if val2 == 0 and op == "/":
                        stack_operand.push_stack("NaN")
                        break
                    elif type(val1) != int or type(val2) != int:
                        stack_operand.push_stack("NaN")
                        break
                    stack_operand.push_stack(self.applyOp(val1, val2, op))

            # pop opening brace
                stack_operator.pop_stack()

        # Current token is an operator.
            else:

            # While top of 'stack_operator' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'stack_operator'
            # to top two elements in stack_operand stack.
                while (stack_operator.size() != 0 and
                       self.precedence(stack_operator.peek()) >=
                       self.precedence(tokens[i])):
                    val2 = stack_operand.pop_stack()
                    val1 = stack_operand.pop_stack()
                    op = stack_operator.pop_stack()
                    if val2 == 0 and op == "/":
                        stack_operand.push_stack("NaN")
                        break
                    elif type(val1) != int or type(val2) != int:
                        stack_operand.push_stack("NaN")
                        break
                    stack_operand.push_stack(self.applyOp(val1, val2, op))

            # Push current token to 'stack_operator'.
                if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                    if stack_operand.peek() == "NaN":
                        break
                    stack_operator.push_stack(tokens[i])
                else:
                    stack_operand.push_stack("NaN")
                    break

            i += 1

    # Entire expression has been parsed
    # at this point, apply remaining stack_operator
    # to remaining stack_operand.
        while stack_operator.size() != 0 and stack_operand.peek() != "NaN":
            val2 = stack_operand.pop_stack()
            val1 = stack_operand.pop_stack()
            op = stack_operator.pop_stack()
            if val2 == 0 and op == "/":
                stack_operand.push_stack("NaN")
                break
            elif type(val1) != int or type(val2) != int:
                stack_operand.push_stack("NaN")
                break
            stack_operand.push_stack(self.applyOp(val1, val2, op))

    # Top of 'stack_operand' contains result,
    # return it.
        return stack_operand.peek()


# Driver Code
# if __name__ == "__main__":
#     print("eval test start --------------")
#     eval = EvalExpression()
#     print(eval.evaluate("10$ + 20 * 2"))
#     print(eval.evaluate(" 10 +  ( 2  *  5 ) "))
#     print(eval.evaluate("100 * 2 + 12"))
#     print(eval.evaluate("100 * ( 2 + 12 ) / 0"))
#     print("eval test end --------------")


# This code is contributed
# by Rituraj Jain


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.pop()
# print(f"the peek element of stack is {stack.peek()}")
# print(f"the length of stack is {stack.size()}")
# stack.print_stack()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.insert(0,element)

    def dequeue(self):
        return self.queue.pop()

    def poll(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)



# showcase
# queue = Queue()
#
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.dequeue()
# print(queue.poll())
# print(queue.size())
# print(queue.queue)



class StackWithTwoQs:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self,x):
        self.queue1.enqueue(x)

    def pop(self):
        while len(self.queue1.queue) >= 2:
            self.queue2.enqueue(self.queue1.dequeue())
        pop_head = self.queue1.queue   #mark the result and return at the end
        self.queue1 = self.queue2     # overwrite queue
        self.queue2 = Queue()    # re_initialized
        return pop_head

    def peek(self):
        while len(self.queue1.queue) >= 2:
            self.queue2.enqueue(self.queue1.dequeue())
        ret = self.queue1.poll()
        # print(f'element in swap queue: {self.queue2.queue}')
        self.queue2.enqueue(ret)
        self.queue1 = self.queue2
        self.queue2 = Queue()
        return ret

    def size(self):
        return len(self.queue1.queue)


swq = StackWithTwoQs()

swq.push(1)
swq.push(2)
swq.push(3)
swq.push(4)
print(f"push result {swq.queue1.queue}")
print(f"pop return {swq.pop()}")
print(f"current stack {swq.queue1.queue}")
print(f"stack peek {swq.peek()}")
print(f"current stack {swq.queue1.queue}")
print(f"stack size {swq.size()}")
print(f"current stack {swq.queue1.queue}")
swq.pop()
print(swq.queue1.queue)



