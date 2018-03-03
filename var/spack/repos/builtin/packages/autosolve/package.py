##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install autosolve
#
# You can edit this file again by typing:
#
#     spack edit autosolve
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Autosolve(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "autosolve"
    
    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', git='https://github.com/bast/cmake-example.git')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('boost@1.65.1~atomic~chrono~clanglibcpp~date_time~debug~exception~filesystem~graph~icu+iostreams~locale~log~math~mpi+multithreaded +program_options~python~random~regex+serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave')
    depends_on('cmake@3.9.4')
    depends_on('openmpi@2.1.2')
    depends_on('hwloc -libxml2')
    depends_on('dealii@8.5.1 -arpack -gsl -metis -oce -python -slepc +mpi +p4est +trilinos +petsc +netcdf +hdf5')
    depends_on('cgal')
	depends_on('trilinos -exodus')