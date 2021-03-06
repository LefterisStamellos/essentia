# Copyright (C) 2006-2016  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/

#!/usr/bin/python


def test():
  try:
    import essentia
    import os
    #from essentia.extractor import essentia_music
    from essentia import essentia_extractor
    #options, args = essentia_extractor.parse_args()
    #exec('options = ' + str(options))
    essentia_extractor.compute('music', "../../audio/recorded/britney.wav","foo.sig")
    os.unlink("foo.sig")
    return 0
  except:
    raise
    print "Failed to run essentia_music"
    return 1
