# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Recorder(AutotoolsPackage):
    """A multi-level library for understanding I/O
    activity in HPC applications."""

    homepage = "https://github.com/uiuc-hpc/Recorder"
    url      = "https://github.com/uiuc-hpc/Recorder/archive/v2.1.4.tar.gz"

    maintainers = ['wangvsa']

    version('2.1.4', sha256='f66756595a7f310929c247ae03fd08a18d9843f578fffa1e3072f557bf5a158e')

    variant('posix', default=True, description="Enable POSIX level tracing")
    variant('mpi', default=True, description="Enable MPI level tracing. MPI is required even with this option turn off")
    variant('hdf5', default=True, description="Enable HDF5 level tracing. HDF5 is required even with this option turn off.")

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('mpi')
    depends_on('hdf5')

    def configure_args(self):
        args = []
        if "+posix" not in self.spec:
            args += ["--disable-posix"]
        if "+mpi" not in self.spec:
            args += ["--disable-mpi"]
        if "+hdf5" not in self.spec:
            args += ["--disable-hdf5"]

        return args
