#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path


class FileInfo(object):

    """统计文件的数字字符个数、
       非空白数字个数、
       空白字符个数、
       文件行数、
       文件所在路径"""

    def __init__(self, file_path, encoding_type="utf-8"):
        self.file_path = file_path
        self.encoding_type = encoding_type
        while True:
            if not os.path.exists(self.file_path):
                self.file_path=input("实例化的文件路径不存在，请重新输入：")
            else:
                break

    def get_file_content(self):
        content = ""
        with open(self.file_path, encoding=self.encoding_type) as fp:
            content = fp.read()
        return content

    def count_number_str(self):

        """统计文件中的数字字符个数"""

        count = 0
        content = self.get_file_content()
        for i in content:
            if i>="0" and i<="9":
                count+=1
        return count

    def count_not_space_str(self):

        """统计文件中的非空白字符个数"""

        count =0
        content = self.get_file_content()
        for i in content:
            if not i.isspace():
                count += 1
        return count

    def count_space_str(self):

        """统计文件中的空白字符个数"""

        count =0
        content = self.get_file_content()
        for i in content:
            if i.isspace():
                count += 1
        return count

    def count_lines(self):

        """统计文件中的行数"""

        count = 0
        content = self.get_file_content()
        for i in content.split("\n"):
            count += 1
        return count


class Advanced_FileInfo(FileInfo):

    """高级的文件信息处理类"""

    def __init__(self, file_path, encoding_type="utf-8"):
        FileInfo.__init__(self, file_path, encoding_type="utf-8")

    def get_content_by_line_num(self, line_number):
        try:
            return self.get_file_content().split("\n")[line_number-1]
        except:
            return None

    def print_file_info(self):
        print("文件的统计信息如下：")
        print("文件中包含的数字数量:%s" % self.count_number_str())
        print("文件中包含的非空白字符数量:%s" % self.count_not_space_str())
        print("文件中包含的空白字符数量:%s" % self.count_space_str())
        print("文件中包含的行数:%s" % self.count_lines())


fi = Advanced_FileInfo("d:\\python\\data.txt")
print("获取第一行的文件内容：", fi.get_content_by_line_num(1))
fi.print_file_info()