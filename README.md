#《再要你命3k单词》默写出题程序

##起因

参加陈琦老师的330club让我见识了一种非常好的单词背诵方法，简单说就是把需要背诵的单词都写在一张纸上，然后看着英文默写中文，不求多准确，多义词写出所有的词义，但是一定要强迫自己去记忆。同时不断订正。

##使用过程

但是每次生成这个默写文件是非常耗费时间的，所以写了这个程序。主要使用过程是：

1. 从你指定的List号码中抽取所有单词，比如11,22,13,31,2。 这里所有数字需要用逗号隔开，同时保证输入数字在1~31之间(因为《再要你命3k》只有31个List)。当然这里是不要求顺序输入的，所以你可以1,15,31这样的跳着默写。
2. 将指定的数组中所有list的单词全部抽取出来并且乱序排序。
3. 然后生成两个txt文件，其中Eng.txt是所有的单词，而Chn.txt包含全部的对应Eng.txt英文的单词中文解释。
4. 这样你就可以用任何你喜欢的编辑器默写中文，对照订正。同时，你既可以使用电子版本默写订正，也可以使用利用word，WPS等文字处理软件的分栏功能进行分栏后打印出来，使用纸质版默写订正。
5. 当然你如果新建一个ChnNew.txt默写中文，在Linux下就可以使用Linux的`diff`命令，自动化检查。Windows用的不多，征求大家建议看有什么好的检查方法。

##使用步骤(以windows为例)


1. 解压win32and64.zip文件
2. 打开解压后文件，选择`dist`文件夹进入，可以看到`ZYNM3k.exe`这个程序，点击打开
3. 在出现的文本框中输入如下的数字串，1,2,3。使用英文输入逗号，不要有空格
4. 点击`RUN`按钮就可以在当前文件夹看到生成的`Chn.txt`和`Eng.txt`

至于Linux的使用者，我公布了源代码，直接运行源代码都是可以的。如果使用打包后的程序可能可能需要赋予执行权限。

##技术细节：

Crack3kGREWords主要使用Python，同时使用SQLite作为数据后台存储单词的中英文，Tkinter制作GUI界面。然后利用cxfreeze生成Linux可执行程序，py2exe生成可以windows使用的执行程序。

##注意

windows版本32位和64位操作系统都可以使用，Linux只在64位的Ubuntu14.04测试成功

# Crack3kGREWords

Crack3kGREWords helps you remember GRE word essence 

Crack3kGREWords uses python as the main language and SQLite to store the data and Tkinter for GUI.
