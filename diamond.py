#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# [0,1,2,3,4]
for i in range(5):
    print(" "*(5-i-1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()
# [0,1,2,3]
for i in range(5-1):
    print(" "*(i+1),end="")
    for j in range(5-i-1):
        print("* ",end="")
    print()