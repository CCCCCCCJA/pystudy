class Solution:
    def findString(self, words, s) -> int:
        left, right = 0, len(words) - 1
        n = len(words)
        while left <= right:
            while left <= right and not words[left]:
                left += 1
            while left <= right and not words[right]:
                right -= 1
            if left > right:
                return -1
            mid = (left + right) // 2
            while mid >= left and not words[mid]:
                mid -= 1
            if words[mid] == s:
                return mid
            elif words[mid] > s:
                right = mid - 1
            else:
                left = mid + 1
        return -1


words = ["", "", "", "", "AbHSZkLKTnHBbchUaS", "", "", "", "", "", "", "", "", "", "", "", "Ag kFlfSmsAEMy", "",
         "AsKLCqP", "", "", "", "", "", "AwNHxnNNZG", "", "", "", "", "", "", "", "BPwnIg", "", "CTZVBhsbvQpKHn",
         "DbWXiVetWyFeDu", "", "", "", "", "DdVm", "", "", "", "", "EIXK", "EUzGOV", "", "FBLOHPrpE", "GHMqgmMCXLkEBgU",
         "", "HPDGLlVDt", "", "", "", "", "", "", "HfF", "", "", "", "ILzzRaXUzNieYll", "", "", "", "", "", "", "", "",
         "IXO", "", "", "", "", "JMsO", "", "", "", "", "", "", "", "", "", "", "", "JNqzgSHitHRhdauLMcJ", "",
         "JZkNLIvaG", "", "", "KwRVFXYVJiueHvDHRTaJ", "", "", "LDTWBS", "", "", "", "", "", "", "LYN", "", "", "", "",
         "", "", "", "LpgNAXXV cWNYTwxo", "", "", "", "", "", "", "", "", "", "LxWJTErsIjyXjfCqrK", "", "", "", "", "",
         "", "", "", "MlJUQNiISaxtt", "", "", "", "", "", "", "", "", "", "", "O", "", "", "", "", "", "", "",
         "OHyIQptaYAfinbkjT", "", "", "", "", "", "", "", "", "", "", "", "OcQIESYXEmdykm", "", "", "", "", "", "", "",
         "", "Ol utzavtJOrPIK", "", "", "", "", "QLy", "", "", "", "", "", "QQZriWTlYYJgdlWl", "", "", "", "", "",
         "QhHySgWDIJwFtYP", "", "", "", "", "", "", "", "", "", "QiqwcedXKkVHDulp", "", "", "", "", "",
         "QtSvWSREnaYrrscc", "RHHeBMEnG nUX", "", "", "", "", "", "", "", "", "", "S", "", "", "", "", "", "", "", "",
         "", "SoULoFHOumjYMArBdiW", "", "", "", "", "SqHyxrJVNkrNaZG", "", "", "", "", "", "", "", "ThyUiuy", "", "",
         "Tu ac", "", "", "", "", "", "", "", "", "", "UGoOqhdXVzKl", "", "", "", "", "UbmA", "", "", "", "", "", "",
         "", "", "", "", "UsJhUmDujiOTntftsx", "", "", "", "", "", "", "", "", "", "", "V", "", "", "", "", "", "", "",
         "WEHisFZW wgmmVL", "", "", "", "", "", "", "", "", "", "", "", "WayOichMZsXpvJF", "", "WxVmzLgGjGlZOJwdzRd",
         "", "", "WzMjbVe WqjHOZJi", "", "", "", "", "", "", "", "", "", "", "", "XBVQZDHQT", "", "", "", "", "",
         "XMnsPtB AuMzDv", "", "XRNgMvqmhfjSfVVOP", "", "", "", "", "", "", "", "", "", "XYNh", "", "", "", "YfT", "",
         "", "", "", "", "", "", "", "", "", "", "amPIKYDmkUtUtFznRSvy", "", "", "", "", "", "", "", "", "",
         "bSs H MHwtgkOUzc", "", "", "", "cZhtYPrq ZpxZ", "", "", "", "", "", "", "dUGjmZGq", "e", "", "", "", "", "",
         "", "", "", "", "eWp", "epctu", "", "", "", "", "", "", "", "", "ezTPGIKrUmY", "", "", "", "", "", "", "", "",
         "", "", "fDnxFNxYyzUdQLc", "", "", "", "", "", "", "fFq", "", "", "", "", "", "", "", "", "", "", "fVjbEkHHU",
         "", "", "", "", "", "", "fux", "", "", "", "", "", "", "", "", "", "", "fwNIhmjYGktBo", "", "", "", "", "", "",
         "gEw", "", "", "hCisHtVxXZLjazN", "", "", "iqtlVbWLc", "", "", "jgLIRdgwDIaXioxoQkJn", "", "jpfhmJLfe", "", "",
         "", "kJEFz", "", "", "", "", "", "", "", "", "", "", "kKGFNPRtWNMY", "", "", "", "", "", "", "", "kXsm YJ", "",
         "", "", "kxjNfp c", "", "", "", "", "lnHVOerQcvgQEbBH", "", "", "", "", "", "mBsZUwwGmIsTwBUG", "",
         "mDMENtWiZwu", "", "miuxyF VvYebav", "", "", "", "", "", "nMWP", "", "", "", "", "", "", "", "", "", "", "",
         "nVbrbTsffMvICzx", "", "", "", "nYQuyy", "", "neMPLcFrptsISrhXBWe", "", "", "", "", "", "", "", "", "",
         "oAhJcIL", "", "", "", "", "ptybFCyrvqgy", "", "", "", "qVMPHyOgzIexxZ", "", "", "", "", "", "", "",
         "qvxuleCVWTYeboMK", "qyJLPQMBUuEEkhI", "", "", "", "", "", "", "", "", "", "", "rOsUPq", "", "", "", "sp v",
         "tjABXGFKaX", "", "", "", "", "", "", "", "", "uCFtpnikffzpIGynu", "", "", "uUOuBVKFxs", "", "", "", "", "",
         "", "ukVV", "", "", "", "", "uoRyNsvADRrPlF", "", "", "vJEsAKrSc jrBnvb", "", "", "", "", "", "", "", "", "",
         "", "wKjM", "", "", "", "", "", "", "", "", "wfWltxcuOFs", "", "", "", "", "", "", "", "wrjXviwslafTEBrLBDcQ",
         "", "", "", "", "", "", "", "", "", "", "xqhYBOAEpUzGUDG", "", "", "", "", "", "", "", "", "", "", "y", "",
         "yEvRmNbkvfELjCvG", "", "", "", "", "", "", "z NBqViMo", "", "", "", "zhEOGXTiOsTMbzW", "", "", "", "", "",
         "zuaVLjhQhNdg"]
s = "WEHisFZW wgmmVL"
ss = Solution()
print(ss.findString(words, s))
