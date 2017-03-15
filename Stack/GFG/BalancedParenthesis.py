from algorithmic_toolb.Stack.Stack import Stack
# http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


class BalancedParenthesis:
    def __init__(self):
        self.stack = Stack()
        self.parenthesis_dict = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        self.reverse_paren_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

    def traverse_string(self,parenthesis_string):
        print "Traversing=>",parenthesis_string
        unmatched=False
        for i in list(parenthesis_string):
            if self.parenthesis_dict.has_key(i):
                self.stack.push(i)
            else:
                popped_paren = self.stack.pop()

                if popped_paren==self.reverse_paren_dict[i]:
                    continue
                else:
                    unmatched=True

        if self.stack.size()!=0:
            unmatched=True

        if unmatched:
            print parenthesis_string," doesn't have matched parenthesis\n"
        else:
            print parenthesis_string, " have matched parenthesis\n"



bp = BalancedParenthesis()
bp.traverse_string("[()]{}{[()()]()}")
bp.traverse_string("[()]{}{[()()]()")
