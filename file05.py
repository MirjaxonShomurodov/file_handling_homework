def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    b=[]
    n=0
    a=0
    for i in range(len(data)):
        if data[i].isdigit()!=1:
           n+=1
        if data[i].isdigit()==1:
           a+=1
    return f"[{a},{n}]"

# Read data from file 

f=open('data/data05.txt').read()
print(main(f))