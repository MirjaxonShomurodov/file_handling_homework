def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    sum=0
    for i in range(len(data)):
        if data[i].isdigit():
           l.append(data[i])
        a="".join(l)
        x=int(a)
        i=0
    while x>0:
           r=x%10
           r+=x
           x//=10
    return r

# Read data from file

f=open('data/data07.txt').read()

print(main(f))
    