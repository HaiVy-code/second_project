# Bài tập 2.1 (Cơ bản):

# Tạo cửa sổ kích thước 600x400, tiêu đề "Luyện tập Bài 2".

# Bài tập 2.2 (Định dạng):

# Đặt màu nền là "lightblue".
# Thêm một Text "Xin chào, tôi đang học GUIZERO", màu "red", size 16.

from guizero import App, Text

cuaso = App("Luyen tap Bai 2")

cuaso.width = 600

cuaso.height = 400

chu = Text(cuaso, "Xin chao, toi dang hoc GUIZERO")

cuaso.bg = "lightblue"

chu.align = "top"

chu.text_color = "red"

chu.size = 16

cuaso.display()


