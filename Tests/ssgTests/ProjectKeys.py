#
#
# template.py
#
# alternate template python test file
#
#
#
class ProjectKeys:

    keyData = [69, 55, 99, 81, 81, 81, 97, 97, 118, 101, 106, 76, 108, 99, 99, 73, 53, 83, 67, 97, 114, 106, 116, 99, 48, 109, 109, 117, 51, 51, 56, 77, 119, 89, 72, 52, 108, 106, 50, 49, 120, 117, 85, 61]

    
    key3_value = [101, 105, 75, 100, 103, 90, 102, 72, 43, 90, 53, 79, 80, 50, 87, 101, 48, 75, 50, 77, 101, 97, 104, 80, 104, 50, 57, 77, 122, 106, 122, 109, 89, 101, 102, 85, 55, 54, 85, 84, 104, 69, 79, 78, 68, 49, 108, 84, 115, 114, 103, 111, 99, 66, 116, 111, 71, 88, 118, 47, 108, 49, 119, 48, 88, 122, 114, 107, 120, 101, 84, 83, 117, 110, 81, 61]
    
    key1_value = [120, 109, 81, 80, 52, 121, 107, 77, 107, 112, 115, 107, 121, 122, 86, 117, 71, 88, 74, 68, 109, 73, 80, 74, 66, 110, 87, 111, 110, 72, 111, 56, 78, 50, 47, 112, 70, 108, 51, 98, 49, 82, 111, 73, 54, 88, 86, 87, 114, 53, 52, 118, 103, 85, 50, 105, 56, 105, 81, 61]
    
    key2_value = [71, 70, 105, 57, 111, 87, 98, 114, 68, 69, 101, 99, 113, 119, 98, 102, 85, 72, 76, 101, 85, 106, 66, 47, 119, 48, 86, 122, 97, 97, 49, 101, 99, 43, 57, 74, 73, 115, 68, 119, 87, 80, 109, 76, 103, 110, 71, 73, 119, 48, 68, 90, 78, 89, 97, 82, 105, 98, 99, 61]
    


if __name__ == '__main__':
    keys = ProjectKeys()
    key_len = False if len(keys.keyData) == 0 else True
    key1_len = False if len(keys.key1_value) == 0 else True
    key2_len = False if len(keys.key2_value) == 0 else True
    key3_len = False if len(keys.key3_value) == 0 else True
    result = reduce(lambda p,q: p and q, [key_len, key1_len, key2_len, key3_len])
    message = "Success" if result else "Failed"
    print(message)
