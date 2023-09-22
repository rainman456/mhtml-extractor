import os
import argparse
import re
# Function to extract the embedded image from the MHTML file
def extract_images(input_file,output_folder):
    pattern=re.compile(b'\xff\xd8[\s\S]*?\xff\xd9')
    with open(input_file, 'rb') as fp:
        data = fp.read()
    extension='jpg'
    lisr=re.findall(pattern,data)
    for i,huy in enumerate(lisr):
        output_file = os.path.join(output_folder, f'file{i}.{extension}')
        with open(output_file, 'wb') as gp:
            gp.write(huy)
        print(f"file written as  {output_file} in  folder")
    pattern2=re.compile(b'\x89PNG\r\n\x1a\n[\s\S]*?\x00IEND\xaeB`\x82')
    with open(input_file, 'rb') as fi:
        data2 = fi.read()
    extension='png'
    lisr=re.findall(pattern2,data)
    for j,hut in enumerate(lisr):
        output_file = os.path.join(output_folder, f'file{j}.{extension}')
        with open(output_file, 'wb') as gp:
            gp.write(hut)
        print(f"file written as  {output_file} in  folder")
    pattern3=re.compile(b'RIFF\x82,\x00\x00WEBPVP8 v,[\s\S]*?\x00')
    with open(input_file, 'rb') as fi:
        data2 = fi.read()
    extension='webp'
    lisr=re.findall(pattern3,data)
    for k,hyt in enumerate(lisr):
        output_file = os.path.join(output_folder, f'file{k}.{extension}')
        with open(output_file, 'wb') as gp:
            gp.write(hyt)
        print(f"file written as  {output_file} in  folder")
def extract_htmlcss(input_file,output_folder):
    with open(input_file, 'rb') as fp:
        data = fp.read()
        text=data.decode('utf-8','backslashreplace')
    if 'Content-Type: text/html' in text:
        extension = 'html'
        print("yess")
        start = text.find('<html')
        foo=text.find('</html>')+ 7
        htl=text[start:foo]

    output_file = os.path.join(output_folder, f'file.{extension}')
    with open(output_file, 'wb') as html_file:
        html_file.write(htl.encode('utf-8'))
    print(f"file written as  {output_file} in  folder")
    
    if 'Content-Type: text/css' in text:
        extension = 'css'
        print("yess")
        marker='Content-Type: text/css'
        start=0
        while start < len(text):
            start = text.find(marker, start)
            if start == -1:
                break
        #Add the bytes from the marker until the end of the image to the list
            end = text.find('------MultipartBoundary--', start)  # JPEG end marker
            if end != -1:
                hts=text[start:end + 2]
                start = end + 2
            else:
                break
    output_file = os.path.join(output_folder, f'file.{extension}')
    with open(output_file, 'wb') as css_file:
        css_file.write(hts.encode('utf-8'))
    print(f"file written as  {output_file} in  folder")
        
def main():
    parser = argparse.ArgumentParser(description="Extract and save an embedded image from an MHTML file.")
    parser.add_argument("input_file", help="Path to the input MHTML file")
    #parser.add_argument("output_folder", help="Path to the output folder where the image will be saved")

    args = parser.parse_args()
    input_file = args.input_file
    output_folder = input_file.replace('.mhtml',"")

    if not os.path.isfile(input_file):
        print("Input file does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extract_images(input_file, output_folder)
    extract_htmlcss(input_file, output_folder)

if __name__ == "__main__":
    main()
