"""
**dp[j]** means there is at least one way to be segmented from 0 to j

we expand the **i** in each iteration to find a way that dp[j] is true, and there is a word to fill in the segmentation of s[j:i]

In other word, find a **j** that s[0:j] can be segmented, and s[j:i] is in word_set
"""


def wordBreak(s: str, wordDict) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(len(dp)):
        for j in range(i):
            if dp[j] and s[j: i] in word_set:
                dp[i] = True
                break
    return dp[-1]