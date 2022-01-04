# 提取pdf文件中的图片
import os
import fitz

def extract_image(file):
    dir_name = os.path.dirname(file)
    file_name = os.path.splitext(os.path.basename(file))[0]  # 不包含后缀的文件名
    print(dir_name, file_name)
    pdf_document = fitz.open(file)
    if not os.path.isdir(f"{dir_name}/{file_name}"):
        os.mkdir(f"{dir_name}/{file_name}")
    for current_page in range(len(pdf_document)):
        for image in pdf_document.get_page_images(current_page):
            xref = image[0]
            pix = fitz.Pixmap(pdf_document, xref)
            if pix.n < 5:        # this is GRAY or RGB
                pix.save(f"{dir_name}/{file_name}/page{current_page}-{xref}.png")
            else:                # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(f"{dir_name}/{file_name}/page{current_page}-{xref}.png")


if __name__ == '__main__':
    extract_image("/Users/ltc/Documents/学习资料/行业研究/达摩院2022十大科技趋势.pdf")
