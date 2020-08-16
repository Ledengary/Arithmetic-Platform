import math
import traceback
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None
        self.value = None
        self.args = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def addLast(self, data, given_args=None, given_value=None):
        new_node = node(data)
        if given_value != None:
            new_node.value = given_value
        if len(given_args) != 0:
            new_node.args = given_args
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def update(self, data, given_args=None, given_value=None):
        new_node = node(data)
        if len(given_args) == 0:
            given_args = None
        current_node = self.head
        while current_node.next != None:
            if current_node.data == data:
                current_node.value = given_value
                current_node.args = given_args
                return
            current_node = current_node.next
        if self.tail.data == data:
            self.tail.value = given_value
            self.tail.args = given_args
            return

    def addFirst(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            after = self.head
            self.head = new_node
            new_node.next = after
            after.last = new_node
        self.size += 1

    def deleteLast(self):
        if self.size != 0:
            if self.size ==1:
                self.head = None
                self.tail = None
            else:
                last_node = self.tail
                before = last_node.last
                before.next = None
                self.tail = before
            self.size -= 1

    def deleteFirst(self):
        if self.size != 0:
            if self.size ==1:
                self.head = None
                self.tail = None
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
                self.size -= 1

    def getLast(self):
        if self.size != 0:
            return self.tail.data
        else:
            return "NULL"

    def getFirst(self):
        if self.size != 0:
            return self.head.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head == None and self.tail == None and self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = []
        current_node = self.head
        while current_node.next != None:
            the_list.append(current_node.data)
            current_node = current_node.next
        the_list.append(self.tail.data)
        return the_list

    def displayKeyValue(self):
        the_list = dict()
        current_node = self.head
        while current_node.next != None:
            the_list[current_node.data] = current_node.value
            current_node = current_node.next
        the_list[self.tail.data] = self.tail.value
        return the_list

    def displayKeyArgs(self):
        the_list = dict()
        current_node = self.head
        while current_node.next != None:
            the_list[current_node.data] = current_node.args
            current_node = current_node.next
        the_list[self.tail.data] = self.tail.args
        return the_list

class Queue:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def enqueue(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            if self.size == 1:
                returnable = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return returnable.data
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
                self.size -= 1
                return next_node.data
        else:
            return "NULL"

    def getFirst(self):
        if self.size != 0:
            return self.head.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head == None and self.tail == None and self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = []
        current_node = self.head
        while current_node.next != None:
            the_list.append(current_node.data)
            current_node = current_node.next
        the_list.append(self.tail.data)
        return the_list

class Stack:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def pop(self):
        if self.size != 0:
            if self.size == 1:
                returnable = self.tail
                self.head = None
                self.tail = None
                self.size -= 1
                return returnable.data
            else:
                to_be_popped_node = self.tail
                before = to_be_popped_node.last
                self.tail = before
                before.next = None
                self.size -= 1
                return to_be_popped_node.data
        else:
            return "NULL"

    def push(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def peek(self):
        if self.size != 0:
            return self.tail.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = []
        current_node = self.head
        while current_node.next != None:
            the_list.append(current_node.data)
            current_node = current_node.next
        the_list.append(self.tail.data)
        return the_list

def check_brackets(line):
    char_stack = Stack()
    for char in line:
        if char == "(":
            char_stack.push(char)
        elif char == ")":
            if char_stack.isEmpty() is True:
                return False
            char_stack.pop()
    return char_stack.isEmpty()

definitions = linked_list()

def check_define_syntax(line):
    if line.find("=") != -1 and line[6] == " ":
        line = line[7:]
        try:
            parts = line.split("=")
            parts[0] = parts[0].strip()
            parts[1] = parts[1].strip()
            if check_brackets(parts[0]) is True and check_brackets(parts[1]) is True:
                # print("Eligible")
                arguments_list = []
                if parts[0].find("(") == -1:
                    if parts[0] not in definitions.displayKeyValue():
                        definitions.addLast(parts[0], arguments_list, parts[1])
                    else:
                        definitions.update(parts[0], arguments_list, parts[1])
                else:
                    arguments = parts[0][parts[0].find("(") + 1:parts[0].find(")")]
                    arguments_list = arguments.split(",")
                    if parts[0] not in definitions.displayKeyValue():
                        definitions.addLast(parts[0][:parts[0].find("(")], arguments_list, parts[1])
                    else:
                        definitions.update(parts[0][:parts[0].find("(")], arguments_list, parts[1])
            else:
                print(">>err3 : wrong syntax3")
        except:
            print(">>err3 : wrong syntax2")
    else:
        print(">>err3 : wrong syntax1")

# a + b * c / d - e

def isOperator(check):
    if check == "+" or check == "-" or check == "*" or check == "/" or check == "^":
        return True
    else:
        return False

def check_if_its_just_a_single_number(input_line):
    if input_line is None:
        return
    for each_char in input_line:
        if each_char == "+" or each_char == "-" or each_char == "*" or each_char == "/" or each_char == "^":
            return False
    return True

def given_infix_to_list(given_infix):
    if check_if_its_just_a_single_number(given_infix) is True:
        return given_infix
    infix = []
    temp_char_type = "N/A"
    temp = ""
    print("------------------------------", given_infix, detecting_a_function(given_infix))
    if given_infix is None:
        return
    for each_char in given_infix:
        if temp_char_type == "N/A":
            temp = each_char
            if each_char.isdigit() is True:
                temp_char_type = "digit"
            if isOperator(each_char) is True:
                temp_char_type = "operator"
            if each_char == "(" or each_char == ")":
                temp = ""
                infix.append(each_char)
        else:
            if each_char == "(" or each_char == ")":
                infix.append(temp)
                infix.append(each_char)
                temp = ""
            else:
                if each_char.isdigit() is True:
                    if temp_char_type == "digit":
                        temp += each_char
                    else:
                        infix.append(temp)
                        temp_char_type = "digit"
                        temp = each_char

                if isOperator(each_char) is True:
                    if temp_char_type == "operator":
                        temp += each_char
                    else:
                        infix.append(temp)
                        temp_char_type = "operator"
                        temp = each_char
                if each_char == ".":
                    temp += each_char

    if len(infix) != 0:
        if infix[len(infix) - 1] != temp:
            infix.append(temp)
    infix = list(filter(None, infix))
    return infix

def infix_to_postfix(given_infix):
    if check_if_its_just_a_single_number(given_infix) is True:
        return given_infix
    if given_infix is None:
        return
    if given_infix[0] == "-":
        print("NEGATIVE NUMBER GIVEN !")
        return given_infix
    infix = given_infix_to_list(given_infix)
    infix = list(map(lambda x: "+" if x == "--" else x, infix))
    infix = list(map(lambda x: "+" if x == "++" else x, infix))
    print("INFIX :", infix)
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    itf_stack = Stack()
    postfix = []
    for token in infix:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "abcdefghijklmnopqrstuvwxyz" or token[0] in "0123456789":
            postfix.append(token)
        elif token == '(':
            itf_stack.push(token)
        elif token == ')':
            topToken = itf_stack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = itf_stack.pop()
        else:
            while (itf_stack.isEmpty() is False) and (prec[itf_stack.peek()] >= prec[token]):
                  postfix.append(itf_stack.pop())
            itf_stack.push(token)

    while not itf_stack.isEmpty():
        postfix.append(itf_stack.pop())
    return " ".join(postfix)

def calculate(number_one, number_two, operator):
    if operator == "+":
        return number_one + number_two
    elif operator == "-":
        return number_one - number_two
    elif operator == "*":
        return number_one * number_two
    elif operator == "/":
        return number_one / number_two
    elif operator == "^":
        return math.pow(number_one, number_two)

def evaluate_postfix(given_postfix):
    try:
        if given_postfix is None or len(given_postfix) == 0:
            return
        if given_postfix[0] == "-":
            return given_postfix
        postfix = given_postfix.split(" ")
        ep_stack = Stack()
        for each_ep in postfix:
            if each_ep[0].isdigit() is True:
                if str(each_ep).find(".") == -1:
                    ep_stack.push(int(each_ep))
                else:
                    ep_stack.push(float(each_ep))
            else:
                if isOperator(each_ep):
                    number_one = ep_stack.pop()
                    number_two = ep_stack.pop()
                    answer = calculate(number_two, number_one, each_ep)
                    ep_stack.push(answer)
        return ep_stack.pop()
    except Exception as ex:
        traceback.print_exc()
        print("EVALUATION FAILED")
        return None

def insert_to_function(function, insertable):
    functions = definitions.displayKeyValue()
    func_values = definitions.displayKeyArgs()
    second = functions[function]
    second_args = func_values[function]
    ins_parts = insertable.split(" ")
    answer = second
    ans_counter = 0
    for each_arg in second_args:
        answer = answer.replace(each_arg.strip(), ins_parts[ans_counter])
        ans_counter += 1
    answer = check_for_fake_brackets(answer)
    return answer

def check_for_completed_brackets(line):
    completed_stack = Stack()
    for each_char in line:
        if each_char == "(":
            completed_stack.push("(")
        elif each_char == ")":
            completed_stack.pop()
    return completed_stack.isEmpty()

def detecting_a_function(line):
    print("INPUT LINE :", line)
    start_point = 0
    detected_function_name = ""
    while line.find("(", start_point, len(line)) != -1:
        found_at = line.find("(", start_point, len(line))
        for i in range(found_at - 1, -1, -1):
            if line[i].isdigit() is False and isOperator(line[i]) is False:
                detected_function_name = line[i] + detected_function_name
            else:
                break
        if detected_function_name != "":
            return True
        else:
            dtc_stack = Stack()
            dtc_stack.push("(")
            for i_c_f in range(found_at + 1, len(line)):
                if line[i_c_f] == "(":
                    dtc_stack.push("(")
                elif line[i_c_f] == ")":
                    dtc_stack.pop()
                if dtc_stack.isEmpty() is True:
                    start_point = i_c_f + 1
                    break
    return False

def split_by_comma(inside_line):
    answer_list = []
    start_point = 0
    counter = 0
    for each_char in inside_line:
        if each_char == ",":
            if check_for_completed_brackets(inside_line[:counter]) is True:
                answer_list.append(inside_line[start_point:counter])
                start_point = counter + 1
        counter += 1
    start_point -= 1
    answer_list.append(inside_line[start_point+1:])
    print(answer_list)
    return answer_list

def calculate_function(function):
    functions = definitions.displayKeyValue()
    print(function, "!!!")
    answer = ""
    if function.find("(") != -1:
        detected_function_name = ""
        found_at = function.find("(")
        # detecting the function in a string of math commands
        for i in range(found_at - 1, -1, -1):
            if function[i].isdigit() is False and isOperator(function[i]) is False:
                detected_function_name = function[i] + detected_function_name
            else:
                break
        if detected_function_name != "":
            cf_stack = Stack()
            cf_stack.push("(")
            for i_c_f in range(function.find("(") + 1, len(function)):
                if function[i_c_f] == "(":
                    cf_stack.push("(")
                elif function[i_c_f] == ")":
                    cf_stack.pop()
                if cf_stack.isEmpty() is True:
                    inside_line = function[found_at + 1:i_c_f]
                    answer = inside_line
                    if inside_line.find(",") != -1:
                        parts = split_by_comma(inside_line)
                        comma_answers = ""
                        for each_comma in parts:
                            called = calculate_function(each_comma)
                            print("GOT", called, "--INNER BETWEEN--", detected_function_name)
                            comma_answers += " " + called
                        comma_answers = comma_answers[1:]
                        print(comma_answers, "...")
                        called = insert_to_function(detected_function_name, comma_answers)
                        called = str(evaluate_postfix(infix_to_postfix(called)))
                        answer = function[:function.find(detected_function_name)] + called + function[i_c_f + 1:]
                        # if detecting_a_function(answer) is True:
                        #     print("STILL")
                        #     answer = calculate_function(answer)
                        # answer = str(evaluate_postfix(infix_to_postfix(answer)))
                        print("ROLL BACK1 :", answer)
                    else:
                        called = calculate_function(inside_line)
                        print("GOT", called, "--INNER FUNCTION--", detected_function_name)
                        called = insert_to_function(detected_function_name, called)
                        print(called, "... 1")
                        called = str(evaluate_postfix(infix_to_postfix(called)))
                        print(called, "... 2")
                        answer = function[:function.find(detected_function_name)] + called + function[i_c_f + 1:]
                        # if detecting_a_function(answer) is True:
                        #     print("STILL")
                        #     answer = calculate_function(answer)
                        # answer = str(evaluate_postfix(infix_to_postfix(answer)))
                        print("ROLL BACK2 :", answer)
                    return answer
    else:
        answer = infix_to_postfix(function)
        print("check:", function, "answer:", answer)
        answer = str(evaluate_postfix(answer))
        print("Returnable Answer :", answer)
        return answer

def check_for_functions(line):
    functions = definitions.displayKeyValue()
    function_args = definitions.displayKeyArgs()
    print(functions, function_args)
    answer = calculate_function(line)
    while detecting_a_function(answer) is True:
        answer = calculate_function(answer)
    print("Final :", answer, ":)")
    return answer

def check_for_variables(line):
    print(line)
    answer = ""
    to_be_checked = ""
    variables_list = ""
    last_type = "N/A"
    counter = 0
    for each_char in line:
        if each_char in "abcdefghijklmnopqrstuvwxyz" or each_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if last_type == "char":
                to_be_checked += each_char
                last_type = "char"
            else:
                to_be_checked = each_char
                last_type = "char"
        else:
            if last_type == "char":
                if each_char != "(":
                    if to_be_checked != "":
                        variables_list += " " + to_be_checked + "_" + str(counter - len(to_be_checked))
                to_be_checked = ""
            else:
                last_type = "N/A"
        counter += 1
    if to_be_checked != "":
        variables_list += " " + to_be_checked + "_" + str(counter - len(to_be_checked))
    variables_list = variables_list[1:]
    print(variables_list)
    if variables_list != "":
        variables_list_parts = variables_list.split(" ")
        defined_variables = definitions.displayKeyValue()
        counter = 0
        start_point = 0
        for each_one in variables_list_parts:
            parts = each_one.split("_")
            var = parts[0]
            var_index = int(parts[1])
            content = defined_variables[var]
            answer += line[start_point:var_index] + content
            start_point = var_index + len(var)
            if len(variables_list_parts) - 1 == counter:
                answer += line[start_point:]
            counter += 1
        print(answer)
        return answer
    else:
        return line

# print(check_for_variables("1+yes+23-no+1/no"))

def find_starting_and_ending_brackets(line):
    finding_stack = Stack()
    start_from = 0
    found_at = line.find("(", start_from, len(line))
    counter = found_at
    for each_char in line[found_at:]:
        if each_char == "(":
            finding_stack.push("(")
        elif each_char == ")":
            finding_stack.pop()
        if finding_stack.isEmpty() is True:
            temp = [found_at, counter]
            return  temp
        counter += 1
    return -1

def check_for_fake_brackets(line):
    commands_list = []
    brackets_stack = Stack()
    start_from = 0
    while line.find("(", start_from, len(line)) != -1:
        found_at = line.find("(", start_from, len(line))
        counter = found_at
        for each_char in line[found_at:]:
            if each_char == "(":
                brackets_stack.push("(")
            elif each_char == ")":
                brackets_stack.pop()
            if brackets_stack.isEmpty() is True:
                commands_list.append(line[start_from:counter+1])
                start_from = counter + 1
                break
            counter += 1
    commands_list.append(line[start_from:])
    print(commands_list, "COMMANDS LIST")
    each_command_counter = 0
    for each_command in commands_list:
        if each_command.find("(") != -1:
            print(each_command, "CAME !")
            answer = each_command
            if each_command.find("(") == 0:
                # then we have found a olaviat dar command in brackets !!!
                infos = find_starting_and_ending_brackets(each_command)
                called = calculate_function(each_command[infos[0]+1:infos[1]])
                called = str(evaluate_postfix(infix_to_postfix(called)))
                answer = called
            else:
                if isOperator(each_command[each_command.find("(") - 1]) is True \
                        or each_command[each_command.find("(") - 1] == "(":
                    # then we have found a olaviat dar command in brackets !!!
                    infos = find_starting_and_ending_brackets(each_command)
                    called = calculate_function(each_command[infos[0]+1:infos[1]])
                    called = str(evaluate_postfix(infix_to_postfix(called)))
                    answer = each_command[:infos[0]] + called + each_command[infos[1]+1:]
            commands_list[each_command_counter] = answer
            each_command_counter += 1
    print("___", commands_list, "___")
    return "".join(commands_list)

def check_print_syntax(line):
    if line[5] == " ":
        line = line[6:]
        if check_brackets(line) is True:
            # check if there is a function to be calculated first !
            # if there is, first calculate it and clear the string up with the right amount of the function1
            # either way, at the last part, convert the given infix string to postfix and then evaluate it !
            print("-------------------------CHECKING BRACKETS-------------------------------", line)
            line = check_for_fake_brackets(line)
            print("-------------------------CHECKING VARIABLES-------------------------------", line)
            line = check_for_variables(line)
            print("-------------------------CHECKING FUNCTIONS-------------------------------", line)
            line = check_for_functions(line)
            print("-------------------------FINAL ANSWER-------------------------------------")
            line = evaluate_postfix(infix_to_postfix(line))
            print(line, ".")
    else:
        print(">>err3 : wrong syntax1")

def statement_founder(variable, given_list):
    variable_statement = []
    non_variable_statement = []
    if variable in given_list:
        index_to_test = given_list.index(variable)
        if index_to_test != 0:
            if given_list[index_to_test - 1] == '*':
                if index_to_test - 3 >= 0:
                    variable_statement = given_list[index_to_test - 3:index_to_test + 1]
                    non_variable_statement = given_list[:index_to_test - 3] + given_list[index_to_test + 1:]
                else:
                    variable_statement = ['+'] + given_list[index_to_test - 2:index_to_test + 1]
                    non_variable_statement = ['+'] + given_list[:index_to_test - 2] + given_list[index_to_test + 1:]
            else:
                variable_statement = given_list[index_to_test - 1:index_to_test + 1]
                non_variable_statement = given_list[:index_to_test - 1] + given_list[index_to_test + 1:]
        else:
            variable_statement = ['+'] + given_list[0]
            non_variable_statement = given_list[1:]
    else:
        non_variable_statement = given_list
    answers_list = [variable_statement, non_variable_statement]
    print("ANSWERS_LIST :", answers_list)
    return answers_list

def second_equation_solver(variable, key_list, value_list):
    # variable_statement = []
    # non_variable_statement = []
    # index_to_test = key_list.index(variable)
    # if index_to_test != 0:
    #     if key_list[index_to_test - 1] == '*':
    #         variable_statement = key_list[index_to_test - 2:index_to_test + 3]
    #         non_variable_statement = key_list[:index_to_test - 2] + key_list[index_to_test + 3:]
    #     else:
    #         variable_statement = key_list[index_to_test:index_to_test + 3]
    #         non_variable_statement = key_list[:index_to_test] + key_list[index_to_test + 3:]
    # else:
    #     variable_statement = key_list[0:3]
    #     non_variable_statement = key_list[3:]
    # print(variable_statement, non_variable_statement)
    pass

def first_equation_solver(variable, key_list, value_list):
    print("FIRST !", key_list, value_list)
    key_variable_statement = statement_founder(variable, key_list)[0]
    key_non_variable_statement = statement_founder(variable, key_list)[1]
    value_variable_statement = statement_founder(variable, value_list)[0]
    value_non_variable_statement = statement_founder(variable, value_list)[1]
    print("KEY :", key_variable_statement, key_non_variable_statement)
    print("VALUE :", value_variable_statement, value_non_variable_statement)
    key_non_variable_statement_answer = evaluate_postfix(infix_to_postfix("".join(key_non_variable_statement)))
    value_non_variable_statement_answer = evaluate_postfix(infix_to_postfix("".join(value_non_variable_statement)))
    statement_answer = str(value_non_variable_statement_answer - key_non_variable_statement_answer)
    if statement_answer[0] != '-':
        statement_answer = '+' + statement_answer
    variable_answer = ""
    key_variable_statement_called = []
    value_variable_statement_called = []
    if len(value_variable_statement) != 0:
        if value_variable_statement[0] == '+':
            value_variable_statement[0] = '-'
        elif value_variable_statement[0] == '-':
            value_variable_statement[0] = '+'
    if len(key_variable_statement) == 2:
        key_variable_statement = key_variable_statement[0] + '1' + '*' + key_variable_statement[1]
    if len(value_variable_statement) == 2:
        value_variable_statement = value_variable_statement[0] + '1' + '*' + value_variable_statement[1]
    if len(value_variable_statement) != 0:
        value_variable_statement_called = value_variable_statement[:value_variable_statement.index(variable) - 1]
    key_variable_statement_called = key_variable_statement[:key_variable_statement.index(variable) - 1]
    value_variable_statement_called = value_variable_statement_called
    variable_answer = key_variable_statement_called + value_variable_statement_called
    print("STATEMENT_ANSWER :", statement_answer)
    print(key_variable_statement, value_variable_statement)
    print(key_variable_statement[:key_variable_statement.index(variable) - 1], value_variable_statement_called)
    if variable_answer[0] == '-':
        variable_answer = "1" + "".join(variable_answer) + "-1"
    else:
        variable_answer = variable_answer[1:]
    variable_answer = evaluate_postfix(infix_to_postfix(variable_answer))
    print("variable_answer :", variable_answer)
    cleared_statement = str(variable_answer) + "*" + variable + "=" + "".join(value_variable_statement_called)
    print("CLEARED_STATEMENT :", cleared_statement)
    variable_answer = str(variable_answer)
    secondary_answer = "".join(value_variable_statement_called)
    print(variable_answer, secondary_answer)
    final_answer = ""
    if (variable_answer[0] == '-' and secondary_answer[0] == "+") or (variable_answer[0] == '+' and secondary_answer[0] == "-"):
        final_answer = "-" + str(evaluate_postfix(infix_to_postfix(secondary_answer[1:] + "/" + variable_answer[1:])))
    if variable_answer[0] == '-' and secondary_answer[0] == "-":
        final_answer = "+" + str(evaluate_postfix(infix_to_postfix(secondary_answer[1:] + "/" + variable_answer[1:])))
    print(str(variable + " = " + final_answer))

def check_if_type_is_mutual(type_one, type_two):
    if type_one == type_two:
        return True
    else:
        return False

def commands_to_list(key):
    if True:
        numcom_list = []
        temp = key[0]
        temp_type = "N/A"
        if key[0].isdigit():
            temp_type = "digit"
        else:
            temp_type = "operator"

        for each_char in key[1:]:
            if each_char.isdigit() is True:
                if check_if_type_is_mutual(temp_type, "digit"):
                    temp += each_char
                else:
                    numcom_list.append(temp)
                    temp = each_char
                    temp_type = "digit"
            else:
                if isOperator(each_char) is True:
                    # we got an operatorend(temp)
                    numcom_list.append(temp)
                    temp = each_char
                    temp_type = "operator"
                else:
                    if each_char != "(" and each_char != ")":
                        # we got the variable name
                        if check_if_type_is_mutual(temp_type, "variable"):
                            temp += each_char
                        else:
                            numcom_list.append(temp)
                            temp = each_char
                            temp_type = "variable"
        numcom_list.append(temp)
        return numcom_list

def check_for_equation(variable, key_list):
    print(key_list)
    try:
        power_index = key_list.index("^")
        start_from = 0
        while power_index != -1:
            if key_list[power_index - 1] == variable:
                return 2
            else:
                start_from = power_index + 1
                power_index = key_list.index("^", start_from, len(key_list))
    except:
        return 1
    return 1

def check_solve_syntax(line):
    if line.find("=") != -1 and line[5] == " ":
        line = line[6:]
        if check_brackets(line) is True:
                parts = line.split("=")
                parts[0] = parts[0].strip()
                parts[1] = parts[1].strip()
                parts_0_inner = parts[0].split(" ")
                variable = parts_0_inner[0]
                parts[0] = parts_0_inner[1]
                if check_brackets(parts[0]) is True and check_brackets(parts[1]) is True:
                    print("VARIABLE", variable)
                    print("ONE", parts[0])
                    print("TWO", parts[1])
                    key = parts[0]
                    value = parts[1]
                    if key.find(variable) != -1 or value.find(variable) != -1:
                        key_list = commands_to_list(key)
                        value_list = commands_to_list(value)
                        if check_for_equation(variable, key_list) == 2:
                            print("SECOND EQUATION DETECTED")
                            second_equation_solver(variable, key_list, value_list)
                        else:
                            print("FIRST EQUATION DETECTED")
                            first_equation_solver(variable, key_list, value_list)
                    else:
                        print(">>err3 : wrong syntax1")
                else:
                    print(">>err3 : wrong syntax3")
    else:
        print(">>err3 : wrong syntax1")

# print(check_solve_syntax("solve x 2^3-4*x+7=12+3*x"))
input_line = "#new"
check_define_syntax("define yes = 40")
check_define_syntax("define no = 30")
check_define_syntax("define damn(x) = 5")
check_define_syntax("define double(x,y) = x+y")
check_define_syntax("define triple(x,y,z) = x+1")
check_define_syntax("define f(x) = 1/(8-x)")

if input_line == "#new":
    while True:
        input_line = input()
        if input_line != "#end":
            if input_line.startswith("#"):
                input_line = input_line[1:]
                if input_line.startswith("define"):
                    check_define_syntax(input_line)
                elif input_line.startswith("print"):
                    check_print_syntax(input_line)
                elif input_line.startswith("solve"):
                    check_solve_syntax(input_line)
                elif input_line.startswith("new"):
                    print("new")
                elif input_line.startswith("end"):
                    break
                else:
                    print(">>err2 : undefined exp1")
            else:
                print(">>err3 : wrong syntax")
        else:
            break

# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# print(my_stack.display())
# print(my_stack.getSize())
# print(my_stack.pop())
# my_stack.push(3)
# print(my_stack.display())
# print(my_stack.getSize())

# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# print(my_queue.display())
# print(my_queue.dequeue())
# print(my_queue.display())
# print(my_queue.getSize())

# my_list = linked_list()
# my_list.addLast(1)
# my_list.addLast(2)
# my_list.addFirst(0)
# print(my_list.display())
# print("Last :", my_list.getLast())
# print("First :", my_list.getFirst())
# print(my_list.isEmpty())
# my_list.clear()
# print(my_list.isEmpty())
# my_list.getSize()