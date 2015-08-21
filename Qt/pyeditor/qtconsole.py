from PyQt4 import QtGui

__author__ = 'Girish'
from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager

def put_ipy(parent):
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt4'

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    kernel_client.namespace  = parent

    def stop():
        kernel_client.stop_channels()
        kernel_manager.shutdown_kernel()

    layout = QtGui.QVBoxLayout(parent)
    widget = RichIPythonWidget(parent=parent)
    layout.addWidget(widget)
    widget.kernel_manager = kernel_manager
    widget.kernel_client = kernel_client
    widget.exit_requested.connect(stop)
    ipython_widget = widget
    ipython_widget.show()
    kernel.shell.push({'widget':widget,'kernel':kernel, 'parent':parent})
    return {'widget':widget,'kernel':kernel}

app = QtGui.QApplication([])
win = QtGui.QWidget(None)
win.show()
put_ipy(win)
