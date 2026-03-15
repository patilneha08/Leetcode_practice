from collections import defaultdict
from collections import Counter
import LIST

#Two Sum
def twosum(nums,target):
    h={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in h:
            return [h[diff],i]
        h[n]=i
    return
n=[2,3,4,5]
t=6
print(twosum(n,t))

#Contains Duplicate
def containsduplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
n=[3,2,5,6,6,3]
containsduplicate(n)

def containsduplicate(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False

#Valid Anagram
def validanagram(s1,s2): #Using sorted function
    return sorted(s1)==sorted(s2)


def validAnagram(self, s: str, t: str) -> bool: #Using hashmaps
    counts,countt={},{}
    if len(s)!=len(t):
        return False
    for i in range(len(s)): #setup the hash table
        counts[s[i]] = 1 + counts.get(s[i],0)
        countt[t[i]] = 1 + countt.get(t[i],0)
    for c in counts.keys():
        if counts[c]!=countt.get(c,0):
            return False
    return True

#Group Anagram
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())

#Top k Frequent Elements
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    c=Counter(nums)
    l=[]
    for i in c.most_common(k):
        l.append(i[0])
    return l

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

#Encode and Decode Strings
def encode(self, strs: List[str]) -> str:
    new=''
    for s in strs:
        new=new+str(len(s))+'#'+s
    return new
    

def decode(self, s: str) -> List[str]:
    l,i=[],0
    while i<len(s):
        j=i
        while s[j]!='#':
            j+=1
        length=int(s[i:j])
        l.append(s[j+1:j+length+1])
        i=j+length+1
    return l

#Product of Array except self
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res=[1]*len(nums)
    prefix=1
    for i in range(len(nums)):
        res[i]=prefix
        prefix=prefix*nums[i]
    postfix=1
    for j in range(len(nums)-1,-1,-1):
        res[j]=res[j]*postfix
        postfix=postfix*nums[j]
    return res

#Valid Sudoku
def isValidSudoku(self, board: List[List[str]]) -> bool:
    row=collections.defaultdict(set)
    col=collections.defaultdict(set)
    block=collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c]=='.':
                continue
            if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in block[(r//3,c//3)]:
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            block[(r//3,c//3)].add(board[r][c])
    return True

#Longest consecutive sequence
def longestConsecutive(self, nums: List[int]) -> int:
    nums=set(nums)
    longest=0
    for n in nums:
        if n-1 not in nums:
            length=0
            while(n+length) in nums:
                length+=1
            longest=max(length,longest)
    return longest

#Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True

    def alphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))

#Two sum II
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i,j=0,len(numbers)-1
    while i<j:
        cur=numbers[i]+numbers[j]
        if cur>target:
            j-=1
        elif cur<target:
            i+=1
        else:
            return [i+1,j+1]

#3 Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if n==nums[i-1] and i>0:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                cur=n+nums[l]+nums[r]
                if cur<0:
                    l+=1
                elif cur>0:
                    r-=1
                elif cur==0:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res

#Container with Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1
        while l<r:
            val=min(height[r],height[l])*(r-l)
            res=max(val,res)
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return res

#Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:  #Solution 1
        res=0
        maxl=[0]*len(height)
        maxr=[0]*len(height)
        minlr=[0]*len(height)
        maxln,maxrn,minlrn=0,0,0
        for i in range(len(height)):
            maxl[i]=maxln
            if height[i]>maxln:
                maxln=height[i]
        for j in range(len(height)-1,-1,-1):
            maxr[j]=maxrn
            if height[j]>maxrn:
                maxrn=height[j]
        for k in range(len(height)):
            minlr[k]=min(maxl[k],maxr[k])
            c=minlr[k]-height[k]
            if c>0:
                res+=c
            else:
                res+=0
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r=0,len(height)-1
        maxl,maxr=height[l],height[r]
        res=0
        while l<r:
            if maxl<=maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=maxr-height[r]
        return res

#Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        h={')':'(',']':'[','}':'{'}
        for i in s:
            if i in h:
                if stack and stack[-1]==h[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
    
#Min Stack
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        i=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(i)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

#Eavluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                total=stack.pop()+stack.pop()
                stack.append(total)
            elif i=='-':
                total=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            elif i=='*':
                total=stack.pop()*stack.pop()
                stack.append(total)
            elif i=='/':
                total=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(total)
            else:
                stack.append(int(i))
        return stack[-1]

#daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                StackInd,StackTemp=stack.pop()
                res[StackInd]=(i-StackInd)
            stack.append([i,t])
        return res
    
#Binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+((r-l)//2) #l is added so that the mid shifts towards the actual mid value
            if target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            elif target==nums[mid]:
                return mid
        return -1
    

#Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l,r=0,len(i)-1
            while l<=r:
                m=l+(r-l)//2
                if target>i[m]:
                    l=m+1
                elif target<i[m]:
                    r=m-1
                else:
                    return True
        return False