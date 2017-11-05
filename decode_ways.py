"""
Decode ways.

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"

char_map = {}
def decode_ways(string):
    queue = [(string,0)]
    result = []

    while len(queue) != 0:
        temp_string,pos = queue.pop(0)
        if pos == len(temp_string):
            result.append(temp_string)
        elif pos == len(temp_string) - 1:
            queue.append((temp_string[0:pos] + char_map[temp_string[pos]],pos+1))
        else :
            queue.append((temp_string[0:pos] + char_map[temp_string[pos]] + temp_string[pos+1:len(temp_string)],pos+1))
            queue.append((temp_string[0:pos] + char_map[temp_string[pos] + temp_string[pos+1]]+temp_string[pos+2:len(temp_string)],pos+1))

    return result


if __name__ == '__main__':

    temp = 97
    for i in range(1,26):
        char_map[str(i)] = chr(temp)
        temp += 1
    print(decode_ways("121212"))
