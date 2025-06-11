def validate_python_code(code: str, name_func: str, test_cases: list) -> tuple[bool, str]:
    namespace = {}
    try:
        exec(code, namespace)
    except Exception as e:
        return False, f"Error in code execution: {str(e)}"

    func = namespace.get(name_func)
    if not func:
        return False, f"Function '{name_func}' not found in the provided code."

    for case in test_cases:
        entrada = case["inputs"]
        esperado = case["expected"]
        try:
            result = func(*entrada) if isinstance(entrada, (list, tuple)) else func(entrada)
            if result != esperado:
                return False, f"Test case {entrada} failed: expected {esperado}, got {result}"
        except Exception as e:
            return False, f"Error during test case execution: {str(e)}"

    return True, "All test cases passed."
