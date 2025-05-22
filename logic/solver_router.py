from logic.solver_eoq import solve_eoq
from logic.solver_breakeven import solve_breakeven

def solve_problem(text, problem_type):
    if problem_type == "eoq":
        return solve_eoq(text)
    elif problem_type == "break_even":
        return solve_breakeven(text)
    else:
        return "🚧 Dạng bài này chưa hỗ trợ trong bản demo.
This problem type is not yet supported in the demo."