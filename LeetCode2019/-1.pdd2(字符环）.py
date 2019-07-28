"""
字符串数组能否首尾相接构成环，[ abc, cdf, fga] -> true
"""

def isCharCircle(strs:list[str]):
    hDict = {}
    tDict = {}
    # 构成环 有 hDict == tDict, 但 hDict == tDict，却有可能出现 [abba, cddc] 这种构成自环的情况， 还需保证 每一对 h,t 不来自同一个字符串