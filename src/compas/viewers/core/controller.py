from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

try:
    import PySide2
except ImportError:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtOpenGL
    import PySide.QtGui as QtWidgets
    from PySide.QtOpenGL import QGLWidget as QOpenGLWidget
else:
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtOpenGL
    from PySide2 import QtWidgets
    # from PySide2.QtWidgets import QOpenGLWidget
    from PySide2.QtOpenGL import QGLWidget as QOpenGLWidget

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


__author__    = ['Tom Van Mele', ]
__copyright__ = 'Copyright 2016 - Block Research Group, ETH Zurich'
__license__   = 'MIT License'
__email__     = 'vanmelet@ethz.ch'


__all__ = ['Controller', ]


class Controller(object):

    def __init__(self, app):
        self.app = app

    @property
    def view(self):
        return self.app.view

    def opengl_version_info(self):
        print(glGetString(GL_VENDOR))
        print(glGetString(GL_RENDERER))
        print(glGetString(GL_VERSION))
        print(glGetString(GL_SHADING_LANGUAGE_VERSION))
        print(self.view.format().majorVersion())
        print(self.view.context().format().majorVersion())

    def opengl_extensions(self):
        extensions = str(glGetString(GL_EXTENSIONS)).split(' ')
        for name in extensions:
            print(name)

    def opengl_set_version(self, version):
        major, minor = version
        gl_format = QtOpenGL.QGLFormat()
        gl_format.setVersion(major, minor)
        gl_format.setProfile(QtOpenGL.QGLFormat.CoreProfile)
        gl_format.setSampleBuffers(True)
        gl_format.setDefaultFormat(gl_format)
        self.view.context().setFormat(gl_format)
        self.view.context().create()
        self.view.glInit()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
