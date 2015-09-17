__author__ = 'Girish'


def longest_subpalindrome(text):
    if text =='' :return 0,0
    def length(slice):a,b =slice; return b-a
    candidates =[grow(text,start,end) for start in range(len(text)) for end in (start,start+1) if start !=end]
    return max(candidates,key=length)
def grow(text,start,end):
    while start >0 and end <len(text) and text[start-1].upper() == text[end].upper():
        start-=1; end+=1
    return start,end



print("girish"[longest_subpalindrome("girish")[0]:longest_subpalindrome("girish")[1]])