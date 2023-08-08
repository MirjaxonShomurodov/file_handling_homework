def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    name=0
    for i in range(len(data)):
        if data[i].isdigit():
           l.append(data[i])
           i+=1
    return l  

# Read data from file 

f=open('data/data03.txt').read()
print(main(f))