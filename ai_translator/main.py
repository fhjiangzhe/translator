import gradio as gr
import sys
import os
import shutil
from translator import PDFTranslator

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def translate_pdf(file, source_lang, target_lang):
    # 检查文件对象是否为空
    if file is None:
        return "未上传任何文件"

    # 上传文件保存到指定目录
    save_path = "saved_files"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    destination = os.path.join(save_path, os.path.basename(file.name))
    shutil.copy(file.name, destination)

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator("chatglm2")
    translated_file_path = translator.translate_pdf(destination, "markdown", source_lang, target_lang, pages=None)

    return translated_file_path


iface = gr.Interface(
    fn=translate_pdf,
    inputs=[
        gr.inputs.File(label="上传待翻译PDF文件"),
        gr.inputs.Dropdown(choices=['English', 'Chinese', 'Spanish'], default='English', label="源语言"),
        gr.inputs.Dropdown(choices=['English', 'Chinese', 'Spanish'], default='Chinese', label="目标语言")
    ],
    outputs=[
        gr.outputs.File(label="下载翻译后的文件")
    ],
    live=False
)

iface.launch(share=True, server_name="0.0.0.0")
