icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/目标检测.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # 添加图标
        MainWindow.setWindowIcon(icon)
        
        # 创建主控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建模块一
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 185, 890, 483))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        # 创建“目标位置”模块
        
        self.frame_object = QtWidgets.QFrame(self.frame)
        self.frame_object.setGeometry(QtCore.QRect(0, 0, 483, 394))
        self.frame_object.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_object.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_object.setObjectName("frame_object")
        
        
        # 创建“检测结果”模块
        
        self.frame_result = QtWidgets.QFrame(self.frame)
        self.frame_result.setGeometry(QtCore.QRect(0, 395, 483, 225))
        self.frame_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result.setObjectName("frame_result")
        
        # 创建模块二
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(483, 185, 966, 890))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # 创建“图片”模块
        self.frame_label = QtWidgets.QFrame(self.frame_2)
        self.frame_label.setGeometry(QtCore.QRect(0, 0, 966, 394))
        self.frame_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label.setObjectName("frame_label")
        
        # 添加图片
        self.label_show = QtWidgets.QLabel(self.frame_label)
        self.label_show.setGeometry(QtCore.QRect(0, 0, 965, 393))
        self.label_show.setMinimumSize(QtCore.QSize(965, 393))
        self.label_show.setMaximumSize(QtCore.QSize(965, 393))
        self.label_show.setStyleSheet("border-image: url(:/icons/ui_imgs/2.png);")
        self.label_show.setText("")
        self.label_show.setObjectName("label_show")
        
        
        
        # 创建“表格”模块
        
        self.frame_table = QtWidgets.QFrame(self.frame_2)
        self.frame_table.setGeometry(QtCore.QRect(0, 619, 966, 271))
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        
        # 添加表格
        self.groupBox_3 = QtWidgets.QWidget(self.frame_table)
        self.groupBox_3.setGeometry(QtCore.QRect(0,10,966,271))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        
        
        # 创建模块三
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1449, 185, 471, 890))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        
        # 创建“文件”模块
        self.frame_file = QtWidgets.QFrame(self.frame_3)
        self.frame_file.setGeometry(QtCore.QRect(0, 0, 471, 890))
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        
        
        # 创建“操作”模块
        self.frame_action = QtWidgets.QFrame(self.frame_3)
        self.frame_action.setGeometry(QtCore.QRect(0, 395, 483, 225))
        self.frame_action.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_action.setObjectName("frame_action")