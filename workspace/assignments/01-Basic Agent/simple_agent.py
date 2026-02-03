"""
Jednoduchý AI Agent s OpenAI API a Tools
Demonstruje:
- Volání OpenAI API (GPT-4o)
- Definici custom tools (kalkulátor, převod teploty, konverze měny)
- Zpracování tool calls a fed zpět do modelu
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Načtení environment variables
load_dotenv()

# Inicializace OpenAI klienta
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# ============================================================================
# FUNKCE - Implementace nástrojů
# ============================================================================

def calculator(operation: str, num1: float, num2: float) -> dict:
    """Jednoduchá kalkulačka s operacemi: add, subtract, multiply, divide"""
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return {"error": "Division by zero not allowed"}
            result = num1 / num2
        else:
            return {"error": f"Unknown operation: {operation}"}
        
        return {"operation": operation, "num1": num1, "num2": num2, "result": result}
    except Exception as e:
        return {"error": str(e)}


def convert_temperature(value: float, from_unit: str, to_unit: str) -> dict:
    """Konverze teplot mezi Celsius, Fahrenheit a Kelvin"""
    try:
        # Normalizace jednotek
        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()
        
        # Prevod na Celsius (jako mezistupínek)
        if from_unit == "celsius" or from_unit == "c":
            celsius = value
        elif from_unit == "fahrenheit" or from_unit == "f":
            celsius = (value - 32) * 5/9
        elif from_unit == "kelvin" or from_unit == "k":
            celsius = value - 273.15
        else:
            return {"error": f"Unknown unit: {from_unit}"}
        
        # Prevod z Celsius na cílovou jednotku
        if to_unit == "celsius" or to_unit == "c":
            result = celsius
        elif to_unit == "fahrenheit" or to_unit == "f":
            result = celsius * 9/5 + 32
        elif to_unit == "kelvin" or to_unit == "k":
            result = celsius + 273.15
        else:
            return {"error": f"Unknown unit: {to_unit}"}
        
        return {
            "original_value": value,
            "original_unit": from_unit,
            "result": round(result, 2),
            "result_unit": to_unit,
        }
    except Exception as e:
        return {"error": str(e)}


def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """Vrací přibližný směnný kurz (mockovaná data)"""
    # Toto je zjednodušení - v praxi bychom použili API jako exchangerate-api.com
    rates = {
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09,
        ("USD", "CZK"): 24.50,
        ("CZK", "USD"): 0.041,
        ("EUR", "CZK"): 26.70,
        ("CZK", "EUR"): 0.0375,
        ("USD", "GBP"): 0.79,
        ("GBP", "USD"): 1.27,
    }
    
    key = (from_currency.upper(), to_currency.upper())
    rate = rates.get(key)
    
    if rate:
        return {
            "from": from_currency.upper(),
            "to": to_currency.upper(),
            "rate": rate,
            "note": "Aproximní kurz pro demo"
        }
    else:
        return {"error": f"Kurz pro {from_currency} -> {to_currency} není k dispozici"}


# ============================================================================
# DEFINICE TOOLS PRO OPENAI
# ============================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Kalkulačka pro základní matematické operace. Podporuje: add (sčítání), subtract (odčítání), multiply (násobení), divide (dělení)",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Matematická operace: 'add', 'subtract', 'multiply', 'divide'",
                        "enum": ["add", "subtract", "multiply", "divide"]
                    },
                    "num1": {
                        "type": "number",
                        "description": "První číslo"
                    },
                    "num2": {
                        "type": "number",
                        "description": "Druhé číslo"
                    }
                },
                "required": ["operation", "num1", "num2"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "convert_temperature",
            "description": "Konverze teploty mezi jednotkami: Celsius, Fahrenheit, Kelvin",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "Hodnota teploty"
                    },
                    "from_unit": {
                        "type": "string",
                        "description": "Zdrojová jednotka: 'celsius', 'fahrenheit', 'kelvin' (nebo 'c', 'f', 'k')"
                    },
                    "to_unit": {
                        "type": "string",
                        "description": "Cílová jednotka: 'celsius', 'fahrenheit', 'kelvin' (nebo 'c', 'f', 'k')"
                    }
                },
                "required": ["value", "from_unit", "to_unit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Vrací směnný kurz mezi dvěma měnami. Dostupné měny: USD, EUR, CZK, GBP",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_currency": {
                        "type": "string",
                        "description": "Zdrojová měna (např. 'USD', 'EUR', 'CZK')"
                    },
                    "to_currency": {
                        "type": "string",
                        "description": "Cílová měna (např. 'EUR', 'CZK', 'GBP')"
                    }
                },
                "required": ["from_currency", "to_currency"]
            }
        }
    }
]

# Mapování funkcí pro snadné volání
available_functions = {
    "calculator": calculator,
    "convert_temperature": convert_temperature,
    "get_exchange_rate": get_exchange_rate,
}


# ============================================================================
# AGENT LOGIKA
# ============================================================================

def run_agent(user_message: str, model: str = "gpt-4o") -> str:
    """
    Spustí agenta s daným uživatelským poselstvím.
    Agent může použít tools, aby odpověděl na otázku.
    """
    
    print(f"\n{'='*70}")
    print(f"USER: {user_message}")
    print(f"{'='*70}\n")
    
    # Inicializace conversation history
    messages = [
        {
            "role": "system",
            "content": "Jsi pomocný asistent. Máš k dispozici nástroje pro matematické operace, konverzi teplot a směnné kurzy. Když je to potřebné, používej tyto nástroje k odpovědi na otázky uživatele."
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
    
    # Smyčka pro iteraci s modelem a tools
    max_iterations = 5
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"[Iterace {iteration}]")
        
        # Zavolání OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        
        # Kontrola zda model chtěl zavolat nějaký tool
        if response_message.tool_calls:
            print(f"→ Model chtěl zavolat tools:\n")
            
            # Přidání asistentovy odpovědi do konverzace
            messages.append({
                "role": "assistant",
                "tool_calls": response_message.tool_calls,
                "content": ""
            })
            
            # Zpracování každého tool call
            tool_results = []
            for tool_call in response_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                tool_id = tool_call.id
                
                print(f"  Function: {tool_name}")
                print(f"  Arguments: {tool_args}")
                
                # Zavolání příslušné funkce
                function = available_functions[tool_name]
                function_result = function(**tool_args)
                
                print(f"  Result: {function_result}\n")
                
                # Uložení výsledku
                tool_results.append({
                    "tool_call_id": tool_id,
                    "name": tool_name,
                    "result": function_result
                })
            
            # Přidání tool results do konverzace
            for result in tool_results:
                messages.append({
                    "role": "tool",
                    "tool_call_id": result["tool_call_id"],
                    "name": result["name"],
                    "content": json.dumps(result["result"])
                })
        
        else:
            # Model vrátil konečnou odpověď bez tool call
            print(f"→ Model vrátil odpověď:\n")
            final_response = response_message.content
            print(f"ASSISTANT: {final_response}\n")
            return final_response
    
    return "Překročen maximální počet iterací."


# ============================================================================
# MAIN - Příklady
# ============================================================================

if __name__ == "__main__":
    # Příklad 1: Matematika
    run_agent("Kolik je 157 + 283?")
    
    # Příklad 2: Konverze teplot
    run_agent("Kolik stupňů Celsia je 98.6 Fahrenheitů?")
    
    # Příklad 3: Směnný kurz
    run_agent("Jaký je kurz z EUR na CZK?")
    
    # Příklad 4: Složitější otázka
    run_agent("Vypočítej 1500 děleno 12 a výsledek zaokrouhli na dvě desetinná místa.")
