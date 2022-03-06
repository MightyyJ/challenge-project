FROM python:3
ADD app.py /
ADD empty_file.txt /
ADD moby_dick.txt /
CMD ["python", "./app.py", "./empty_file.txt", "./moby_dick.txt"]