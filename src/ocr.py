# -*- coding: utf-8 -*-
from PIL import Image
from typing import List
import sys
import os
import pyocr
import pyocr.builders


# tesseract-ocrを使うこと前提よ
def call_ocr(tool_num:int = 0):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        sys.exit(1)
    if tool_num > len(tools):
        return tools[0]
    return tools[tool_num]

class OcrMachine(object):
    def __init__(self, tool_num:int = 0):
        self.__tool = call_ocr(tool_num)
    
    @property
    def tool(self):
        return self.__tool
    
    # 画像から文字を抽出
    def run_ocr(self, img_path:str, use_lang:str = "jpn", layout_num:int = 6)->List[str]:
        get_sentences = self.tool.image_to_string(
                Image.open(img_path),
                lang = use_lang,
                builder = pyocr.builders.TextBuilder(tesseract_layout = layout_num)
                )
        return get_sentences.split("\n")
    
    def write_result(self, img_path:str, output_dir_path= os.path.join(os.getcwd(), "result"), use_lang:str = "jpn", layout_num:int = 6):
        if os.path.exists(output_dir_path) is False:
            os.mkdir(output_dir_path)
        result_file_name = os.path.basename(img_path).split(".")[0] + ".txt"
        result_path = os.path.join(output_dir_path, result_file_name)
        ocr_result = self.run_ocr(img_path, use_lang, layout_num)
        with open(result_path, "w") as result_file:
            for line in ocr_result:
                result_file.write(line)
                result_file.write("\n")
  