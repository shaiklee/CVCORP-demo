if __name__ == "__main__":
    # print("Transaction Pipeline")
    # process_transactions("transactions.txt")
    print("Build Index")
    build_index("knowledge.txt")
    print("Query System")
    query_system()

import os
import sys
from contextlib import contextmanager
#
#
def secure_opener(path, flags):
    return os.open(path, flags, 0o600)

#
#
#
class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file (Custom Manager)")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file (Custom Manager)")
        if self.file:
            self.file.close()
#
#
#
@contextmanager
def managed_file(filename, mode):
    print("Opening file (Decorator Manager)")
    f = open(filename, mode, encoding="utf-8")
    try:
        yield f
    finally:
        print("Closing file (Decorator Manager)")
        f.close()
#
#
#
def file_handling_demo():
    f = open(
        "demo.txt",
        mode="w+",#'r', 'w', 'a', 'x', 'b', 't', '+'
        buffering=1,#-ve -> default, 0 -> binary, 1->words, x>1 -> x bytes
        encoding="utf-8",
        errors="strict",#'strict', 'ignore', 'replace', 'surrogateescape'
        newline="\n"
    )
    # WRITE METHODS
    f.write("Line 1\n")
    f.write("text writing")
    f.writelines(["Line 2\n", "Line 3\n"])
    f.flush()
    print("Current position:", f.tell())
    f.seek(0)
    print("Read all:", f.read())# whole file
    f.seek(0)
    print("Readline:", f.readline())# file lo okka line
    f.seek(0)
    print("Readlines:", f.readlines())# list of all lines in file
    f.truncate()
    f.close()
    with open("print_output.txt", "a") as f:
        print("testing with append", file=f)
    sys.stdin = open("print_output.txt", "r")
    print("Input read:", input())
    print(input())
    sys.stdin.close()
    fd = os.open("fd_demo.txt", os.O_CREAT | os.O_WRONLY)
    print(fd)
    f = open(fd, "w", closefd=True)
    f.write("Written using file descriptor\n")
    f.flush()
    os.fsync(f.fileno())
    f.close()



    with open("secure.txt", "w", opener=secure_opener) as f:
        f.write("Secure file with 600 permission")



    with CustomFileManager("custom.txt", "w") as f:
        f.write("Using class-based context manager\n")



    with managed_file("decorator.txt", "w") as f:
        f.write("Using decorator-based context manager\n")



    with open("state.txt", "w+") as f:
        print("Readable:", f.readable())
        print("Writable:", f.writable())
        print("Seekable:", f.seekable())

        f.write("Testing state\n")
        f.seek(0)
        print("Content:", f.read())



    with open("demo.txt", "r") as f:
        for line in f:
            print("Iter:", line.strip())

file_handling_demo()
# import sys

# Question 1
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("Number of characters:", len(content))







with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if len(line.strip()) > 10:
            print(line.strip())


with open("sample.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


with open("sample.txt", "a") as file:
    file.write("Line 4\n")
    file.write("Line 5\n")


with open("sample.txt", "r") as file:
    print(file.read())

with open("sample.txt", "r") as file:
    first_part = file.read(10)
    print("First 10 characters:", first_part)

    position = file.tell()
    print("Cursor position after reading 10 chars:", position)

    file.seek(0)
    print("Cursor moved to beginning.")

    full_content = file.read()
    print("Full content:\n", full_content)

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        self.file.write("This is written inside __enter__\n")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        if exc_type:
            print("Exception occurred:")
            print("Type:", exc_type)
            print("Value:", exc_value)
        return False



with FileManager("sample.txt") as f:
    f.write("Writing more data inside with block\n")


from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()
        print("File closed safely.")



with open_file("sample.txt", "r") as f:
    print(f.read())


with open("sample.txt", "r") as file:
    while True:
        chunk = file.read(5)
        if not chunk:
            break
        print("Chunk:", chunk)
        print("Cursor position:", file.tell())

    file.seek(10)
    print("\nMoved cursor to position 10\n")
    while True:
        chunk = file.read(5)
        if not chunk:
            break
        print("Chunk after seek:", chunk)
        print("Cursor position:", file.tell())

#




#Question 1
#open a file using context manager
with open("test.txt", "r") as t:
    print(t.read())
    t.seek(0)
    # print(t.readline(10))
    c=0
    for i in t:
        c+=len(i)
    print(c)
    t.seek(0)
    print(len(t.read()))

with open("test.txt",'r') as f:
    for i in f.readlines():
        if len(i)>10:
            print(i[:-2])
with open("demo.txt",'w+') as f:
    f.write("hello world\n")
    f.writelines(["how are you\n", "thinnara\n"])
    f.seek(0)
    print(f.read())

class open_file:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode=mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File opened successfully")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed successfully")


with open_file("test.txt", "w+") as f:
    f.write("Hello World")
    f.seek(0)
    print(f.read())

@contextmanager
def open_file(fn, mode):
    print("opening file")
    with open(fn, mode) as f:
        yield f
        print("intermediate file")

    print("outside open")
    print("closing file")



with open_file("test.txt", "w+") as f:
    print(f)




from contextlib import contextmanager

class A:
    def __init__(self, a):
        self.a = a
    def __enter__(self):
        print(f"entered the CM for file")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exited the CM")


with A(5) as obj:
    print(obj.a)
    print("inside CM")

class File_CM:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        print(f"entered the CM for file {self.file_name}")
        self.file=open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exited the CM")
        self.file.close()

with File_CM("test.txt", "w") as f:
    f.write("hello")

@contextmanager
def file_cm(file_name,mode):
    f=open(file_name,mode)
    try:
        yield f
    except Exception as e:
        print(e)
        f.close()
with file_cm("test.txt","r") as f:
    print(f.read())



with open("demo.txt", "w") as f:
    f.write("Hello World")
    print("hello", file=f)
sys.stdin=open("demo.txt")
print(input())
