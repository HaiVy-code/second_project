# Bài tập 2.3 (Sáng tạo):

# Tạo một cửa sổ với tiêu đề "Hộp thoại của tôi".
# Chèn 2 Text: một dòng giới thiệu tên bạn, một dòng ghi "Học GUI thật thú vị!".
# Thử thay đổi màu chữ từng dòng.

from guizero import App, Text

cuaso = App("Hop thoai cua toi")

chu1 = Text(cuaso, "Toi la Hai Vy")

chu1.text_color = "#D08AFF"

chu2 = Text(cuaso, "Hoc GUI that thu vi")

chu2.text_color = "#83CDFF"

cuaso.display()