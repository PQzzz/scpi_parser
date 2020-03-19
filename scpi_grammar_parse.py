from lark import Lark
from lark.lexer  import Token
from lark.tree import Tree

# program_message_unit：SCPI消息单元
# PROGRAM_MESSAGE_SEPARATOR：SCPI消息分隔符(;)
# execute_message_unit：SCPI执行消息单元
# query_message_unit：SCPI查询消息单元



class CommandInterpreter:
    SCPI_GRAMMAR = """
        start: program_message_unit ( PROGRAM_MESSAGE_SEPARATOR program_message_unit )*
        program_message_unit: execute_message_unit | query_message_unit
        execute_message_unit: execute_message_header ( program_data ( PROGRAM_DATA_SEPARATOR program_data )*)?
        query_message_unit: query_program_header ( program_data (PROGRAM_DATA_SEPARATOR program_data )*)?
        program_data :  SPECIFIC_PROGRAM_DATA
                        | INTEGER_NUMERIC_DATA UNIT_PROGRAM_DATA?
                        | DECIMAL_NUMERIC_PROGRAM_DATA UNIT_PROGRAM_DATA?
                        | OTHER_NUMERIC_DATA UNIT_PROGRAM_DATA?
                        | STRING_PROGRAM_DATA
                        | PATH_PROGRAM_DATA
                        | FILE_PROGRAM_DATA
                        
                        
        //                | suffix_program_data
        //                | arbitrary_block_program_data
        //                | expression_program_data

        execute_message_header: simple_execute_message_header 
                                | compound_execute_message_header 
                                | common_execute_message_header

        simple_execute_message_header: PROGRAM_MNEMONIC
        compound_execute_message_header: ":"? PROGRAM_MNEMONIC ( ":" PROGRAM_MNEMONIC )+
        common_execute_message_header: "*" PROGRAM_MNEMONIC

        query_program_header:   simple_query_program_header
                                | compound_query_program_header
                                | common_query_program_header

        simple_query_program_header: PROGRAM_MNEMONIC "?"
        compound_query_program_header: ":"? PROGRAM_MNEMONIC (":" PROGRAM_MNEMONIC)+ "?"
        common_query_program_header: "*" PROGRAM_MNEMONIC "?"


        //suffix_program_data: "/" (suffix_prog_data_with_mult | suffix_prog_data_without_mult ("/"|".")? )+
        //suffix_prog_data_with_mult: SUFFIX_MULT (SUFFIX_UNIT "-"? _DIGIT)?
        //suffix_prog_data_without_mult: SUFFIX_UNIT ("-"? _DIGIT)?
        //SUFFIX_MULT: "EX"|"PE"|"T"|"G"|"MA"|"K"|"M"|"U"|"N"|"P"|"F"|"A"
        //SUFFIX_UNIT: PROGRAM_MNEMONIC


        SPECIFIC_PROGRAM_DATA: "MIN" | "MAX" | "DEF"
        
        UNIT_PROGRAM_DATA: WORD

        INTEGER_NUMERIC_DATA: ("+"|"-")?  _DIGIT+ 

        OTHER_NUMERIC_DATA: "#" (( ("H"|"h") _HEX_DIGIT+ ) | (("Q"|"q") "0".."7"+ ) | (("B"|"b") ("0"|"1")+)) 

        STRING_PROGRAM_DATA: _SINGLE_QUOTED_STRING | _DOUBLE_QUOTED_STRING
        _SINGLE_QUOTED_STRING: "\'" ( "\'\'" | /[^']/ )* "\'"
        _DOUBLE_QUOTED_STRING: "\"" ( "\"\"" | /[^\\"]/ )* "\""

        DECIMAL_NUMERIC_PROGRAM_DATA: _MANTISSA ( _EXPONENT )? 
        _MANTISSA: ("+"|"-")? ( _DIGIT* "." _DIGIT+) | (_DIGIT+ "." _DIGIT*)
        _EXPONENT: ("E"|"e") ("+"|"-")? _DIGIT+
        _DIGIT: "0".."9"
        _HEX_DIGIT: "a".."f"|"A".."F"|"0".."9"

        
        PATH_PROGRAM_DATA: ("/" /[A-Za-z0-9_]+/)+ "/"?
        
        FILE_PROGRAM_DATA: ("/" /[A-Za-z0-9_]+/)* "/"? /[A-Za-z0-9_]+/ "." /[A-Za-z0-9_]+/
        
        
        PROGRAM_MESSAGE_SEPARATOR : ";"
        PROGRAM_DATA_SEPARATOR : ","
        PROGRAM_MNEMONIC : /[A-Za-z]+[A-Za-z0-9_]*/


        %import common.WS_INLINE
        %import common.DECIMAL
        %import common.WORD
        %ignore WS_INLINE
    """

    def __init__(self):
        self.parser = Lark(self.SCPI_GRAMMAR, parser='lalr', lexer="contextual")
        pass

    def process_line(self, command_string):
        # try:
        return self.parser.parse(command_string)
        # except:
        #     return "SCPI语法错误"

def tree_to_subtree(tree):
    subtree_list = []
    for subtree in tree.children:
        if type(subtree) == Tree:
            subtree_list.append(subtree)
    return subtree_list


def deep_travel_tree(root, node_list):
    if root is None:
        return
    if root.children:
        for node in root.children:
            if (type(node)==Token):
                node_list.append(node)
            elif (type(node)==Tree):
                deep_travel_tree(node, node_list)
    return node_list




if __name__ == '__main__':
    ci = CommandInterpreter()
    # print(ci.process_line(":CHA:AMPL:LENG? 123_a.mp3;:CHAN:ERR:COUNt?"))
    # root = ci.process_line(":CHAN:PATTern:LENG? 123_a.mp3;:CHAN:ERR:COUNt?").iter_subtrees()
    # for i in root:
    #     print(i)
    root = ci.process_line(":CHAn1:AMPLority 250mV;:CHAN2:PATT:LENG MIN;:CHAN3:RATE?".upper())

    subtree_list = tree_to_subtree(root)

    execute_cmd = []
    query_cmd = []
    for root in subtree_list:
        node_list = []
        node_list = deep_travel_tree(root, node_list)
        if root.children[0].data == "execute_message_unit":
            execute_cmd.append(node_list)
        elif root.children[0].data == "query_message_unit":
            query_cmd.append(node_list)

    print(execute_cmd)
    print(query_cmd)



