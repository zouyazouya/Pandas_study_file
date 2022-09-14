'''
CD D:\LYJ\DataAnalysis
streamlit run d:\lyj\dataanalysis\opencv_text.py

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python 清华镜像，下载速度快
'''

import streamlit as st
import cv2,os
from PIL import Image

def open_img(path='.'):
    files = os.listdir(path)
    file = st.sidebar.selectbox("选择图片",files)
    file_path = os.path.join(path,file)
    img_color = st.sidebar.selectbox("选择颜色",["彩色","灰度"])
    if img_color == "彩色":
        img = cv2.imread(file_path,cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    return img

def open_video():
    vc = cv2.VideoCapture('./sample.mp4')
    if vc.isOpened():
        open, frame = vc.read()  # open 为布尔值
    else:
        open = False

    while open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)
            if cv2.waitKey(10) & 0xFF == 27:
                break
    vc.release()
    cv2.destroyAllWindows()

def border_fill(img):
    top_size,bottom_size,right_size,left_size = (50,50,50,50)
    replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)
    col1,col2,col3 = st.columns(3)
    col1.image(replicate,"replicate")
    col2.image(reflect,"reflect")
    col3.image(reflect101,"reflect101")
    col1, col2, col3 = st.columns(3)
    col1.image(wrap,"wrap")
    col2.image(constant,"constant")
    st.text('''
    BORDER_REPLICATE: 复制法，也就是复制最边缘像素。
    BORDER_REFLECT: 反射法，对感兴趣的图像中的像素在两边进行复制。例如：fedcba|abcdefgh|hgfedcb
    BORDER_REFLECT_101: 反射法，也就是以最边缘像素为轴，对称。gfedcb|abcdefgh|gfedcba
    BORDER_WRAP: 外包装法。cdefgh|abcdefgh|abcdefg
    BORDER_CONSTANT: 常量法，常数值填充。
    ''')

def main():
    # 标题
    html_temp='''
    <div style="background-color:tomato;">
    <h1 style="color:white;">opencv测试
    </h1>
    </div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)

## 打开图片
    img = open_img()
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(img1)

## 打开视屏
    if st.button("视频演示开始"):
        open_video()

## 截取部分图像数据
    img2 = img1[600:900,300:600]
    with col2:
        st.image(img2)

## 颜色通道提取
    b,g,r = cv2.split(img)
    color_ch = st.sidebar.selectbox("选择颜色通道",["B","G","R"])
    with col3:
        if color_ch=="R":
            img[:,:,2]=0
            img[:,:,1]=0
            st.image(img)
        elif color_ch == "G":
            img[:, :, 0] = 0
            img[:, :, 2] = 0
            st.image(img)
        else:
            img[:, :, 0] = 0
            img[:, :, 1] = 0
            st.image(img)

## 边界填充
    border_fill(img1)

## 数值计算


if __name__ == '__main__':
    main()


