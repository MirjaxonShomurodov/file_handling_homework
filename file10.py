def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    rows=data.split('\n')
    data=[]
    for i in rows[:-1]:
        data.append(i.split(','))
        s=len(data[0][0])
        return s
# Read data from file


f=open('data/data10.txt').read()
print(main(f))