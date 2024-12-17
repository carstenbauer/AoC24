# lines = open(0).readlines()

# A = int(lines[0].strip().split(': ')[1])
# B = int(lines[1].strip().split(': ')[1])
# C = int(lines[2].strip().split(': ')[1])
# program = lines[4].strip().split(': ')[1]
# code = list(map(int, program.split(',')))

# def combo(operand, registers):
#     if 0<= operand <= 3:
#         return operand
#     elif operand == 4:
#         return registers[0]
#     elif operand == 5:
#         return registers[1]
#     elif operand == 6:
#         return registers[2]
#     elif operand == 7:
#         raise Exception("saw invalid operand 7")

# def execute(instptr, code, registers, out):
#     opcode = code[instptr]
#     operand = code[instptr+1]
#     # print(instptr, "->", opcode, operand, registers, out)
#     if opcode == 0: # adv
#         registers[0] = registers[0] >> combo(operand, registers)
#     elif opcode == 1: # bxl
#         registers[1] = registers[1] ^ operand
#     elif opcode == 2: # bst
#         registers[1] = combo(operand, registers) % 8
#     elif opcode == 3: # jnz
#         if not registers[0] == 0:
#             return operand
#     elif opcode == 4: # bxc
#         registers[1] = registers[1] ^ registers[2]
#     elif opcode == 5: # out
#         out.append(combo(operand, registers) % 8)
#     elif opcode == 6: # bdv
#         registers[1] = registers[0] >> combo(operand, registers)
#     elif opcode == 7: # cdv
#         registers[2] = registers[0] >> combo(operand, registers)
#     return instptr + 2

# def run(code, registers):
#     instptr = 0
#     out = []
#     while instptr < len(code)-1:
#         instptr = execute(instptr, code, registers, out)
#     return out

# print("Part I:", ','.join(map(str, run(code, [A,B,C]))))

# ## Part II

# def run_check(code, registers):
#     instptr = 0
#     out = []
#     while instptr < len(code)-1:
#         instptr = execute(instptr, code, registers, out)
#         for i in range(len(out)):
#             if not out[i] == code[i]:
#                 return out
#     return out

# for A in range(50000000):
#     out = run_check(code, [A,B,C])
#     if out == code:
#         break
# print("Part II:", A)
#
# Unfortunately, not directly brute-forcible....