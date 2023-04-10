def ret():
    return {
        "fake": ["image1_f.png","image2_f.png","image3_f.png","image4_f.png","image5_f.png","image6_f.png","image7_f.png","image8_f.png","image9_f.png","image10_f.png","image11_f.png","image12_f.png","image13_f.png","image14_f.png","image15_f.png","image16_f.png","image17_f.png","image18_f.png","image19_f.png","image20_f.png","image21_f.png","image22_f.png","image23_f.png",]
    }

d=ret()
def class_x(filename):
    if filename in d["fake"]:
        return 0
    return 1

