import math
from google.adk.tools import ToolContext



def find_related_info(tool_context: ToolContext, topic: str) -> dict:
    try:
        search_results = tool_context.search_memory(f"Information about {topic}")
        if search_results.results:
            print(f"Found {len(search_results.results)} memory results for '{topic}'")
            # Process search_results.results (which are SearchMemoryResponseEntry)
            top_result_text = search_results.results[0].text
            return {"memory_snippet": top_result_text}
        else:
            return {"message": "No relevant memories found."}
    except ValueError as e:
        return {"error": f"Memory service error: {e}"} # e.g., Service not configured
    except Exception as e:
        return {"error": f"Unexpected error searching memory: {e}"}



def calculate_unary_operation(x: float, operation: str) -> float:
    """
    Perform a unary math operation on a single number.

    Supported operations: 'sqrt', 'log', 'log10', 'sin', 'cos', 'tan',
                          'asin', 'acos', 'atan', 'abs', 'exp'

    Args:
        x (float): The operand
        operation (str): The name of the operation

    Returns:
        float: Result of the operation

    Raises:
        ValueError: If the operation is unsupported
        ValueError: If the input is invalid for the operation (e.g., log(-1))
    """
    if operation == 'sqrt':
        return math.sqrt(x)
    elif operation == 'log':
        return math.log(x)
    elif operation == 'log10':
        return math.log10(x)
    elif operation == 'sin':
        return math.sin(x)
    elif operation == 'cos':
        return math.cos(x)
    elif operation == 'tan':
        return math.tan(x)
    elif operation == 'asin':
        return math.asin(x)
    elif operation == 'acos':
        return math.acos(x)
    elif operation == 'atan':
        return math.atan(x)
    elif operation == 'abs':
        return abs(x)
    elif operation == 'exp':
        return math.exp(x)
    else:
        raise ValueError(f"Unsupported unary operation: {operation}")


def calculate_binary_operation(a: float, b: float, operator: str) -> float:
    """
    Perform a binary math operation on two numbers.

    Supported operators: +, -, *, /, %, **

    Args:
        a (float): First operand
        b (float): Second operand
        operator (str): One of '+', '-', '*', '/', '%', '**'

    Returns:
        float: Result of the operation

    Raises:
        ValueError: If an invalid operator is used
        ZeroDivisionError: If division by zero is attempted
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    elif operator == '%':
        if b == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % b
    elif operator == '**':
        return a ** b
    else:
        raise ValueError(f"Unsupported operator: {operator}")


def lookup_constant(name: str) -> str:
    constants = {
        "speed of light": {"symbol": "c", "value": 299_792_458, "unit": "m/s"},
        "gravitational constant": {"symbol": "G", "value": 6.67430e-11, "unit": "m^3 kg^-1 s^-2"},
        "planck constant": {"symbol": "h", "value": 6.62607015e-34, "unit": "J·s"},
        "elementary charge": {"symbol": "e", "value": 1.602176634e-19, "unit": "C"},
        "avogadro constant": {"symbol": "Nₐ", "value": 6.02214076e23, "unit": "mol⁻¹"},
        "boltzmann constant": {"symbol": "k", "value": 1.380649e-23, "unit": "J/K"},
        "gas constant": {"symbol": "R", "value": 8.314462618, "unit": "J/mol·K"},
        "acceleration due to gravity": {"symbol": "g", "value": 9.80665, "unit": "m/s²"},
        "pi": {"symbol": "π", "value": 3.1415926535, "unit": ""},
        "euler's number": {"symbol": "e", "value": 2.7182818284, "unit": ""}
    }

    name = name.lower().strip()
    for key, data in constants.items():
        if name in key or name == data["symbol"].lower():
            return f"{key.title()} ({data['symbol']}): {data['value']} {data['unit']}"

    return "Constant not found. Try a common name or symbol like 'c', 'g', or 'pi'."
