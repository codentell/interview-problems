

def contains_duplicate(blocks: bool) -> bool: 
    for i in range(0, len(blocks)-1):
        for j in range(i+1, len(blocks)):
            if blocks[i] == blocks[j]:
                return True
    return False

def main():
    print("Solution #1: Brute force way")
    blocks = [1,2,3,1]
    results = contains_duplicate(blocks)
    print(blocks)
    print(results)

if __name__ == "__main__":
    main()
