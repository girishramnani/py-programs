from PyQt4.QtCore import Qt, QRegExp
from PyQt4.QtGui import QSyntaxHighlighter, QSyntaxHighlighter, QTextCharFormat, QFont, QColor, QTextCharFormat

__author__ = 'Girish'


class PythonHighlighter(QSyntaxHighlighter):
    
    
    def __init__(self,parent):
        QSyntaxHighlighter.__init__(self,parent)
        self.highlightRules = []



        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)

        keywords = list(['print','if','else','elif','global','def','while','class','from','import','as','in','filter',"for","range"])
        self.highlightRules = [(QRegExp("\\b" + pattern + "\\b"), keywordFormat)
                for pattern in keywords]


        pattern = QRegExp("'[a-z|A-Z|0-9]'|\"[a-zA-Z0-9]*\"")
        charFormat = QTextCharFormat()
        charFormat.setForeground(QColor(80,120,0))
        self.highlightRules.append((pattern,charFormat))



        otherformats = QTextCharFormat()
        words= dir(object)+['self']
        otherformats.setForeground(QColor( 255/1.25,182/1.25,193/1.25))
        self.highlightRules.extend((QRegExp("\\b"+Opattern+"\\b"),otherformats) for Opattern in words)


        pattern = QRegExp(" [0-9]* ")
        numformat = QTextCharFormat()
        numformat.setForeground(Qt.blue)
        self.highlightRules.append((pattern,numformat))

    def highlightBlock(self, p_str):
        for pattern,format in self.highlightRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(p_str)
            while index >=0:
                length = expression.matchedLength()
                self.setFormat(index,length,format)
                index = expression.indexIn(p_str,index+length)
