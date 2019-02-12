from Q2Version import EnumResponse
import operator

'''
ASSUMPTIONS:
I assume in this case that the versions are always delimited by a period
I also assume that no negative versions can exist
'''

def compareVersion(v1, v2):
    splitV1 = v1.split('.')
    splitV2 = v2.split('.')

    #Pad the decimals before comparing
    while len(splitV1[len(splitV1)-1]) != len(splitV2[len(splitV2)-1]):
        if len(splitV1[1]) > len(splitV2[1]):
            splitV2[1]+="0"
        else:
            splitV1[1] += "0"

    if operator.gt(splitV1, splitV2):
        return EnumResponse.Response.GREATER
    if operator.lt(splitV1,splitV2):
        return EnumResponse.Response.LESSER
    return EnumResponse.Response.EQUAL
