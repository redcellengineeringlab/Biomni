from biomni.agent import A1

def main():
    try:
        agent = A1(path='../data', llm='claude-sonnet-4-20250514')
        while True:
            print("Type something")
            q = input("> ").strip()
            if not q:
                continue
            elif q in ("/quit"):
                break
            
            res = agent.go(q)
            
            if isinstance(res, str):
                print(res)
    except Exception as e:
        print(f"There was an error {e}")
            
if __name__ == "main":
    main()
