import ast
code = 'print"Hello"'
def analyze_code(code):
    
    def check_python_syntax(code):
        try:
            ast.parse(code)
            valid = {
                "valid": True,
                "message": "Syntax is valid",
            }  
            return True, valid      
        except SyntaxError as e:
            error_message = {
                "valid": False,
                "message":e.msg,
                "line": e.lineno,
                "offset": e.offset,
            }
            return False, error_message
        
    is_valid, syntax_result = check_python_syntax(code)

    
    def cal_py_score(code):
        list_of_keywords = ['import','print','def','elif','False','True','None','lambda','yield','del']

        score = 0
        for keyword in list_of_keywords:
            if keyword in code:
                score += 1
        return score
    
    def cal_cpp_score(code):
        list_of_keywords = ['#include','cin','cout','iostream','std::','using namespace']
        score = 0
        for keyword in list_of_keywords:
            if keyword in code:
                score += 1
        return score
    
    def cal_c_score(code):
        list_of_keywords = ['scanf','printf','stdio','register', 'typedef', 'restrict', 'extern', 'goto', '_Atomic / _Thread_local' ]
        score = 0
        for keyword in list_of_keywords:
            if keyword in code:
                score += 1
        return score
    
    def cal_java_score(code):
        list_of_keywords = ['System.out.println','public static void main','String args[]', 'interface', 'transient', 'synchronized', 'volatile', 'native', 'strictfp', 'assert']
        score = 0
        for keyword in list_of_keywords:
            if keyword in code:
                score += 1
        return score
    
    def cal_javascript_score(code):
        list_of_keywords = ['console.log','function','var ','let ','const ', '===', '!==', 'async', 'await', 'Promise', 'document.getElementById', 'window.location','import.meta', 'export default', 'module.exports', 'require(', 'process.env', 'setTimeout', 'setInterval']
        score = 0
        for keyword in list_of_keywords:
            if keyword in code:
                score += 1
        return score
    
    py_score = cal_py_score(code)
    cpp_score = cal_cpp_score(code)
    c_score = cal_c_score(code)
    java_score = cal_java_score(code)
    javascript_score = cal_javascript_score(code)
    
    #Highest Score Detection
    scores = {
        "Python": py_score,
        "C++": cpp_score,
        "C": c_score,
        "Java": java_score,
        "JavaScript": javascript_score
    }
    
    highest_score = 0
    second_highest_score = 0
    detected_lang = None
    tie = False
    for language, score in scores.items():
            
            
        if(score > highest_score):
            second_highest_score = highest_score
            highest_score = score
            detected_lang = language
            tie = False
              
        elif(score == highest_score):
            tie = True
            
        elif(score > second_highest_score and score < highest_score):
            second_highest_score = score
    
    
    
    if(highest_score == 0 or tie):
        return "Ambiguous" , 0, None
        
    
    confidence = ((highest_score - second_highest_score) / highest_score) * 100 if highest_score > 0 else 0
    
    syntax_result = None
    if detected_lang == "Python":
        is_valid,syntax_result = check_python_syntax(code)
    return detected_lang, confidence, syntax_result
    