from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import click
import re


# 创建一个命令组
@click.group()
def cli():
    pass

@click.command(name='split')
@click.option(
    "--split",
    "-s",
    "split_point",
    default=None,
    help="从那页开始拆分,逗号进行分拼接",
    type=str,
)
@click.option(
    "--input",
    "-i",
    "input_path",
    default="./demo.pdf",
    prompt="输入要拆分的PDF文件或文件夹",
    help="需要拆分的文件或文件夹",
    type=str,
)
@click.option(
    "--output",
    "-o",
    "output_dir",
    default="./",
    prompt="文件输出目录",
    help="指定文件输出目录",
    type=str,
)
@click.option(
    "--search-str",
    "-ss",
    "search_str",
    default=None,
    help="指定在PDF中搜索的字符串",
    type=str,
)
def split_pdf(input_path, output_dir, split_point, search_str):
    input_path = Path(input_path)
    output_path = Path(output_dir)

    # 检查输入文件和输出目录
    if input_path.is_dir():
        pdf_files = [f for f in input_path.glob("*.pdf")]
        if not pdf_files:
            print(f"No PDF files found in the directory: {input_path}")
            return
    elif input_path.is_file() and input_path.suffix.lower() == ".pdf":
        pdf_files = [input_path]
    else:
        print(
            f"Invalid input. Please provide a valid PDF file or folder containing PDF files."
        )
        return

    output_path.mkdir(parents=True, exist_ok=True)



    # 拆分PDF
    # 处理每个 PDF 文件
    for pdf_file in pdf_files:
        try:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            print(f"The PDF has {num_pages} pages")

            # 查找指定字符串
            start_page = None
            if search_str:
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text and search_str.lower() in text.lower():
                        start_page = i
                        print(
                            f"Found '{search_str}' on page {i + 1}. Starting split from this page."
                        )
                        break

            if start_page is None and split_point is None:
                print(f"'{search_str}' not found in the PDF.")
                return
            split_points = []
            if split_point is not None :
                try:
                    split_points = [
                        num
                        for i in split_point.split(",")
                        if (num := int(i.strip())) >= 1 and num <= num_pages
                    ]
                except ValueError as e:
                    print(f"Error converting points:{e}")
            # 加上起始页和结束页,并且进行去重
            split_points = [0]+ split_points+[start_page]+ [num_pages]
            split_points = sorted(set([x for x in split_points if x is not None]))
            print(f"--------------------------------{split_points}")
            print(f"Splitting at pages:{split_points[1:-1]}")

            for i in range(len(split_points) - 1):
                writer = PdfWriter()
                for j in range(split_points[i], split_points[i + 1]):
                    page = reader.pages[j]
                    writer.add_page(page)
                output_file = Path.joinpath(
                    output_path, pdf_file.stem + str(i+1) + pdf_file.suffix
                )
                with open(output_file, "wb") as f:
                    writer.write(f)
                print(f"Saved:{output_file}")

            print(
                f"PDF has been split int {len(split_points)-1} parts in {output_path}."
            )
        except Exception as e:
            print(f"An error occurred:{e}")


# 合并PDF的命令
@click.command(name="merge")
@click.option(
    "--input",
    "-i",
    "input_path",
    default="./",
    prompt="输入要合并的PDF文件夹",
    help="需要合并的PDF文件夹",
    type=str,
)
@click.option(
    "--output",
    "-o",
    "output_file",
    default="./merged_output.pdf",
    prompt="合并后输出的PDF文件路径",
    help="合并后的输出文件",
    type=str,
)
@click.option(
    "--reg",
    "-reg",
    "regx",
    default="1.pdf",
    prompt="输入要合并的文件结尾",
    help="输入要合并的文件结尾",
    type=str,
)
def merge_pdfs(input_path, output_file,regx):
    input_path = Path(input_path)
    output_path = Path(output_file)

    # 检查输入文件夹是否存在PDF文件
    if not input_path.is_dir():
        print(f"The provided path is not a directory: {input_path}")
        return

    pdf_files = sorted([f for f in input_path.glob("*"+regx)], key=lambda x: int(re.search(r'专项(\d+)', x.name).group(1)))
    print(f"---{pdf_files}")
    if not pdf_files:
        print(f"No PDF files found in the directory: {input_path}")
        return

    writer = PdfWriter()

    # 合并所有PDF文件
    for pdf_file in pdf_files:
        try:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Added {pdf_file} to the merged file.")
        except Exception as e:
            print(f"An error occurred while reading {pdf_file}: {e}")

    # 保存合并后的文件
    try:
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"PDFs merged successfully into {output_path}.")
    except Exception as e:
        print(f"An error occurred while saving the merged PDF: {e}")



# 将子命令添加到命令组
cli.add_command(split_pdf)  # 添加拆分命令
cli.add_command(merge_pdfs)          # 添加合并命令


if __name__ == "__main__":
    cli()
