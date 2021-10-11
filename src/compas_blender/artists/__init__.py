"""
********************************************************************************
artists
********************************************************************************

.. currentmodule:: compas_blender.artists

Artists for visualising (painting) COMPAS data structures in Blender.


Base Classes
============

.. autosummary::
    :toctree: generated/

    BaseArtist


Classes
=======

.. autosummary::
    :toctree: generated/

    FrameArtist
    NetworkArtist
    MeshArtist
    RobotModelArtist

"""

from ._artist import BaseArtist  # noqa: F401
from .frameartist import FrameArtist
from .meshartist import MeshArtist
from .networkartist import NetworkArtist
from .robotmodelartist import (  # noqa: F401
    BaseRobotModelArtist,
    RobotModelArtist
)

__all__ = [
    'FrameArtist',
    'NetworkArtist',
    'MeshArtist',
    'RobotModelArtist'
]
