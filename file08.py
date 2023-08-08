def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    for i in range(len(data)):
        if data[i].isdigit():
           l.append(data[i])
    a=max(l) 
    return a  

# Read data from file 

f=open('data/data08.txt').read()
print(main(f))