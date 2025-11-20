<h1 style="text-align:center">pyqt5</h1>

---

### 配置external tools：

- pyqt5-designer.exe

Program:?\Scripts\designer.exe
Working directory:$FileDir$

- pyqt5-pyuic.exe

Description:convert .ui to .py
Program:?\Scripts\pyuic5.exe
Arguments:$FileName$ -o $FileNameWithoutExtension$.py
Working directory:$FileDir$

- pyqt5-pyrcc.exe

Description:convert .qrc to .py
Program:?\Scripts\pyrcc5.exe
Arguments:$FileName$ -o $FileNameWithoutExtension$.py
Working directory:$FileDir$
