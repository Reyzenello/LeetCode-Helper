import requests
import json

# Replace with your actual Ollama API key
OLLAMA_API_KEY = 'your_ollama_api_key'
OLLAMA_API_URL = 'https://api.ollama.ai/v1/solve'

def get_ollama_solution(problem_statement):
    headers = {
        'Authorization': f'Bearer {OLLAMA_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'problem_statement': problem_statement
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def main():
    print("Welcome to the LeetCode Coding Partner!")
    print("Please enter your LeetCode problem statement (type 'exit' to quit):")

    while True:
        problem_statement = input("\nProblem statement: ")
        
        if problem_statement.lower() == 'exit':
            print("Goodbye!")
            break

        print("\nSending problem to Ollama for solution...")
        solution = get_ollama_solution(problem_statement)

        if 'error' in solution:
            print(f"Error: {solution['error']}")
        else:
            print("Solution received from Ollama:")
            print(json.dumps(solution, indent=4))

if __name__ == "__main__":
    main()
