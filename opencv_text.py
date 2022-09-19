'''
CD D:\LYJ\DataAnalysis
streamlit run d:\lyj\dataanalysis\opencv_text.py

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python 清华镜像，下载速度快
'''

import streamlit as st
import cv2,os
from imutils import contours
import argparse
import imutils
import myutils

## 设置参数
# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",required=True,
#                 help="path to input image")
# ap.add_argument("-t","--template",required=True,
#                 help="path to template OCR-A image")
# args = vars(ap.parse_args())

## 指定信用卡类型
FIRST_NUMBER ={
    "3":"American Express",
    "4":"Visa",
    "5":"MasterCard",
    "6":"Discover Card"
}

def open_img(key,path='./pic'):
    files = os.listdir(path)
    file = st.sidebar.selectbox("",files,key=key)
    file_path = os.path.join(path,file)
    img = cv2.imread(file_path)
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

def sort_contours(cnts,method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # 用一个最小的矩形，把找到的形状包起来x,y,h,w
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts,boundingBoxes) = zip(*sorted(zip(cnts,boundingBoxes),
                                       key=lambda b: b[1][i],reverse=reverse))
    return cnts,boundingBoxes

def recog_nums(card,num):
    ref = cv2.cvtColor(num,cv2.COLOR_BGR2GRAY)
    # 二值转换
    ref = cv2.threshold(ref,10,255,cv2.THRESH_BINARY_INV)[1]
    # 计算轮廓 （只检测外轮廓）
    refCnts,hierarchy=cv2.findContours(ref.copy(),cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(num,refCnts,-1,(0,0,255),2)
    # 排序，从左到右，从上到下
    refCnts = sort_contours(refCnts,method="left-to-right")[0]
    digits = {}
    # 遍历每一个轮廓
    for (i,c) in enumerate(refCnts):
        #计算外界矩形并且resize成合适大小
        (x,y,w,h) = cv2.boundingRect(c)
        roi = ref[y:y+h, x:x+w]
        roi = cv2.resize(roi,(57,88))
        #每一个数字对应一个模板
        digits[i] = roi

    # 初始化卷积核
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

    gray = cv2.cvtColor(card,cv2.COLOR_BGR2GRAY)
    #礼帽操作，突出更明亮的区域
    tophat = cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,rectKernel)



    col1,col2,col3 = st.columns(3)
    col1.image(ref)
    col2.image(cv2.cvtColor(num,cv2.COLOR_BGR2RGB),"识别字数：{}".format(len(refCnts)))
    col3.image(tophat)


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
    st.sidebar.caption("选择卡片图")
    card_img = open_img(key=1)
    st.sidebar.caption("选择模板")
    temp_img = open_img(key=2)
    col1,col2 = st.columns(2)
    col1.image(cv2.cvtColor(card_img,cv2.COLOR_BGR2RGB))
    col2.image(cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB))

    if st.checkbox("开始识别"):
        recog_nums(card_img,temp_img)


if __name__ == '__main__':
    main()


