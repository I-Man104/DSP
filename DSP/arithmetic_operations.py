# def addition():
#     file_path1 = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path1:
#         return

#     file_path2 = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path2:
#         return

#     first = read_file(file_path1)
#     second = read_file(file_path2)

#     max_len = max(len(first), len(second))

#     # Append zeros to the shorter signal
#     while len(first) < max_len:
#         first.append((0, 0))
#     while len(second) < max_len:
#         second.append((0, 0))

#     result_points = [(x, y1 + y2) for (x, y1), (_, y2) in zip(first, second)]

# def subtraction():
#     file_path1 = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path1:
#         return

#     file_path2 = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path2:
#         return

#     points1 = read_file(file_path1)
#     points2 = read_file(file_path2)

#     max_len = max(len(points1), len(points2))

#     # Append zeros to the shorter signal
#     while len(points1) < max_len:
#         points1.append((0, 0))
#     while len(points2) < max_len:
#         points2.append((0, 0))

#     result_points = [(x, y1 - y2) for (x, y1), (_, y2) in zip(points1, points2)]

    
# def multiplication():
#     file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path:
#         return

#     constant = simpledialog.askfloat("Multiplication", "Enter a constant value:")
#     if constant is None:
#         return

#     points = read_file(file_path)

#     result_points = [(x, y * constant) for (x, y) in points]

# def squaring():
#     file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path:
#         return

#     points = read_file(file_path)

#     result_points = [(x, y ** 2) for (x, y) in points]

# def shifting():
#     file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path:
#         return

#     shift = simpledialog.askfloat("Shifting", "Enter a shift value:")
#     if shift is None:
#         return

#     points = read_file(file_path)

#     result_points = [(x + shift, y) for (x, y) in points]

# def normalization():
#     file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path:
#         return

#     normalize_option = simpledialog.askstring("Normalization", "Choose normalization (0-1 or -1-1):")
#     if normalize_option not in ("0-1", "-1-1"):
#         print("Invalid normalization option.")
#         return

#     points = read_file(file_path)

#     if normalize_option == "0-1":
#         min_y = min(y for (_, y) in points)
#         max_y = max(y for (_, y) in points)
#         result_points = [(x, (y - min_y) / (max_y - min_y)) for (x, y) in points]
#     else:  # -1-1 normalization
#         min_y = min(y for (_, y) in points)
#         max_y = max(y for (_, y) in points)
#         max_abs_y = max(abs(y) for (_, y) in points)
#         result_points = [(x, (2 * (y / max_abs_y) - 1)) for (x, y) in points]

   

# def accumulation():
#     file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
#     if not file_path:
#         return

#     points = read_file(file_path)

#     accumulated_signal = [(x, 0) for x, _ in points]

#     for i, (_, y) in enumerate(points):
#         accumulated_signal[i] = (points[i][0], sum(y for _, y in points[:i+1]))