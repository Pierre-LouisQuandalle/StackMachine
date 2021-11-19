class Stack:
    s = []
    def __init__(self):
        self.s = []
    
    def push(self, value):
        self.s.append(value)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    def __str__(self) -> str:
        return "{}".format(self.s)

def test_stack():
    stack = Stack()
    stack.push(3)
    stack.push(6)
    value = 6
    stack.push(value)
    assert stack.peek() == value
    top = stack.pop()
    assert top == value


def stack_machine(progamm, debug_mode = False):
    stack = Stack()

    if debug_mode:
        print("programme: ", progamm)

    for opcode in parse_program(progamm):
        match opcode:
            case 'OP_PLUS':
                stack.push(stack.pop() + stack.pop())
            case 'OP_MUL':
                stack.push(stack.pop() * stack.pop())
            case 'OP_NEGATE':
                stack.push(-1 * stack.pop())
            case 'OP_EQUAL':
                if stack.pop()==stack.pop():
                    stack.push(1)
                else : 
                    stack.push(0)
            case 'OP_MAX':
                stack.push(max(stack.pop(),stack.pop()))
            case _: 
                stack.push(opcode)
        
        if debug_mode:
            print("{}: {}".format(opcode,  stack))

    return stack.pop()

def test_machine():
    assert stack_machine("1 1 +") == 2
    assert stack_machine("1 2 +") == 3
    assert stack_machine("1 2 + 7 +") == 10
    assert stack_machine("1 2 + 3 *") == 9
    assert stack_machine("1 2 + 3 * -") == -9
    assert stack_machine("1 2 =") == 0
    assert stack_machine("1 1 =") == 1
    assert stack_machine("1 1 + 2 =") == 1
    assert stack_machine("4 44 max") == 44
    print('✔ All good!')

def parse_program(s):
    assoc = {
        '+': 'OP_PLUS',
        '*': 'OP_MUL',
        '-': 'OP_NEGATE',
        "=": "OP_EQUAL",
        "max": "OP_MAX",
    }
    return map(lambda elm: assoc[elm] if elm in assoc else int(elm), s.split())

test_stack()
test_machine()

import codecs
monprogramme = "372032202a2033202a202d202d"
print(stack_machine(codecs.decode(monprogramme, "hex").decode(), debug_mode=True))