my_var = 10

str_var = str(my_var)
print(str_var, type(str_var))

# 1. Dấu nháy kép: "Hello"
# 2. Dấu nháy đơn: 'Hello'
# 3. Cặp ba dấu nháy kép: """Multi-line string""" 
    # thường dùng trong trường hợp văn bản có nhiều dòng
# 4. Cặp ba dấu nháy đơn: '''Multi-line string'''

# my_str = '''fshfkjdsf'''

# print(my_str)

# str1 = "Hello"
# str2 = "MindX"

# # Tạo ra string mới không liên quan đến những string cũ
# # Lặp string: Toán tử *
# str3 = str1 * 3

# first_name = input("Nhap ho: ")
# last_name = input("Nhap ten: ")

# # String Interpolation
# info = f"""
# First Name: {first_name}
# Last Name: {last_name}
# """

# len (length): Trả về chiều dài của chuỗi ký tự


# Cách đánh vị trí: Bắt đầu từ 0 -> độ dài - 1
# Cách đánh vị trí 2: Bắt đầu từ -1 -> -độ dài
# my_str = "Hello MindX JJDSHGKJSHGKHFGKJHK" # -1 -> -5
# print(my_str[ -len(my_str) ])

# Lấy chuỗi con trong chuỗi cha
my_str = "Hello Hoang"
my_str[0] = 'K'
print(my_str)
# Slicing: start:end-1:step
# 2:7:1 -> 2, 3, 4, 5, 6
# 2:7:2 -> 2, 4, 6
# print(
#     my_str[6] + my_str[7] 
#     + my_str[8] + my_str[9] 
#     + my_str[10])
# 6->10
# start:end+1:step
# print(my_str[6:11:1])